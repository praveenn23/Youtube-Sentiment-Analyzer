# YouTube Sentiment Analyzer

A modern web application that analyzes the sentiment of YouTube video comments using AI-powered natural language processing. Built with React frontend and Flask backend.

## Features

- 🎥 **YouTube Integration**: Fetch comments from any YouTube video using the official API
- 🤖 **AI-Powered Analysis**: Advanced sentiment analysis using NLTK VADER
- 📊 **Visual Insights**: Beautiful charts and statistics to understand comment sentiment
- 🎨 **Modern UI**: Responsive design with Material-UI components
- 📱 **Mobile Friendly**: Works seamlessly on desktop and mobile devices

## Screenshots

The application features:
- Clean, modern interface with YouTube-inspired design
- Real-time sentiment analysis with progress indicators
- Interactive charts showing sentiment distribution
- Sample comments with sentiment labels and scores
- Responsive design for all screen sizes

## Prerequisites

Before running this application, you need:

1. **Python 3.7+** installed on your system
2. **Node.js 14+** and npm installed on your system
3. **YouTube Data API Key** from Google Cloud Console

### Getting a YouTube Data API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the YouTube Data API v3
4. Create credentials (API Key)
5. Copy the API key for use in the application

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Youtube_Sentiment
   ```

2. **Install dependencies**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Install Node.js dependencies
   cd frontend
   npm install
   cd ..
   ```

3. **Install concurrently (for running both servers)**
   ```bash
   npm install
   ```

## Usage

### Option 1: Run Both Frontend and Backend Together
```bash
npm start
```

### Option 2: Run Separately

**Backend (Flask API)**
```bash
python app.py
```
The backend will run on `http://localhost:5000`

**Frontend (React App)**
```bash
cd frontend
npm start
```
The frontend will run on `http://localhost:3000`

## How to Use

1. **Open the application** in your browser at `http://localhost:3000`

2. **Enter the required information**:
   - YouTube Video URL (e.g., `https://www.youtube.com/watch?v=VIDEO_ID`)
   - Your YouTube Data API Key
   - Maximum number of comments to analyze (1-1000)

3. **Click "Analyze Sentiment"** to start the analysis

4. **View the results**:
   - Summary cards showing total comments and sentiment distribution
   - Interactive pie chart of sentiment distribution
   - Bar chart of average sentiment scores
   - Sample comments with sentiment labels and scores

## API Endpoints

### POST `/api/analyze`
Analyzes the sentiment of YouTube video comments.

**Request Body:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "api_key": "YOUR_YOUTUBE_API_KEY",
  "max_comments": 500
}
```

**Response:**
```json
{
  "total_comments": 500,
  "sentiment_distribution": {
    "positive": 250,
    "negative": 100,
    "neutral": 150
  },
  "average_scores": {
    "positive": 0.15,
    "negative": 0.08,
    "neutral": 0.77,
    "compound": 0.12
  },
  "chart_data": "base64_encoded_chart_image",
  "sample_comments": [
    {
      "comment": "Great video!",
      "sentiment": "positive",
      "compound": 0.6369
    }
  ]
}
```

### GET `/api/health`
Health check endpoint.

## Project Structure

```
Youtube_Sentiment/
├── app.py                 # Flask backend API
├── main.py               # Original CLI application
├── youtube_scraper.py    # YouTube comment fetching
├── sentiment_analysis.py # Sentiment analysis logic
├── utils.py              # Utility functions
├── requirements.txt      # Python dependencies
├── package.json          # Node.js scripts
├── README.md            # This file
└── frontend/            # React frontend
    ├── public/
    ├── src/
    │   ├── components/
    │   │   ├── ResultsDisplay.js
    │   │   └── SentimentAnalysis.js
    │   ├── App.js
    │   └── App.css
    ├── package.json
    └── README.md
```

## Technologies Used

### Backend
- **Flask**: Python web framework
- **NLTK**: Natural language processing library
- **VADER**: Sentiment analysis tool
- **YouTube Data API**: For fetching video comments
- **Pandas**: Data manipulation
- **Matplotlib/Seaborn**: Chart generation

### Frontend
- **React**: JavaScript library for building user interfaces
- **Material-UI**: React component library
- **Recharts**: Charting library for React
- **Axios**: HTTP client for API calls

## Customization

### Adding New Sentiment Analysis Models
You can extend the sentiment analysis by modifying `sentiment_analysis.py`:

```python
def analyze_sentiment_custom(comments):
    # Add your custom sentiment analysis logic here
    pass
```

### Styling
The application uses Material-UI theming. You can customize the theme in `frontend/src/App.js`:

```javascript
const theme = createTheme({
  palette: {
    primary: {
      main: '#ff0000', // Change primary color
    },
    // Add more customizations
  },
});
```

## Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure the Flask backend is running on port 5000
2. **API Key Errors**: Verify your YouTube Data API key is valid and has the correct permissions
3. **No Comments Found**: Some videos may have comments disabled or limited
4. **Rate Limiting**: YouTube API has quotas, consider reducing max_comments for testing

### Error Messages

- **"Invalid YouTube URL"**: Check that the URL is a valid YouTube video URL
- **"API key not valid"**: Verify your YouTube Data API key
- **"Comments disabled"**: The video may have comments disabled

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- YouTube Data API for providing access to video data
- NLTK team for the VADER sentiment analysis tool
- Material-UI team for the beautiful React components
- Recharts team for the charting library