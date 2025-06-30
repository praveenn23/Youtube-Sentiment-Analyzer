import React, { useState } from 'react';
import ResultsDisplay from './components/ResultsDisplay';
import './App.css';

function App() {
  const DEFAULT_API_KEY = 'AIzaSyAdy0uk4cYfx8nFMmgOEOk0H01MKfNIU28';

  const [formData, setFormData] = useState({
    videoUrl: '',
    apiKey: DEFAULT_API_KEY,
    maxComments: 500
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [results, setResults] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults(null);

    try {
      const response = await fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          video_url: formData.videoUrl,
          api_key: formData.apiKey,
          max_comments: parseInt(formData.maxComments)
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to analyze video');
      }

      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Hero Section */}
      <div className="hero-section">
        <div className="hero-content">
          <div className="hero-title">YouTube Comments Sentiment Analyzer</div>
          <div className="hero-desc">
            Analyze the sentiment of YouTube video comments.
          </div>
          <form className="hero-form-row" onSubmit={handleSubmit}>
            <input
              type="text"
              name="videoUrl"
              placeholder="Paste YouTube video URL"
              value={formData.videoUrl}
              onChange={handleInputChange}
              required
            />
            <button type="submit" >
              {loading ? 'Analyzing...' : 'Analyze'}
            </button>
          </form>
          {error && <p className="error-text">{error}</p>}
        </div>
      </div>

      {/* Features Section */}
      <div className="features-section">
        <div className="features-title">Key Features</div>
        <div className="features-row">
          <div className="feature-card">
            <span className="feature-icon">🧠</span>
            <h3>Sentiment Analysis</h3>
            <p>Understand the overall sentiment of comments on your video with advanced analysis techniques.</p>
          </div>
          <div className="feature-card">
            <span className="feature-icon">👥</span>
            <h3>Audience Insights</h3>
            <p>Gain insights into audience reactions, identify key themes, and track trends over time.</p>
          </div>
          <div className="feature-card">
            <span className="feature-icon">📈</span>
            <h3>Content Optimization</h3>
            <p>Optimize your content strategy based on audience feedback and sentiment analysis results.</p>
          </div>
        </div>
      </div>

      {/* How It Works Section */}
      <div className="how-section">
        <div className="how-title">How It Works</div>
        <ul className="how-list">
          <li>
            <span className="how-icon">🔗</span>
            <span>
              <span className="how-step-title">Paste Video URL</span>
              <span className="how-step-desc"> — Enter the URL of the video you want to analyze.</span>
            </span>
          </li>
          <li>
            <span className="how-icon">🤖</span>
            <span>
              <span className="how-step-title">Analyze Sentiment</span>
              <span className="how-step-desc"> — Our tool analyzes the video comments and provides a analysis data.</span>
            </span>
          </li>
          <li>
            <span className="how-icon">📊</span>
            <span>
              <span className="how-step-title">View Results</span>
              <span className="how-step-desc"> — View detailed sentiment analysis results, including overall sentiment, key themes, and audience reactions.</span>
            </span>
          </li>
        </ul>
      </div>

      {/* Display Results Section */}
      {results && <ResultsDisplay data={results} />}

      {/* Footer Section */}
      <footer className="footer-section">
        <p>&copy; 2023 Praveen Kumar. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
