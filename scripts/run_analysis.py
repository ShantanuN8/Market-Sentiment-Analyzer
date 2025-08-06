from pathlib import Path 
import sys

project_root= Path(__file__).parent.parent
sys.path.insert(0,str(project_root))
from src.market_sentiment.analyzer import MarketSentimentAnalyzer

if __name__ == '__main__':
    analyzer= MarketSentimentAnalyzer()
    analyzer.run()