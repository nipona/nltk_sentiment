from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


sia = SentimentIntensityAnalyzer()

def get_sentiment(text, algo="nltk"):
    if algo=="nltk":
        score = sia.polarity_scores(text)["compound"]
    elif algo=="textblob":
        score = TextBlob(text).sentiment.polarity

    return score

