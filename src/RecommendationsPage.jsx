import React from 'react';
 

function RecommendationsPage({ recommendations }) {
 console.log("Recommendations prop received:", recommendations);


 return (
 <>
 <h2 className="text-2xl font-bold text-center mt-12 text-pink-500 mb-4">
 Recommended Hostels
 </h2>
 
 {recommendations && recommendations.length > 0 ? (
 <ul className="list-none space-y-4">
 {recommendations.map((hostel, index) => (
 <li key={index} className="bg-white shadow-md rounded-md p-4">
 <h3 className="text-lg font-semibold text-gray-800">{hostel.hostel_name}</h3>
 <p className="text-gray-600">Location: {hostel.location}</p>
 <p className="text-gray-600">Rent: ₹{hostel.rent}</p>
 <p className="text-gray-600">Room Type: {hostel.room_type}</p>
 <p className="text-gray-600">Rating: {hostel.rating}</p>
 <p className="text-gray-600">
 Amenities: {hostel.amenities.join(', ')}
 </p>
  <p className="text-gray-600">
 Safety Priority: {hostel.safety_priority}
 </p>
 </li>
 ))}
 </ul>
 ) : (
 <div className="text-center mt-8 p-4 bg-gray-100 rounded-md shadow-inner">
 <p className="text-gray-700 font-semibold mb-2">Sorry, no hostels matched your preferences.</p>
 <p className="text-sm text-gray-600">Please try adjusting your budget, location, or other criteria.</p>
 </div>
 )}
 </>
 );
}


export default RecommendationsPage;
