from playwright.sync_api import sync_playwright
import requests
from geopy.geocoders import Nominatim
import time

headers = {
    'User-Agent': 'AwsGlobalMap/1.0 (adkins.devon@hotmail.com)'
}

# Initialize geolocator
geolocator = Nominatim(user_agent="AwsGlobalMap")

# Group countries by continent for concise mappings
continents = {
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

# Expand into a flat dictionary
continent_map = {country: continent for continent, countries in continents.items() for country in countries}

def normalize_location(location):
    """
    Normalize location and map to a continent.
    """
    for country, continent in continent_map.items():
        if country.lower() in location.lower():
            return continent
    return "Unknown"

def scrape_builders():
    """Scrape builder data across all pages."""
    base_url = "https://aws.amazon.com/developer/community/community-builders/community-builders-directory/"
    builders = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Loop through pages
        for page_num in range(1, 150):  # Pages 1 to 149
            print(f"Scraping page {page_num}...")
            page_url = f"{base_url}?cb-cards.sort-by=item.additionalFields.cbName&cb-cards.sort-order=asc&awsf.builder-category=*all&awsf.location=*all&awsf.year=*all&awsm.page-cb-cards={page_num}"
            page.goto(page_url, timeout=60000)
            page.wait_for_selector('.lb-xbcol.m-showcase-card.aws-card-item', timeout=30000)

            builder_cards = page.query_selector_all('.lb-xbcol.m-showcase-card.aws-card-item')
            for card in builder_cards:
                name = card.query_selector('.m-headline').inner_text().strip()
                location = card.query_selector('.m-category').inner_text().strip()
                description = card.query_selector('.m-desc').inner_text().strip()

                # Normalize and assign continent
                continent = normalize_location(location)

                # Fetch geolocation data
                latitude, longitude = None, None
                try:
                    geo = geolocator.geocode(location, timeout=10)
                    if geo:
                        latitude = geo.latitude
                        longitude = geo.longitude
                except Exception as e:
                    print(f"Geocoding failed for {location}: {e}")

                builders.append({
                    "name": name,
                    "location": location,
                    "description": description,
                    "continent": continent,
                    "latitude": latitude,
                    "longitude": longitude,
                })

            # Optional delay to avoid being flagged as a bot
            time.sleep(2)

        browser.close()

    return builders

# Example run
if __name__ == "__main__":
    data = scrape_builders()
    print(f"Scraped {len(data)} builders.")
