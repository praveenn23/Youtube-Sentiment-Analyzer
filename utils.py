import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df, sentiment_col='sentiment'):
    """
    Plot the distribution of sentiment labels in the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame with sentiment results.
        sentiment_col (str): Column name for sentiment labels.
    """
    plt.figure(figsize=(6,4))
    sns.countplot(x=sentiment_col, data=df, palette='Set2')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def save_to_csv(df, filename):
    """
    Save DataFrame to a CSV file.
    Args:
        df (pd.DataFrame): DataFrame to save.
        filename (str): Output CSV filename.
    """
    df.to_csv(filename, index=False) 