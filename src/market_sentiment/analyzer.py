from .scraper import NewsScraper
from .sentiment import SentimentAnalyzer
from .excel_export import ExcelExporter 
from config.settings import PORTFOLIOS
from collections import Counter
from datetime import datetime

class MarketSentimentAnalyzer:
    def __init__(self):
        self.scraper= NewsScraper()
        self.sentiment= SentimentAnalyzer()
        self.exporter= ExcelExporter()

    def run(self):
        headlines = self.scraper.scrape()
        data=[]
        for h in headlines:
            sentiment, final_score, tb_s, vd_s =self.sentiment.analyze(h['headline'])
            d=h.copy()
            d['final_sentiment']=sentiment
            d['final_score']=final_score
            d['textblob_score']=tb_s
            d['vader_score']=vd_s
            data.append(d)

        summary=Counter([d['final_sentiment'] for d in data])
        avg_score=round(sum(d['final_score']for d in data)/max(1,len(data)),3)
        print(f'Market Sentiment Summary: {summary}, Avg Score:{avg_score}')
        filename=f"market_sentiment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        report=self.exporter.export(data, summary, filename)
        print(f'Results saved:{report}')