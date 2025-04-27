import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS
import pymongo  # Import PyMongo

app = Flask(__name__)
CORS(app)

# 1. MongoDB Connection URI
#    - Replace with your actual MongoDB connection string.
#    - This string tells PyMongo how to connect to your MongoDB instance.
#    - It typically includes the username, password (if any), host, port, and database name.
#    - Example:  "mongodb://username:password@host:port/database_name"
#    - If your MongoDB is running on the same machine as your Flask app with the default settings, it might look like this:
#      "mongodb://localhost:27017/hostel_recommender"  (where "hostel_recommender" is your database name)
mongo_uri = "mongodb+srv://sakshi:gaurinde@cluster0.vpbqv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# 2. Connect to MongoDB
#    - Use pymongo.MongoClient to establish a connection.
try:
    client = pymongo.MongoClient(mongo_uri)
    db = client.get_database("hostel_recommender")  # Get the database object
    print("Connected to MongoDB!")  # Optional: Print a success message
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
    #  IMPORTANT:  If you can't connect to the database, the rest of your app might not work.  You might want to:
    #  -  Raise an exception here to prevent the app from starting.
    #  -  Return an error response to the client if this happens during a request.


# 3. Define Collections (instead of tables)
#    - In MongoDB, you work with "collections" instead of tables.
#    - You don't define a schema in the same way as with relational databases, but it's good practice to have a consistent structure for your documents.
#    -  We'll define the collections we'll use.  You don't *have* to create them explicitly; MongoDB will create them when you first insert data, but it's good to know what you'll be using.
    hostels_collection = db.hostels  #  Example:  "hostels" collection
    users_collection = db.users # "users" collection
    # Add more collections as needed (e.g., for preferences, ratings).



def get_recommendations(preferences):
    """
    Recommends hostels based on user preferences.

    Args:
        preferences (dict): User preferences.

    Returns:
        list: Recommended hostels (documents from MongoDB).
    """
    #  IMPORTANT:  You'll need to adapt this function to work with MongoDB.
    #  -  Instead of using Pandas and cosine_similarity, you'll use PyMongo to query MongoDB.
    #  -  The logic will be similar, but the syntax will be different.

    #  Example (Conceptual):
    #  1.  Find hostels that match the user's location.
    #      location_match = hostels_collection.find({'location': preferences['location']})
    #
    #  2.  Calculate a score for each hostel based on the preferences.
    #      (You'll need to define how you want to score hostels based on budget, room type, amenities, etc.)
    #
    #  3.  Sort the hostels by score.
    #
    #  4.  Return the top 3 hostels.
    #  recommended_hostels = sorted(hostels, key=lambda x: x['score'], reverse=True)[:3]
    #  return list(recommended_hostels) # Convert the result to a list
    return [] #Added to remove error



@app.route('/recommendations', methods=['POST'])
def get_recommendations_endpoint():
    """
    API endpoint to receive user preferences and return hostel recommendations.
    """
    preferences = request.get_json()
    if not preferences:
        return jsonify({'error': 'No preferences provided'}), 400

    recommendations = get_recommendations(preferences)  # Call your MongoDB-adapted function

    # Convert the MongoDB documents to a JSON-serializable format (if needed)
    #  (PyMongo usually returns data in a format that Flask can handle, but you might need to do some conversion in some cases.)
    return jsonify({'recommendations': recommendations}), 200



@app.route('/test', methods=['GET'])
def test_mongodb_connection():
    """
    Test route to check the MongoDB connection.
    """
    try:
        #  Perform a simple operation to check if the connection is working.
        client.admin.command('ping', 1)  #  The "ping" command is a simple way to test the connection
        return jsonify({'status': 'MongoDB connection successful!'}), 200
    except Exception as e:
        return jsonify({'status': 'MongoDB connection failed!', 'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
