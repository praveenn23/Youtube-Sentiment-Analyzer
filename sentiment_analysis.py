import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(comments):
    """
    Analyze sentiment of comments using NLTK VADER.
    Args:
        comments (List[str]): List of comment texts.
    Returns:
        pd.DataFrame: DataFrame with columns ['comment', 'neg', 'neu', 'pos', 'compound', 'sentiment']
    """
    sia = SentimentIntensityAnalyzer()
    results = []
    for comment in comments:
        scores = sia.polarity_scores(comment)
        sentiment = 'positive' if scores['compound'] > 0.05 else 'negative' if scores['compound'] < -0.05 else 'neutral'
        results.append({
            'comment': comment,
            'neg': scores['neg'],
            'neu': scores['neu'],
            'pos': scores['pos'],
            'compound': scores['compound'],
            'sentiment': sentiment
        })
    return pd.DataFrame(results)


def analyze_toxicity(comments):
    """
    Placeholder for toxicity analysis. Returns neutral for all.
    Args:
        comments (List[str]): List of comment texts.
    Returns:
        pd.DataFrame: DataFrame with columns ['comment', 'toxicity']
    """
    # TODO: Implement real toxicity analysis (e.g., using a pre-trained model)
    return pd.DataFrame({'comment': comments, 'toxicity': ['neutral'] * len(comments)}) 