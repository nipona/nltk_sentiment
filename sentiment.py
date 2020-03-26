
#Loading required libraries
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


def get_sentiment(text, algo="nltk"):
    '''
    Description : This function can be used to calculate sentiment of a given text data.It provides option
    to select between two techniqes - nltk vader & textblob
    
    Arguments:
        text : text data
        algo : choose between two algorithms : nltk (for nltk-vader, default) or textblob (for textblob)
    
    Returns:
        A decimal score between -1 to 1 reflicting the sentiment of the given sentence
        
    '''
    
    sia = SentimentIntensityAnalyzer()
    
    if algo=="nltk":
        score = sia.polarity_scores(text)["compound"]
    elif algo=="textblob":
        score = TextBlob(text).sentiment.polarity

    return score

