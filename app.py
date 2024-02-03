from flask import Flask, render_template, request, jsonify
# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

app = Flask(__name__)
arc_gis = "AAPK7d9198b324c34382b89c6e1485af7a6feZL-WzCqfZjOlsuoTNJ7kCBMlRAaoAnOCgA0I33as1UJjUfgPNOkmdKCmIvwxNrg"

@app.route('/')
def index():
    # Pass the API key to the template
    return render_template('index.html', arc_gis=arc_gis)

# @app.route('/route', methods=['POST'])
# def get_route():
#     source_address = request.form['source_address']
#     destination_address = request.form['destination_address']

#     return render_template('fake.html', arc_gis=arc_gis)

# @app.route('/route', methods=['POST'])
# def get_route():
#     source_address = request.form['source_address']
#     destination_address = request.form['destination_address']

#      # Query the Google Maps Directions API to get the route
#     params = {
#         'origin': source_address,
#         'destination': destination_address,
#         'key': google_api_key
#     }
#     response = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=params)
    
#     if response.status_code == 200:
#         route_data = response.json()
#         return jsonify(route_data)
#     else:
#         return jsonify({'error': 'Unable to retrieve route data'})



# os.getenv('GOOGLEMAPS_API_KEY')

# @app.route('/')
# def index():
#     # Pass the API key to the template
#     return render_template('index.html', api_key=google_api_key)

# @app.route('/route', methods=['POST'])
# def get_route():
#     source_address = request.form['source_address']
#     destination_address = request.form['destination_address']

#      # Query the Google Maps Directions API to get the route
#     params = {
#         'origin': source_address,
#         'destination': destination_address,
#         'key': google_api_key
#     }
#     response = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=params)
    
#     if response.status_code == 200:
#         route_data = response.json()
#         return jsonify(route_data)
#     else:
#         return jsonify({'error': 'Unable to retrieve route data'})
  
if __name__ == '__main__':
    app.run(debug=True)
