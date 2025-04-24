import React from 'react';

 function RecommendationsPage({ recommendations }) {
  console.log("Recommendations prop received:", recommendations);

  return (
    <>
      <h2>Recommended Hostels</h2>
      
        {recommendations ? (
          <ul>
            {recommendations.map((hostelName, index) => (
              <li key={index}>{hostelName}</li>
            ))}
          </ul>
        ) : (
          <p>No recommendations found.</p>
        )}
    </>   
    
  );
 }

 export default RecommendationsPage;