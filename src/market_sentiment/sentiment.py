from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config.settings import SENTIMENT_THRESHOLDS

class SentimentAnalyzer:
    def __init__(self):
        self.vader=SentimentIntensityAnalyzer()
        self.thresholds=SENTIMENT_THRESHOLDS
    def analyze(self, text):

        textblob_score=TextBlob(text).sentiment.polarity
        vader_score =self.vader.polarity_scores(text)['compound']
        final_score=(textblob_score+vader_score)/2
        if final_score >self.thresholds['positive']:
            return 'Positive', final_score,textblob_score, vader_score 
        elif final_score >self.thresholds['negative']:
            return 'Negative', final_score,textblob_score, vader_score
        else:
            return 'Neutral', final_score,textblob_score, vader_score