import React from 'react';

function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-center text-pink-600 mb-6">
        About Smart Hostel Finder
      </h2>
      <div className="bg-white rounded-lg shadow-md p-6">
        <p className="text-gray-700 leading-relaxed mb-4">
          Welcome to Smart Hostel Finder, a web application designed to help
          college girls find safe and comfortable hostel accommodations. We
          understand that choosing the right hostel is a crucial decision, and
          we aim to simplify this process by providing personalized
          recommendations.
        </p>
        <p className="text-gray-700 leading-relaxed mb-4">
          Our platform uses a machine learning model to analyze your
          preferences, including budget, location, room type, desired amenities,
          and safety priorities. By considering these factors, we generate a
          curated list of hostels that align with your individual needs and
          preferences.
        </p>
        <p className="text-gray-700 leading-relaxed mb-4">
          Key Features:
        </p>
        <ul className="list-disc list-inside text-gray-700 mb-6">
          <li>
            <span className="font-semibold">Personalized Recommendations:</span> Get hostel suggestions tailored to your specific
            requirements.
          </li>
          <li>
            <span className="font-semibold">Comprehensive Information:</span> View detailed information about each hostel,
            including location, rent, amenities, and safety ratings.
          </li>
          <li>
            <span className="font-semibold">User-Friendly Interface:</span> Easily navigate through the platform and find the
            information you need.
          </li>
        </ul>
        <p className="text-gray-700 leading-relaxed mb-4">
          Our Mission:
        </p>
        <p className="text-gray-700 leading-relaxed">
          We are committed to empowering college girls to make informed
          decisions about their accommodation. Our goal is to provide a
          reliable and efficient tool that promotes safety, comfort, and
          convenience.
        </p>
      </div>
    </div>
  );
}

export default AboutPage;
