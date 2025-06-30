import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(comments):
    sid = SentimentIntensityAnalyzer()
    
    data = {'comment': [], 'neg': [], 'neu': [], 'pos': [], 'compound': [], 'sentiment': []}
    
    for comment in comments:
        score = sid.polarity_scores(comment)
        data['comment'].append(comment)
        data['neg'].append(score['neg'])
        data['neu'].append(score['neu'])
        data['pos'].append(score['pos'])
        data['compound'].append(score['compound'])
        
        if score['compound'] >= 0.05:
            data['sentiment'].append('Positive')
        elif score['compound'] <= -0.05:
            data['sentiment'].append('Negative')
        else:
            data['sentiment'].append('Neutral')
            
    df = pd.DataFrame(data)
    return df 