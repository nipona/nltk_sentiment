## Sentiment Analysis for feedback data


* Sentiment Analysis, although a vastly researched subject, suffers in some areas. One major reason for this is the lack of domain specific labelled data. Without labelled data, our ability to run and train machine learning models get affected and we are not able to produce results. Here, we are going to try out two pre-trained sentiment libraries nltk and textblob.
* Both nltk and textblob works on bag of words model and may not be the best choice for few domains like finance etc. We are going to try them on general feedback data and compare the results.


* Here is the setp-by-step guide for the same:

1. Download the code from here

```https://github.com/nipona/sentiment.git```

2. Install the following libraries in python (if not already installed)

```
pip install nltk
pip install textblob
```

3. Test the output using get_sentiment file
```
text="I am happy with the services provided"
get_sentiment(text, algo="nltk")
0.5719
get_sentiment(text, algo="textblob")
0.8
text="I am frustrated at not being able to reach your executive"
get_sentiment(text, algo="nltk")
-0.5106
get_sentiment(text, algo="textblob")
-0.09999999999999998
```
### Although we tested with very limited sentences, but nltk seems to be working better than textblob. You can also test with sentences from different domains and compare the results.
