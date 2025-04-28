import React, { useState } from 'react';

function PreferenceForm({ onRecommendations }) {
  const [budget, setBudget] = useState('');
  const [college, setCollege] = useState('');
  const [roomType, setRoomType] = useState('');
  const [amenities, setAmenities] = useState([]);
  const [safetyPriority, setSafetyPriority] = useState('');
  const [maxRent, setMaxRent] = useState(''); // Added state for maxRent

  const colleges = [
    'Fergusson College',
    'Symbiosis College of Arts and Commerce',
    'College of Engineering (COEP Technological University)',
    'MIT World Peace University (MIT-WPU)',
    'Brihan Maharashtra College of Commerce (BMCC)',
    'Sir Parashurambhau College (SP College)',
    'Nowrosjee Wadia College',
    'Ness Wadia College of Commerce',
    'Pune Institute of Computer Technology (PICT)',
    'Vishwakarma Institute of Technology (VIT)',
    'Cummins College of Engineering for Women',
    'Dr. D. Y. Patil Institute of Technology, Pimpri',
    'Modern College of Arts, Science and Commerce, Shivajinagar',
    'Indira College of Commerce and Science',
    'Balaji Institute of Modern Management (BIMM)',
    'Bharati Vidyapeeth Deemed University',
    'All India Shri Shivaji Memorial Society’s College of Engineering (AISSMS COE)',
    'Sinhgad College of Engineering',
    'MIT School of Management',
    'Symbiosis Institute of Business Management (SIBM)',
    'JSPM’s Rajarshi Shahu College of Engineering',
    'International Institute of Information Technology (IIIT)',
    'Army Institute of Technology (AIT)',
    'Vishwakarma Institute of Information Technology (VIIT)',
    'MIT Academy of Engineering (MITAOE)',
    'MIT Art, Design and Technology University',
    'Dr. D. Y. Patil College of Engineering, Akurdi',
    'Trinity College of Engineering and Research',
    'Zeal College of Engineering and Research',
    'Pune Vidyarthi Griha’s College of Engineering and Technology (PVGCOET)',
    'Padmashree Dr. D. Y. Patil Institute of Management Studies',
    'Symbiosis Institute of Technology (SIT)',
    'Bharati Vidyapeeth College of Engineering',
    'Indira School of Business Studies (ISBS)',
    'MIT College of Management',
    'MIT Vishwashanti Gurukul University',
    'Flame University',
    'International School of Business & Media (ISBM)',
    'DY Patil Dental College and Hospital'
  ]; // Added colleges

  const allAmenities = [  // Expanded amenities
    'WiFi',
    'AC',
    'Food',
    'Laundry',
    'TV',
    'Gym',
    'Security',
    'Parking',
    'Attached Bathroom',
    'Hot Water'
  ];

  const handleAmenityChange = (event) => {
    const amenity = event.target.id;
    const isChecked = event.target.checked;

    if (isChecked) {
      setAmenities([...amenities, amenity]);
    } else {
      setAmenities(amenities.filter((a) => a !== amenity));
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const preferences = {
      budget: maxRent ? `Upto ${maxRent}` : budget, // Use maxRent or original budget
      location,
      room_type: roomType,
      amenities,
      safety_priority: safetyPriority,
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
        {/* Maximum Rent Input */}
        <label htmlFor="maxRent" className="text-2xl block text-gray-700 mb-2 mt-2">
          Maximum Rent
        </label>
        <input
          type="number"
          id="maxRent"
          value={maxRent}
          onChange={(e) => setMaxRent(e.target.value)}
          placeholder="Enter maximum rent"
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />

        {/* College Dropdown */}
        <label htmlFor="college" className="text-2xl block text-gray-700 mb-2 mt-2">
          College Name
        </label>
        <select
          id="college"
          value={college}
          onChange={(e) => setCollege(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">Select a College</option>
          {colleges.map((col) => (
            <option key={col} value={col}>
              {col}
            </option>
          ))}
        </select>

        {/* Room Type Dropdown */}
        <label htmlFor="roomType" className="text-2xl block text-gray-700 mb-2 mt-2">
          Room Type
        </label>
        <select
          id="roomType"
          value={roomType}
          onChange={(e) => setRoomType(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">Select Room Type</option>
          <option value="Single">Single</option>
          <option value="Double">Double</option>
          <option value="Shared">Shared</option>
        </select>

        {/* Amenities Checkboxes */}
        <label className="text-2xl block text-gray-700 mb-2 mt-2">
          Amenities Needed
        </label>
        <div className="flex flex-wrap">
          {allAmenities.map((amenity) => (
            <div key={amenity} className="mr-4 mb-2">
              <input
                type="checkbox"
                id={amenity}
                checked={amenities.includes(amenity)}
                onChange={handleAmenityChange}
                className="mr-2"
              />
              <label htmlFor={amenity} className="py-2 px-3 text-gray-700">
                {amenity}
              </label>
            </div>
          ))}
        </div>

        {/* Safety Priority Dropdown */}
        <label htmlFor="safetyPriority" className="text-2xl block text-gray-700 mb-2 mt-2">
          Safety Priority
        </label>
        <select
          id="safetyPriority"
          value={safetyPriority}
          onChange={(e) => setSafetyPriority(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        >
          <option value="">Select Safety Priority</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
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
