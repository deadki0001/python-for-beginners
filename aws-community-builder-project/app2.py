import logging
import json
from playwright.sync_api import sync_playwright
import requests
from geopy.geocoders import Nominatim
import time

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize headers and geolocator
headers = {'User-Agent': 'AwsGlobalMap/1.0'}
geolocator = Nominatim(user_agent="AwsGlobalMap", timeout=10)  # Increase timeout to 10 seconds

# Continent mapping
continent_map = {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
        "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti",
        "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia",
        "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia",
        "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco",
        "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
        "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
        "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan",
        "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia",
        "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
        "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea",
        "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia",
        "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand",
        "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan",
        "Vietnam", "Yemen"
    ],
    "Europe": [
        "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
        "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
        "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia",
        "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
        "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"
    ],
    "North America": [
        "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica",
        "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala",
        "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
        "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States", "USA"
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
        "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
    ],
    "Oceania": [
        "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru",
        "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
        "Tonga", "Tuvalu", "Vanuatu"
    ]
}


def normalize_location(location):
    """Normalize location and map to a continent."""
    for country, continent in continent_map.items():
        if country.lower() in location.lower():
            return continent
    return "Unknown"



# Continent mapping and cache file paths remain the same...

def geocode_location(location, retries=3, delay=2):
    """Geocode a location to latitude and longitude with retries."""
    if location in geo_cache:
        return geo_cache[location]

    for attempt in range(retries):
        try:
            geocoded = geolocator.geocode(location)
            if geocoded:
                geo_cache[location] = (geocoded.latitude, geocoded.longitude)
                save_geo_cache(geo_cache)  # Save updated cache
                return geocoded.latitude, geocoded.longitude
        except Exception as e:
            logger.warning(f"Retry {attempt + 1}/{retries} failed for location '{location}': {e}")
            time.sleep(delay)  # Wait before retrying

    logger.error(f"Failed to geocode location '{location}' after {retries} retries.")
    return None, None


def load_cache():
    try:
        with open('builders_cache.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"last_page": 0, "builders": []}

import json  # Ensure this is imported at the top

def save_cache(cache):
    """Save builder cache to a file."""
    with open('builders_cache.json', 'w') as f:
        json.dump(cache, f)

def save_geo_cache(geo_cache):
    """Save geocoding cache to a JSON file."""
    with open('geo_cache.json', 'w') as f:
        json.dump(geo_cache, f)

def load_geo_cache():
    """Load geocoding cache from a file."""
    try:
        with open('geo_cache.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Initialize `geo_cache`
geo_cache = load_geo_cache()


def scrape_builders():
    """Scrape builder data from the AWS Community Builders directory."""
    base_url = "https://aws.amazon.com/developer/community/community-builders/community-builders-directory/"
    cache = load_cache()
    last_page = cache.get("last_page", 0)
    builders = cache.get("builders", [])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(30000)  # Set timeout to 30 seconds

        for page_num in range(last_page + 1, 150):
            logger.info(f"Scraping page {page_num}...")
            try:
                page.goto(f"{base_url}?awsm.page-cb-cards={page_num}")
                page.wait_for_selector('.lb-xbcol.m-showcase-card.aws-card-item')

                builder_cards = page.query_selector_all('.lb-xbcol.m-showcase-card.aws-card-item')
                for card in builder_cards:
                    try:
                        name = card.query_selector('.m-headline').inner_text().strip()
                        location = card.query_selector('.m-category').inner_text().strip()
                        description = card.query_selector('.m-desc').inner_text().strip()
                        country = location.split(",")[-1].strip()

                        latitude, longitude = geocode_location(location)

                        builders.append({
                            "name": name,
                            "location": location,
                            "description": description,
                            "country": country,
                            "latitude": latitude,
                            "longitude": longitude
                        })
                    except Exception as e:
                        logger.error(f"Error extracting data from card: {e}")

                save_cache({"last_page": page_num, "builders": builders})
            except Exception as e:
                logger.error(f"Error on page {page_num}: {e}")
                break  # Stop scraping to handle errors or retry later

            time.sleep(2)

        browser.close()

    return builders

if __name__ == "__main__":
    logging.info("Starting builder scraping...")
    builders_data = scrape_builders()
    logging.info(f"Scraping complete. Found {len(builders_data)} builders.")