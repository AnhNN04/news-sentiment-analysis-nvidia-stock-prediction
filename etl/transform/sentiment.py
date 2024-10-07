import json
import re
import pandas as pd
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Run two lines below only 1 time when download vader_lexicon for sentiment
#import nltk
#nltk.download('vader_lexicon')

# Clean text before sentiment analysis
"""
Here are common cleaning steps:
    Remove URLs.
    Remove special characters.
    Convert text to lowercase.
    Optionally, remove stopwords (though Transformer models handle this well).
"""
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove special characters and numbers
    text = re.sub(r'\W', ' ', text)
    # Remove single characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # Convert to lowercase
    text = text.lower()
    return text

# Function to get specific sentiment scores (positive, negative, neutral)
def get_sentiment_scores(sia,text):
    sentiment = sia.polarity_scores(text)
    return sentiment['pos'], sentiment['neg'], sentiment['neu']

def sentiment(json_obj_list):
    # Initialize VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Initial a list for contain sentiment news
    sentiment_list = []

    # Perform sentiment analysis
    for json_obj in json_obj_list:
        # Preprocessing content before sentiment
        text = clean_text(json_obj['Content'])
        # Sentiment
        json_obj['Positive'],json_obj['Negative'],json_obj['Neutral']  = get_sentiment_scores(sia,text)
        # Append to sentiment_list
        sentiment_list.append(json_obj)

    # Return results
    return sentiment_list