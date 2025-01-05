from flask import Flask, jsonify, request
from scrape import scrape_builders  # Import scrape_builders from scrape.py
from geopy.geocoders import Nominatim
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)

@app.route('/')
def homepage():
    return send_from_directory('static', 'frontend.html')

# Enable CORS for all routes
CORS(app)

# Global variable to store builder data
builders_data = None

# Initialize geolocator
geolocator = Nominatim(user_agent="AwsGlobalMap")


def load_builders_data():
    """Load builder data into a global variable."""
    global builders_data
    if builders_data is None:  # Only load data if not already loaded
        try:
            print("Scraping builder data...")
            builders_data = scrape_builders()  # Fetch builder data from scrape.py
            print(f"Loaded {len(builders_data)} builders.")
            update_unknown_countries()  # Update country information for unknown entries
        except Exception as e:
            print(f"Error loading builders data: {e}")
            builders_data = []


def update_unknown_countries():
    """Update builders with 'Unknown' country values using reverse geocoding."""
    global builders_data
    for builder in builders_data:
        if builder["country"] == "Unknown":  # Check the 'country' field
            try:
                print(f"Processing builder: {builder['name']} - Coordinates: {builder['latitude']}, {builder['longitude']}")
                location = geolocator.reverse(f"{builder['latitude']}, {builder['longitude']}", timeout=10)
                if location and "country" in location.raw["address"]:
                    builder["country"] = location.raw["address"]["country"]
                    print(f"Updated {builder['name']} to country: {builder['country']}")
                else:
                    print(f"Country not found for {builder['name']}, leaving as 'Unknown'.")
            except Exception as e:
                print(f"Error reverse geocoding for {builder['name']}: {e}")


@app.route('/countries', methods=['GET'])
def get_countries():
    """Return a list of unique countries."""
    load_builders_data()  # Ensure data is loaded

    # Extract unique countries from the 'country' field
    countries = sorted(set(builder["country"] for builder in builders_data if builder["country"] != "Unknown"))

    return jsonify(countries)


@app.route('/builders', methods=['GET'])
def get_builders():
    """Return builder data filtered by country."""
    load_builders_data()  # Ensure data is loaded

    country = request.args.get('country', '')
    if country:
        filtered_builders = [b for b in builders_data if b["country"].lower() == country.lower()]
    else:
        filtered_builders = builders_data  # Return all builders if no country specified

    return jsonify(filtered_builders)


@app.route('/builders/geojson', methods=['GET'])
def get_builders_geojson():
    """Return builder data in GeoJSON format."""
    load_builders_data()  # Ensure data is loaded

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for builder in builders_data:
        if builder["latitude"] and builder["longitude"]:
            feature = {
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
            geojson["features"].append(feature)

    return jsonify(geojson)


@app.route('/search', methods=['GET'])
def search_builder():
    """Search for a builder by name."""
    load_builders_data()  # Ensure data is loaded

    name = request.args.get('name', '').strip().lower()
    if not name:
        return jsonify({"error": "Name parameter is required."}), 400

    # Perform a case-insensitive search for the name
    matching_builders = [
        builder for builder in builders_data
        if name in builder["name"].lower()
    ]

    if matching_builders:
        return jsonify(matching_builders)
    else:
        return jsonify({"message": "No builder found with the specified name."}), 404


if __name__ == '__main__':
    # Load builders data before starting the app
    load_builders_data()

    # Start the Flask app
    app.run(debug=False)
