import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load hostel data
from data import data

# Prepare DataFrame
df = pd.DataFrame(data)

# Fix distance column to numeric
df['distance_to_college'] = df['distance_to_college'].str.replace(' km', '').astype(float)

app = Flask(__name__)
CORS(app)

def prepare_hostel_features(hostel):
    features = []
    features.append(hostel['rent'])
    
    unique_colleges = df['college'].unique()
    for col in unique_colleges:
        features.append(1 if hostel['college'] == col else 0)
    
    room_types = ['Single', 'Double', 'Shared']
    for rt in room_types:
        features.append(1 if hostel['room_type'] == rt else 0)
    
    amenities_list = ['WiFi', 'AC', 'Food', 'Laundry', 'TV', 'Gym', 'Security', 'Parking', 'Attached Bathroom', 'Hot Water']
    for amenity in amenities_list:
        features.append(1 if amenity in hostel['amenities'] else 0)
    
    safety_priority_map = {'High': 3, 'Medium': 2, 'Low': 1}
    features.append(safety_priority_map.get(hostel['safety_priority'], 0))
    
    features.append(hostel['distance_to_college'])
    return features

def prepare_user_preferences(preferences):
    features = []
    
    max_rent = 0
    if "Upto" in preferences['budget']:
        max_rent = int(preferences['budget'].replace("Upto ", ""))
    elif preferences['budget'] == 'Low':
        max_rent = 5000
    elif preferences['budget'] == 'Medium':
        max_rent = 8000
    elif preferences['budget'] == 'High':
        max_rent = 100000
    features.append(max_rent)

    unique_colleges = df['college'].unique()
    for col in unique_colleges:
        features.append(1 if preferences['college'] == col else 0)
    
    room_types = ['Single', 'Double', 'Shared']
    for rt in room_types:
        features.append(1 if preferences['room_type'] == rt else 0)
    
    amenities_list = ['WiFi', 'AC', 'Food', 'Laundry', 'TV', 'Gym', 'Security', 'Parking', 'Attached Bathroom', 'Hot Water']
    for amenity in amenities_list:
        features.append(1 if amenity in preferences['amenities'] else 0)
    
    safety_priority_map = {'High': 3, 'Medium': 2, 'Low': 1}
    features.append(safety_priority_map.get(preferences['safety_priority'], 0))

    features.append(0)  # Distance not needed for user
    return features

def knn_hostels(user_preferences, hostels_df, k=5):
    try:
        hostel_features = [prepare_hostel_features(hostel) for hostel in hostels_df.to_dict(orient='records')]
        nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(hostel_features)
        distances, indices = nbrs.kneighbors([user_preferences])

        nearest_hostels = hostels_df.iloc[indices[0]].copy()
        nearest_hostels['distance'] = distances[0]
        return nearest_hostels.sort_values(by='distance')
    except Exception as e:
        print(f"Error in knn_hostels: {e}")
        return pd.DataFrame()

def filter_hostels(nearest_hostels, preferences):
    max_rent = 0
    if "Upto" in preferences['budget']:
        max_rent = int(preferences['budget'].replace("Upto ", ""))
    elif preferences['budget'] == 'Low':
        max_rent = 5000
    elif preferences['budget'] == 'Medium':
        max_rent = 8000
    elif preferences['budget'] == 'High':
        max_rent = 100000

    filtered = nearest_hostels[nearest_hostels['rent'] <= max_rent]
    filtered = filtered[filtered['room_type'] == preferences['room_type']]

     # Step 2: Amenities filter
    def has_required_amenities(hostel_amenities, preferred_amenities):
        return all(amenity in hostel_amenities for amenity in preferred_amenities)

    if preferences['amenities']:  # if user selected any amenities
        filtered = filtered[filtered['amenities'].apply(lambda x: has_required_amenities(x, preferences['amenities']))]

    # Step 3: Room type filter
    filtered = filtered[filtered['room_type'] == preferences['room_type']]

    # Step 4: Safety priority filter
    filtered = filtered[filtered['safety_priority'] == preferences['safety_priority']]

    return filtered

@app.route('/recommendations', methods=['POST'])
def get_recommendations_endpoint():
    preferences = request.get_json()
    if not preferences:
        return jsonify({'error': 'No preferences provided'}), 400

    try:
        # Step 1: Filter by college/location
        college_hostels_df = df[df['college'] == preferences['college']]

        if college_hostels_df.empty:
            return jsonify({'recommendations': []}), 200

        # Step 2: Adjust K (neighbors)
        k_value = min(10, len(college_hostels_df))  # if less than 10 hostels, k = available hostels

        user_pref_vector = prepare_user_preferences(preferences)
        nearest_hostels_df = knn_hostels(user_pref_vector, college_hostels_df, k=k_value)
        filtered_hostels_df = filter_hostels(nearest_hostels_df, preferences)

        if filtered_hostels_df.empty:
            return jsonify({'recommendations': []}), 200

        recommendations = filtered_hostels_df.to_dict(orient='records')
        return jsonify({'recommendations': recommendations}), 200
    except Exception as e:
        print(f"Error in get_recommendations_endpoint: {e}")
        return jsonify({'error': f'Error processing request: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
