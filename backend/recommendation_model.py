import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from data import data

df = pd.DataFrame(data)

app = Flask(__name__)
CORS(app)

def get_recommendations(preferences):
    try:
        preferred_college = preferences['college']
        college_matched_hostels = df[df['college'] == preferred_college].copy()

        if college_matched_hostels.empty:
            return []

        max_rent = 0
        if "Upto" in preferences['budget']:
            max_rent = int(preferences['budget'].replace("Upto ", ""))
        elif preferences['budget'] == 'Low':
            max_rent = 5000
        elif preferences['budget'] == 'Medium':
            max_rent = 8000
        elif preferences['budget'] == 'High':
            max_rent = 100000
        budget_filtered_hostels = college_matched_hostels[college_matched_hostels['rent'] <= max_rent]

        if budget_filtered_hostels.empty:
            return []

        room_type_filtered_hostels = budget_filtered_hostels[budget_filtered_hostels['room_type'] == preferences['room_type']]
        if room_type_filtered_hostels.empty:
            return []

        def has_all_amenities(hostel_amenities, preferred_amenities):
            return all(amenity in hostel_amenities for amenity in preferred_amenities)

        room_type_filtered_hostels['has_all_amenities'] = room_type_filtered_hostels['amenities'].apply(
            lambda x: has_all_amenities(x, preferences['amenities']))
        amenities_filtered_hostels = room_type_filtered_hostels[room_type_filtered_hostels['has_all_amenities'] == True]
        amenities_filtered_hostels = amenities_filtered_hostels.drop(columns=['has_all_amenities'])
        
        if amenities_filtered_hostels.empty:
            return []

        safety_filtered_hostels = amenities_filtered_hostels[amenities_filtered_hostels['safety_priority'] == preferences['safety_priority']]

        if safety_filtered_hostels.empty:
            return []

        return safety_filtered_hostels.to_dict(orient='records')

    except Exception as e:
        print(f"Error in get_recommendations: {e}")
        return []

@app.route('/recommendations', methods=['POST'])
def get_recommendations_endpoint():
    preferences = request.get_json()
    if not preferences:
        return jsonify({'error': 'No preferences provided'}), 400

    recommendations = get_recommendations(preferences)
    return jsonify({'recommendations': recommendations}), 200

if __name__ == '__main__':
    app.run(debug=True)
