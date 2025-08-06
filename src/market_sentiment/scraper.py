import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config.settings import NEWS_SOURCES
class NewsScraper:
    def __init__(self):
        self.sources=NEWS_SOURCES
    def scrape(self):
        headlines=[]
        for name,url in self.sources.items():
            try:
                res=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                soup =BeautifulSoup(res.content,'html.parser')
                tags=soup.find_all(['h1','h2','h3'])
                for tag in tags[:8]:
                    text= tag.get_text(strip=True)
                    if 20< len(text)<200:
                        headlines.append({
                            'headline':text,'source':name,
                            'timestamp':datetime.now(),'url':url
                        })
            except Exception:
                continue
        return headlines 