import React from 'react';

function HomePage({ onGetStartedClick }) {
  return (
    <>
      
        <h1 className="text-4xl font-bold text-center text-pink-500">
          Find Your Perfect Hostel Match
        </h1>
        <p className="text-lg text-center mt-4 text-gray-700">
          Personalized recommendations for college girls based on your needs
        </p>
        <div className="flex justify-center mt-8">
          <button
            className="bg-pink-500 hover:bg-pink-700 text-white font-bold py-2 px-8 rounded-full"
            onClick={onGetStartedClick}
          >
            Get Started
          </button>
        </div>
      
        </>
  );
}

export default HomePage;