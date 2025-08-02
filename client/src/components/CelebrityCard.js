import React, { useState } from 'react';
import { Play, Pause, Star, Info } from 'lucide-react';

const CelebrityCard = ({ 
  celebrity, 
  isSelected, 
  onSelect, 
  onPreview, 
  onShowDetails,
  isPlaying = false 
}) => {
  const [imageError, setImageError] = useState(false);
  const [isHovered, setIsHovered] = useState(false);

  const getCategoryGradient = (category) => {
    const gradients = {
      bollywood: 'bollywood-gradient',
      tollywood: 'tollywood-gradient', 
      kollywood: 'kollywood-gradient',
      regional: 'regional-gradient'
    };
    return gradients[category] || 'bg-gradient-to-r from-gray-400 to-gray-600';
  };

  const getCategoryColor = (category) => {
    const colors = {
      bollywood: 'text-warning-600',
      tollywood: 'text-secondary-600',
      kollywood: 'text-accent-600', 
      regional: 'text-success-600'
    };
    return colors[category] || 'text-gray-600';
  };

  const handleImageError = () => {
    setImageError(true);
  };

  const handlePreviewClick = (e) => {
    e.stopPropagation();
    onPreview(celebrity.id);
  };

  const handleDetailsClick = (e) => {
    e.stopPropagation();
    onShowDetails(celebrity);
  };

  return (
    <div
      className={`celebrity-card ${isSelected ? 'selected' : ''} group`}
      onClick={() => onSelect(celebrity)}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      {/* Celebrity Image */}
      <div className="relative overflow-hidden">
        {!imageError ? (
        <img
  src={
    celebrity.image && celebrity.image.startsWith('http')
      ? celebrity.image
      : `http://localhost:5000${celebrity.image || `/images/celebrities/${celebrity.id}.jpg`}`
  }
  alt={celebrity.name}
  className="w-full h-48 sm:h-56 object-cover transition-transform duration-300 group-hover:scale-110"
  onError={handleImageError}
/>
        ) : (
          <div className="w-full h-48 sm:h-56 bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-800 flex items-center justify-center">
            <div className="text-center">
              <div className="w-16 h-16 mx-auto mb-2 bg-gray-400 dark:bg-gray-600 rounded-full flex items-center justify-center">
                <span className="text-2xl font-bold text-white">
                  {celebrity.name.charAt(0)}
                </span>
              </div>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                {celebrity.name}
              </p>
            </div>
          </div>
        )}
        
        {/* Category Badge */}
        <div className={`absolute top-3 left-3 px-2 py-1 rounded-full text-xs font-medium text-white ${getCategoryGradient(celebrity.category)}`}>
          {celebrity.category.charAt(0).toUpperCase() + celebrity.category.slice(1)}
        </div>

        {/* Popularity Stars */}
        <div className="absolute top-3 right-3 flex items-center bg-black bg-opacity-50 rounded-full px-2 py-1">
          <Star className="w-3 h-3 text-yellow-400 fill-current" />
          <span className="text-xs text-white ml-1">{celebrity.popularity}</span>
        </div>

        {/* Hover Overlay */}
        {isHovered && (
          <div className="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center transition-opacity duration-300">
            <div className="flex gap-2">
              <button
                onClick={handlePreviewClick}
                className="bg-white bg-opacity-90 hover:bg-opacity-100 text-gray-800 p-2 rounded-full transition-all duration-200 transform hover:scale-110"
                title="Preview Voice"
              >
                {isPlaying ? (
                  <Pause className="w-4 h-4" />
                ) : (
                  <Play className="w-4 h-4" />
                )}
              </button>
              <button
                onClick={handleDetailsClick}
                className="bg-white bg-opacity-90 hover:bg-opacity-100 text-gray-800 p-2 rounded-full transition-all duration-200 transform hover:scale-110"
                title="View Details"
              >
                <Info className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Celebrity Info */}
      <div className="p-4">
        <h3 className="font-semibold text-lg text-gray-900 dark:text-white mb-1 truncate">
          {celebrity.name}
        </h3>
        
        <p className={`text-sm font-medium mb-2 ${getCategoryColor(celebrity.category)}`}>
          {celebrity.category.charAt(0).toUpperCase() + celebrity.category.slice(1)} Star
        </p>

        <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-2 mb-3">
          {celebrity.bio}
        </p>

        {/* Voice Characteristics */}
        <div className="flex flex-wrap gap-1 mb-3">
          {celebrity.voice_characteristics.slice(0, 3).map((characteristic, index) => (
            <span
              key={index}
              className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-xs rounded-full text-gray-700 dark:text-gray-300"
            >
              {characteristic}
            </span>
          ))}
        </div>

        {/* Languages */}
        <div className="flex items-center justify-between">
          <div className="flex flex-wrap gap-1">
            {celebrity.languages.slice(0, 2).map((language, index) => (
              <span
                key={index}
                className="text-xs text-gray-500 dark:text-gray-400 capitalize"
              >
                {language}{index < celebrity.languages.slice(0, 2).length - 1 ? ', ' : ''}
              </span>
            ))}
            {celebrity.languages.length > 2 && (
              <span className="text-xs text-gray-500 dark:text-gray-400">
                +{celebrity.languages.length - 2} more
              </span>
            )}
          </div>
          
          <span className="text-xs text-gray-500 dark:text-gray-400">
            Since {celebrity.debut_year}
          </span>
        </div>
      </div>

      {/* Selection Indicator */}
      {isSelected && (
        <div className="absolute inset-0 border-4 border-primary-500 rounded-2xl pointer-events-none">
          <div className="absolute -top-2 -right-2 bg-primary-500 text-white rounded-full p-1">
            <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
            </svg>
          </div>
        </div>
      )}
    </div>
  );
};

export default CelebrityCard;



