import pymongo
from data import data  # Import the hostel data from data.py

# MongoDB connection URI (replace with your actual URI)
mongo_uri = "mongodb+srv://sakshi:gaurinde@cluster0.vpbqv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client = pymongo.MongoClient(mongo_uri)
    db = client.get_database("hostel_recommender")
    print("Connected to MongoDB!")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit()  # Exit if the database connection fails

hostels_collection = db.hostels
users_collection = db.users


def insert_hostel_data():
    """Inserts hostel data into the 'hostels' collection, using data from data.py."""
    # Hostel data is now imported from data.py
    hostel_data = data

    #  Validate the data before inserting
    for hostel in hostel_data:
        if not all(
            key in hostel
            for key in [
                "hostel_name",
                "location",
                "address",
                "contact_number",
                "distance_to_college",
                "hostel_type",
                "rent",
                "room_type",
                "rating",
                "amenities",
                "safety_priority",
            ]
        ):
            print(f"Skipping invalid hostel data: {hostel}")  #  Print a message and skip
            continue  # Skip to the next hostel in the list

        # Convert contact_number, rent, and rating to numbers if they are strings
        try:
            hostel["contact_number"] = int(hostel["contact_number"])
        except ValueError:
            print(
                f"Invalid contact_number format: {hostel['contact_number']}.  Skipping hostel: {hostel['hostel_name']}"
            )
            continue  # Skip to the next hostel
        try:
            hostel["rent"] = int(hostel["rent"])
        except ValueError:
            print(
                f"Invalid rent format: {hostel['rent']}. Skipping hostel: {hostel['hostel_name']}"
            )
            continue  # Skip to the next hostel
        try:
            hostel["rating"] = float(hostel["rating"])
        except ValueError:
            print(
                f"Invalid rating format: {hostel['rating']}. Skipping hostel: {hostel['hostel_name']}"
            )
            continue  # Skip to the next hostel

        if not isinstance(hostel["amenities"], list):
            print(
                f"Invalid amenities format: {hostel['amenities']}. Skipping hostel: {hostel['hostel_name']}"
            )
            continue  # Skip to the next hostel

    try:
        hostels_collection.insert_many(hostel_data)
        print("Hostel data inserted successfully.")
    except Exception as e:
        print(f"Error inserting hostel data: {e}")



def insert_user_data():
    """Inserts user data into the 'users' collection."""
    # User data (replace with your actual data)
    user_data = [
        {
            "name": "Sakshi",
            "email": "sakshi@example.com",
            "preferences": {
                "budget": "Medium",
                "location": "Yerwada",
                "room_type": "Double",
                "amenities": ["WiFi", "Food"],
                "safety_priority": "High",
            },
            "rated_hostels": {},
        },
        {
            "name": "Shruti",
            "email": "shruti@example.com",
            "preferences": {
                "budget": "High",
                "location": "Shivajinagar",
                "room_type": "Single",
                "amenities": ["WiFi", "AC", "Laundry"],
                "safety_priority": "High",
            },
            "rated_hostels": {},
        },
    ]

    try:
        users_collection.insert_many(user_data)
        print("User data inserted successfully.")
    except Exception as e:
        print(f"Error inserting user data: {e}")



if __name__ == "__main__":
    insert_hostel_data()
    insert_user_data()
    client.close()  # Close the connection when done.
