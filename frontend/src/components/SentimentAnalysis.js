import React from 'react';

const SentimentAnalysis = ({ progress = 0 }) => {
  return (
    <div>
      <p>Analyzing sentiment... {Math.round(progress)}%</p>
      <progress value={progress} max={100} />
    </div>
  );
};

export default SentimentAnalysis;