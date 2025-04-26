import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS


 # Load the hostel data from data.py
from data import data

 # Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

def get_recommendations(preferences):
 """
 Recommends hostels based on user preferences using content-based filtering.

 Args:
 preferences (dict): A dictionary containing user preferences for
                        'budget', 'location', 'room_type', 'amenities', and
                        'safety_priority'.

 Returns:
 list: A list of recommended hostels (hostel_name).
 """

  # Create a feature vector for the user's preferences
 user_features = pd.Series({
   'budget_low': 1 if preferences['budget'] == 'Low' else 0,
   'budget_medium': 1 if preferences['budget'] == 'Medium' else 0,
   'budget_high': 1 if preferences['budget'] == 'High' else 0,
   'location': preferences['location'],
   'room_type_single': 1 if preferences['room_type'] == 'Single' else 0,
   'room_type_double': 1 if preferences['room_type'] == 'Double' else 0,
   'room_type_shared': 1 if preferences['room_type'] == 'Shared' else 0,
   'amenities_wifi': 1 if 'WiFi' in preferences['amenities'] else 0,
   'amenities_ac': 1 if 'AC' in preferences['amenities'] else 0,
   'amenities_food': 1 if 'Food' in preferences['amenities'] else 0,
   'amenities_laundry': 1 if 'Laundry' in preferences['amenities'] else 0,
   'safety_priority_high': 1 if preferences['safety_priority'] == 'High' else 0,
   'safety_priority_medium': 1 if preferences['safety_priority'] == 'Medium' else 0,
   'safety_priority_low': 1 if preferences['safety_priority'] == 'Low' else 0
 })

  # Create feature vectors for all hostels
 hostel_features = df.apply(lambda row: pd.Series({
   'hostel_name': row['hostel_name'],
   'budget_low': 1 if row['rent'] <= 5000 else 0,
   'budget_medium': 1 if 5000 < row['rent'] <= 8000 else 0,
   'budget_high': 1 if row['rent'] > 8000 else 0,
   'location': row['location'],
   'room_type_single': 1 if row['room_type'] == 'Single' else 0,
   'room_type_double': 1 if row['room_type'] == 'Double' else 0,
   'room_type_shared': 1 if row['room_type'] == 'Shared' else 0,
   'amenities_wifi': 1 if 'WiFi' in row['amenities'] else 0,
   'amenities_ac': 1 if 'AC' in row['amenities'] else 0,
   'amenities_food': 1 if 'Food' in row['amenities'] else 0,
   'amenities_laundry': 1 if 'Laundry' in row['amenities'] else 0,
   'safety_priority_high': 1 if row['safety_priority'] == 'High' else 0,
   'safety_priority_medium': 1 if row['safety_priority'] == 'Medium' else 0,
   'safety_priority_low': 1 if row['safety_priority'] == 'Low' else 0
 }), axis=1)

  # Calculate cosine similarity (excluding location for now)
 user_features_for_similarity = user_features.drop('location')
 hostel_features_for_similarity = hostel_features.drop('location', axis=1)

 similarities = cosine_similarity(
  hostel_features_for_similarity.drop('hostel_name', axis=1),
  user_features_for_similarity.values.reshape(1, -1)
 ).flatten()

  # Add similarity scores to the hostel features
 hostel_features['similarity'] = similarities

  # Filter hostels based on location (exact match for now)
 location_matched_hostels = hostel_features[hostel_features['location'] == user_features['location']]

  # Get the top 3 most similar hostels
 top_recommendations = location_matched_hostels.nlargest(3, 'similarity')['hostel_name'].tolist()

 return top_recommendations

@app.route('/recommendations', methods=['POST'])
def get_recommendations_endpoint():
 """
 API endpoint to receive user preferences and return hostel recommendations.
 """
 preferences = request.get_json()
 if not preferences:
  return jsonify({'error': 'No preferences provided'}), 400

 recommendations = get_recommendations(preferences)
 return jsonify({'recommendations': recommendations}), 200

if __name__ == '__main__':
 app.run(debug=True)