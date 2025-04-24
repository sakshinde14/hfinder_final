import React from 'react';

 function PreferenceForm({ onRecommendations }) {
  const handleSubmit = async (event) => {
  event.preventDefault();

  const budget = document.getElementById('budget').value;
  const location = document.getElementById('location').value;
  const room_type = document.getElementById('roomType').value;
  const amenities = Array.from(
  document.querySelectorAll('input[type="checkbox"]:checked')
  ).map((checkbox) => checkbox.id);
  const safety_priority = document.getElementById('safetyPriority').value;

  const preferences = {
  budget,
  location,
  room_type,
  amenities,
  safety_priority,
  };

  try {
  const response = await fetch('http://127.0.0.1:5000/recommendations', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json',
  },
  body: JSON.stringify(preferences),
  });

  if (!response.ok) {
  throw new Error(`HTTP error! Status: ${response.status}`);
  }

  const data = await response.json();
  onRecommendations(data.recommendations);
  } catch (error) {
  console.error('Error fetching recommendations:', error);
  }
  };

  return (
  <>
  <h2 className="text-4xl font-bold text-center mt-12 text-pink-500">
  Enter Your Preferences
  </h2>
  <form onSubmit={handleSubmit}>
  
  <label htmlFor="budget" className="text-2xl block text-gray-700  mb-2 mt-2">
  Budget Range
  </label>
  <select
  id="budget"
  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  >
  <option>Low</option>
  <option>Medium</option>
  <option>High</option>
  </select>
  
  
  <label htmlFor="location" className="text-2xl block text-gray-700  mb-2 mt-2">
  Preferred Location / College Name
  </label>
  <input
  type="text"
  id="location"
  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  />
  
  
  <label htmlFor="roomType" className="text-2xl block text-gray-700 mb-2 mt-2">
  Room Type
  </label>
  <select
  id="roomType"
  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  >
  <option>Single</option>
  <option>Double</option>
  <option>Shared</option>
  </select>
  
  
  <label className="text-2xl block text-gray-700  mb-2 mt-2">
  Amenities Needed
  </label>
  
  <input type="checkbox" id="wifi" className="mr-2" />
  <label htmlFor="wifi" className="py-2 px-3 text-gray-700">
  WiFi
  </label>
  
  
  <input type="checkbox" id="ac" className="mr-2" />
  <label htmlFor="ac" className="py-2 px-3 text-gray-700">
  AC
  </label>
  
  
  <input type="checkbox" id="food" className="mr-2" />
  <label htmlFor="food" className="py-2 px-3 text-gray-700">
  Food
  </label>
  
  
  <input type="checkbox" id="laundry" className="mr-2" />
  <label htmlFor="laundry" className="py-2 px-3 text-gray-700">
  Laundry
  </label>
  
  
  
  <label htmlFor="safetyPriority" className="text-2xl block text-gray-700 mb-2 mt-2">
  Safety Priority
  </label>
  <select
  id="safetyPriority"
  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  >
  <option>High</option>
  <option>Medium</option>
  <option>Low</option>
  </select>
  
  <div className="text-2xl flex justify-center mt-8">
  <button
  type="submit"
  className="bg-pink-500 hover:bg-pink-700 text-white py-2 px-8 rounded-full"
  >
  Show Recommendations
  </button>
  </div>
  </form>
  </>
  );
 }

 export default PreferenceForm;