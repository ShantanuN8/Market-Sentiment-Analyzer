# Market Sentiment Analyzer 📊

A Python-based tool to analyze market sentiment using news and social media data. Extract actionable insights at scale using NLP and data visualization.

---

## 🚀 Features

- **Multi-source sentiment analysis**: Collects data from news headlines, tweets, Reddit, and more.
- **Modern NLP pipeline**: Clean, tokenize, vectorize text and infer sentiment using pre-trained models.
- **Visual dashboards**: Built-in support for time-series charts, word clouds, sentiment distributions.
- **Modular design**: Easily extend with new data sources, sentiment models, or visualizations.
- **Reports & metrics**: Automatic summary of sentiment trends, polarity breakdown, and sentiment‑stock correlations.

---

## 🧭 Getting Started

### Prerequisites
- Python 3.8+
- `pip` package manager

### Installation

```bash
git clone https://github.com/ShantanuN8/Market-Sentiment-Analyzer.git
cd Market-Sentiment-Analyzer
python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
.\venv\Scripts\Activate
pip install -r requirements.txt
```

### Configuration
- Copy `.env.example` to `.env` and fill in your API keys (e.g. Twitter, Reddit, or financial news APIs).
- Modify settings in `config/*.py` to adjust data sources, date/range options, or output paths.

---

## 🧩 Usage Examples

### 1. Run Market Sentiment Analysis

```bash
python run_sentiment.py \
  --symbol TSLA \
  --start-date 2025-01-01 \
  --end-date 2025-06-30
```

Generates:
- Sentiment timeseries CSV
- Weekly sentiment summary report
- Optional interactive dashboard output

### 2. Interactive Dashboard

```bash
python visualize/dashboard.py \
  --symbol TSLA --dashboard-type timeseries
```

Displays charts like daily sentiment and stock correlation plots.

### 3. Custom Analysis Script

```python
from analyzer import SentimentAnalyzer

sa = SentimentAnalyzer(source="twitter", symbol="AAPL")
data = sa.fetch_data(start='2025-07-01', end='2025-08-01')
sentiment = sa.compute_sentiment(data)
sa.save_report(sentiment, path="reports/AAPL_July.md")
```

---

## 📂 Project Structure

```
 Market‑Sentiment‑Analyzer/
 ├── analyzer/
 │   ├── __init__.py
 │   ├── fetchers/        # Data collection modules (twitter, news, reddit…)
 │   ├── processors/      # Cleaning, tokenizing, sentiment scoring
 │   └── utils/           # Helper functions, config loader
 ├── visualize/
 │   ├── dashboard.py
 │   └── charts.py
 ├── tests/
 │   ├── test_fetchers.py
 │   └── test_processors.py
 ├── config/
 │   └── default_settings.py
 ├── requirements.txt
 ├── run_sentiment.py     # Entry‑point script
 ├── .env.example
 └── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Here’s how:
1. Fork the repository.
2. Create a feature branch: `git checkout -b my-feature`
3. Add your feature or fix.
4. Add tests if applicable (`tests/`).
5. Submit a Pull Request.

---

## 🧪 Testing

Run automated tests with:

```bash
pytest
```

Coverage and linting (if configured) can be enabled via CI pipelines.

---

## 🎯 Roadmap / Upcoming Enhancements

- Support for **FinBERT** or custom transformer models for financial-domain sentiment  
- Integration with **news sentiment datasets** like SEntFiN 1.0 for entity-aware polarity analysis  
- Real-time dashboards with dynamic stock-sentiment correlation  
- Backtesting trading strategies based on sentiment signals

---

## ⚖️ License

MIT License. See the [LICENSE](LICENSE) file for full details.

---

## ❗ Disclaimer

This project is intended for educational/research use. Not financial advice. Market sentiment is just one input—please conduct your own due diligence.

---

## 📬 Contact

Maintainer: **Shantanu N.**  
GitHub: [ShantanuN8](https://github.com/ShantanuN8)  
Feel free to open an issue or discussion if you have questions or ideas!
