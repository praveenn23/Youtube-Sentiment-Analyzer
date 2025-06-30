import React from 'react';
import {
  PieChart, Pie, Cell, ResponsiveContainer,
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip
} from 'recharts';

const COLORS = ['#4caf50', '#ff9800', '#f44336', '#2196f3'];

const ResultsDisplay = ({ data }) => {
  if (!data) return null;

  const {
    total_comments = 0,
    sentiment_distribution = {},
    average_scores = {},
    chart_data = [],
    sample_comments = []
  } = data;

  const pieData = Object.entries(sentiment_distribution).map(([sentiment, count]) => ({
    name: sentiment.charAt(0).toUpperCase() + sentiment.slice(1),
    value: count,
    percentage: ((count / total_comments) * 100).toFixed(1)
  }));

  const barData = [
    { name: 'Positive', value: average_scores.positive || 0, color: '#4caf50' },
    { name: 'Neutral', value: average_scores.neutral || 0, color: '#ff9800' },
    { name: 'Negative', value: average_scores.negative || 0, color: '#f44336' },
    { name: 'Compound', value: average_scores.compound || 0, color: '#2196f3' }
  ];

  const getSentimentIcon = (sentiment) => {
    switch (sentiment.toLowerCase()) {
      case 'positive': return '🙂';
      case 'negative': return '🙁';
      default: return '😐';
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Analysis Results</h2>

      <div>
        <h3>Total Comments Analyzed</h3>
        <p>{total_comments}</p>
      </div>

      <div>
        <h3>Sentiment Breakdown</h3>
        {Object.entries(sentiment_distribution).map(([sentiment, count]) => (
          <div key={sentiment}>
            <span style={{ fontSize: '24px' }}>{getSentimentIcon(sentiment)}</span>
            <h4>{sentiment.charAt(0).toUpperCase() + sentiment.slice(1)} Comments</h4>
            <p>{count} ({((count / total_comments) * 100).toFixed(1)}%)</p>
          </div>
        ))}
      </div>

      <div>
        <h3>Sentiment Distribution</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={pieData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percentage }) => `${name}: ${percentage}%`}
                outerRadius={80}
                dataKey="value"
              >
                {pieData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div>
        <h3>Average Sentiment Scores</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={barData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value">
                {barData.map((entry, index) => (
                  <Cell key={`bar-${index}`} fill={entry.color} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div>
        <h3>Sample Comments</h3>
        <ul>
          {sample_comments.length === 0 ? (
            <p>No comments available.</p>
          ) : (
            sample_comments.map((comment, index) => (
              <li key={index} style={{ marginBottom: '10px' }}>
                <span style={{ marginRight: '5px' }}>{getSentimentIcon(comment.sentiment)}</span>
                <strong>{comment.sentiment}</strong> (Score: {comment.compound?.toFixed(3)})<br />
                <span>{comment.comment}</span>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
};

export default ResultsDisplay;

