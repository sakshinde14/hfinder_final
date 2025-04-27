import React, { useState } from 'react';
import './App.css';
import HomePage from './HomePage';
import PreferenceForm from './PreferenceForm';
import RecommendationsPage from './RecommendationsPage'; // Create this component

function App() {
 const [currentPage, setCurrentPage] = useState('home');
 const [recommendations, setRecommendations] = useState([]);

 const handleGetStartedClick = () => {
 setCurrentPage('preferenceForm');
 };

 const handleShowRecommendations = (recommendations) => {
 setRecommendations(recommendations);
 setCurrentPage('recommendations');
 };

 return (
 <>
 {currentPage === 'home' && (
  
 <HomePage onGetStartedClick={handleGetStartedClick} />
  
 )}

 {currentPage === 'preferenceForm' && (
  
 <PreferenceForm onRecommendations={handleShowRecommendations} />
  
 )}

 {currentPage === 'recommendations' && (
  
 <RecommendationsPage recommendations={recommendations} />
  
 )}
 </>
 );
}

export default App;