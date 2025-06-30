import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def plot_sentiment_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sentiment', data=df, palette='viridis')
    plt.title('Sentiment Distribution of YouTube Comments')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Comments')
    
    # Save the plot to a file
    plot_filename = 'sentiment_distribution.png'
    plt.savefig(plot_filename)
    plt.close()
    
    return plot_filename 