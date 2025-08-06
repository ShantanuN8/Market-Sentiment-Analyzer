import os
from pathlib import Path
PROJECT__ROOT=Path(__file__).parent.parent

NEWS_SOURCES={
    'Yahoo_Finance':'https://finance.yahoo.com/news/',
    'MoneyControl':'https://www.moneycontrol.com/news/',
    'The Economic Times':'https://economictimes.indiatimes.com/markets/stocks/news',
    'Mint':'https://www.livemint.com/market/stock-market-news'
}
LOG_DIR=PROJECT__ROOT/'data'/'logs'
LOG_FILE=LOG_DIR/'market_sentiment.log'

SENTIMENT_THRESHOLDS= {'positive': 0.05,'negative': -0.05}
PORTFOLIOS={'Low Risk':{'Govt Bonds':0.6,'Blue-Chip':0.3,'Gold':0.1},
            'Moderate Risk':{'Large-Cap':0.5,'Mid-Cap':0.3,'Equity MF':0.2},
            'High Risk':{'Small-Cap':0.7,'Crypt':0.2,'Gold':0.1}}