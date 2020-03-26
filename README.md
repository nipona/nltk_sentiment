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

### Analysis

* Which one words better, nltk or textblob?

Accuracy achieved by NLTK is around 70 percent and accuracy achieved by Textblob is 60 percent. Clearly, nltk has out performed textblob by a good margin.

* What is the advantage with bag of words approach?

Sentiment Analysis suffers from lack of availability of labelled dataset. Labelling data is a tiresome and expensive process and such datasets may not be available for many domains. Bag of words is a very simple approach which can be used for sentiment analysis when getting labelled dataset is not a viable option.

* When is bag of words not a good option?

Bag of words may not be a good option for certain domains. For example, let us test few examples from financial domain:

```
text = “I want to know the current price of the share”
get_sentiment(text, algo=”nltk”)
0.3612
text = “We want to discuss about the new bond issue”
get_sentiment(text, algo=”textblob”)
0.136
```

So, we notice that although both the sentences are neutral in financial sense but out algorithms, both nltk and vader, think they carry some sentiment. Hence, bag-of-words may not work from some domains like Finance, Medical etc.
