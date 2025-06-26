# YouTube Comment Sentiment Analysis

This project scrapes comments from a YouTube video and analyzes them for sentiment (positive/negative/neutral) and toxicity.

## Features
- Scrape comments from any public YouTube video
- Analyze sentiment using NLTK
- (Optional) Analyze toxicity using scikit-learn
- Visualize results with charts

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get a YouTube Data API key from [Google Cloud Console](https://console.developers.google.com/).

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter the YouTube video URL and your API key when prompted.

## Files
- `main.py`: Main entry point
- `youtube_scraper.py`: Scrapes comments
- `sentiment_analysis.py`: Analyzes sentiment/toxicity
- `utils.py`: Helper functions

## License
MIT 