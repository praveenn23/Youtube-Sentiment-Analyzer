from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import nltk
from youtube_scraper import get_comments
from sentiment_analysis import analyze_sentiment
from utils import plot_sentiment_distribution, save_to_csv

app = Flask(__name__)
CORS(app)

# Download NLTK VADER lexicon if not already present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'ok', 'message': 'API is running'})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    video_url = data.get('video_url')
    api_key = data.get('api_key')
    max_comments = data.get('max_comments', 500)

    if not video_url:
        return jsonify({'error': 'URL is required'}), 400

    if not api_key:
        return jsonify({'error': 'API key is required'}), 400

    try:
        comments = get_comments(video_url, api_key, max_comments)
    except Exception as e:
        return jsonify({'error': f"Error fetching comments: {str(e)}"}), 500

    if not comments:
        return jsonify({'error': 'No comments found or could not fetch comments.'}), 404

    df = analyze_sentiment(comments)
    
    total_comments = len(df)
    sentiment_distribution = df['sentiment'].value_counts().to_dict()
    average_scores = {
        'positive': df['pos'].mean(),
        'neutral': df['neu'].mean(),
        'negative': df['neg'].mean(),
        'compound': df['compound'].mean()
    }
    sample_comments = df.head(5).to_dict(orient='records')

    results = {
        'total_comments': total_comments,
        'sentiment_distribution': sentiment_distribution,
        'average_scores': average_scores,
        'sample_comments': sample_comments,
        'all_comments': df.to_dict(orient='records')
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True) 