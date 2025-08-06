from src.market_sentiment.sentiment import SentimentAnalyzer

def test_basic_sentiment():
    analyzer=SentimentAnalyzer()
    assert analyzer.analyze("Stocks rallied on strong earnings")[0]=="Positive"
    assert analyzer.analyze("Markets crashed due to bad news")[0]=="Negative"
    assert analyzer.analyze("The Federal Reserve kep rates unchanged")[0] in ["Neutral", "Negative","Positive"]
