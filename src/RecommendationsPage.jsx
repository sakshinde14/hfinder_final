import React from 'react';

function RecommendationsPage({ recommendations }) {
  console.log("Recommendations prop received:", recommendations);

  return (
    <div className="bg-blue-100 container mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-center text-pink-600 mb-8">
        Recommended Hostels
      </h2>
      {recommendations && recommendations.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recommendations.map((hostel, index) => (
            <div
              key={index}
              className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-300"
            >
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                {hostel.hostel_name}
              </h3>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Address:</span> {hostel.address}
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Distance from College:</span> {hostel.distance_to_college}
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Rent:</span> ₹{hostel.rent}
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Room Type:</span> {hostel.room_type}
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Rating:</span> {hostel.rating} ⭐
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Amenities:</span>{' '}
                {hostel.amenities.join(', ')}
              </p>
              <p className="text-gray-600">
                <span className="font-medium">Safety Priority:</span>{' '}
                <span
                  className={
                    hostel.safety_priority === 'High'
                      ? 'text-green-500'
                      : hostel.safety_priority === 'Medium'
                      ? 'text-yellow-500'
                      : 'text-red-500'
                      ? 'text-red-500'
                      : 'text-gray-500'
                  }
                >
                  {hostel.safety_priority}
                </span>
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Hostel Type:</span> {hostel.hostel_type}
              </p>
              <p className="text-gray-600 mb-1">
                <span className="font-medium">Contact Number:</span> {hostel.contact_number}
              </p>
            </div>
          ))}
        </div>
      ) : (
        <div className="text-center mt-8 p-6 bg-gray-100 rounded-lg shadow-inner">
          <p className="text-gray-700 font-semibold mb-2">
            Sorry, no hostels matched your preferences.
          </p>
          <p className="text-gray-600 text-sm">
            Please try adjusting your budget, location, or other criteria.
          </p>
        </div>
      )}
    </div>
  );
}

export default RecommendationsPage;
