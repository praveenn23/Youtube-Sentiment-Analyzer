import sys
import pandas as pd
import nltk
from youtube_scraper import get_comments
from sentiment_analysis import analyze_sentiment
from utils import plot_sentiment_distribution, save_to_csv

# Download NLTK VADER lexicon if not already present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

def main():
    print("YouTube Comment Sentiment Analysis\n")
    video_url = input("Enter YouTube video URL: ").strip()
    api_key = "AIzaSyAdy0uk4cYfx8nFMmgOEOk0H01MKfNIU28"  # Replace with your YouTube Data API key
    max_comments = 500

    try:
        comments = get_comments(video_url, api_key, max_comments)
        print(f"Fetched {len(comments)} comments.")
    except Exception as e:
        print(f"Error fetching comments: {e}")
        sys.exit(1)

    print("Analyzing sentiment...")
    df = analyze_sentiment(comments)
    print(df[['comment', 'sentiment']].head())

    plot_sentiment_distribution(df)

    save = input("Save results to CSV? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (default: results.csv): ").strip() or 'results.csv'
        save_to_csv(df, filename)
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    main() 