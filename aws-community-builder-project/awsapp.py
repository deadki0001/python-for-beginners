from flask import Flask, send_from_directory, jsonify, request
from scrape import *
from geopy.geocoders import Nominatim
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Global variable to store builder data
builders_data = None

# Initialize geolocator
geolocator = Nominatim(user_agent="AwsGlobalMap")

def load_builders_data():
    """Load builder data into a global variable."""
    global builders_data
    if builders_data is None:
        try:
            print("Scraping builder data...")
            builders_data = scrape_builders()
            print(f"Loaded {len(builders_data)} builders.")
            update_unknown_countries()
        except Exception as e:
            print(f"Error loading builders data: {e}")
            builders_data = []

def update_unknown_countries():
    """Update builders with 'Unknown' country values using reverse geocoding."""
    global builders_data
    for builder in builders_data:
        if builder["country"] == "Unknown" and builder["latitude"] and builder["longitude"]:
            try:
                location = geolocator.reverse(f"{builder['latitude']}, {builder['longitude']}", timeout=10)
                if location and "country" in location.raw["address"]:
                    builder["country"] = location.raw["address"]["country"]
            except Exception as e:
                print(f"Error reverse geocoding for {builder['name']}: {e}")

@app.route('/')
def homepage():
    return send_from_directory('frontend.html')

@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Return a list of unique countries and builder data grouped by country."""
    load_builders_data()
    country_data = {}

    for builder in builders_data:
        country = builder.get("country", "Unknown")
        if country not in country_data:
            country_data[country] = []
        country_data[country].append({
            "name": builder["name"],
            "description": builder["description"],
            "latitude": builder["latitude"],
            "longitude": builder["longitude"],
        })

    return jsonify(country_data), 200

@app.route('/api/builders', methods=['GET'])
def get_builders():
    """Return builder data filtered by country."""
    load_builders_data()
    country = request.args.get('country', '')
    filtered_builders = [b for b in builders_data if b["country"].lower() == country.lower()] if country else builders_data
    return jsonify(filtered_builders)

@app.route('/api/search', methods=['GET'])
def search_builder():
    """Search for a builder by name."""
    load_builders_data()
    name = request.args.get('name', '').strip().lower()
    if not name:
        return jsonify({"error": "Name parameter is required."}), 400
    matching_builders = [builder for builder in builders_data if name in builder["name"].lower()]
    return jsonify(matching_builders) if matching_builders else jsonify({"message": "No builder found with the specified name."}), 404

@app.route('/api/builders/geojson', methods=['GET'])
def get_builders_geojson():
    """Return builder data in GeoJSON format."""
    load_builders_data()
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": builder["name"],
                    "country": builder["country"],
                    "location": builder["location"],
                    "description": builder["description"]
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [builder["longitude"], builder["latitude"]]
                }
            }
            for builder in builders_data if builder["latitude"] and builder["longitude"]
        ]
    }
    return jsonify(geojson)

if __name__ == '__main__':
    load_builders_data()
    app.run(debug=False, host='0.0.0.0', port=5000)