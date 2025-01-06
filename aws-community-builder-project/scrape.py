from playwright.sync_api import sync_playwright
import requests
from geopy.geocoders import Nominatim
import json
import time
import logging

# Initialize headers and geolocator
headers = {'User-Agent': 'AwsGlobalMap/1.0'}
geolocator = Nominatim(user_agent="AwsGlobalMap")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# File paths for caching
CACHE_FILE = 'builders_cache.json'
GEO_CACHE_FILE = 'geo_cache.json'

# Continent mapping
continent_map = {
    "Africa": [...],
    "Asia": [...],
    "Europe": [...],
    "North America": [...],
    "South America": [...],
    "Oceania": [...]
}

def save_cache(data):
    """Save scraping progress to a cache file."""
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)

def load_cache():
    """Load scraping progress from the cache file."""
    try:
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"last_page": 0, "builders": []}

def save_geo_cache(cache):
    """Save geocoding results to a cache file."""
    with open(GEO_CACHE_FILE, 'w') as f:
        json.dump(cache, f)

def load_geo_cache():
    """Load geocoding results from the cache file."""
    try:
        with open(GEO_CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

geo_cache = load_geo_cache()

def geocode_location(location):
    """Geocode a location and cache the results."""
    if location in geo_cache:
        return geo_cache[location]

    try:
        geo = geolocator.geocode(location, timeout=10)
        if geo:
            geo_cache[location] = (geo.latitude, geo.longitude)
            save_geo_cache(geo_cache)
            return geo.latitude, geo.longitude
    except Exception as e:
        logger.error(f"Geocoding failed for {location}: {e}")
    return None, None

def scrape_builders():
    """Scrape builder data from the AWS Community Builders directory."""
    base_url = "https://aws.amazon.com/developer/community/community-builders/community-builders-directory/"
    cache = load_cache()
    last_page = cache.get("last_page", 0)
    builders = cache.get("builders", [])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(600000)  # Set timeout to 10 minutes

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
    logger.info("Starting scraping...")
    builder_data = scrape_builders()
    logger.info("Scraping complete. Saving data to 'builders.json'.")

    # Save the final data to a JSON file
    with open('builders.json', 'w') as f:
        json.dump(builder_data, f, indent=4)
