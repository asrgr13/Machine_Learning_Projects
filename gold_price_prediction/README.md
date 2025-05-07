# 🪙 Gold Price Prediction (IDR) using Machine Learning

This project aims to predict future gold prices in Indonesian Rupiah (IDR) using historical gold price data, exchange rates, and macroeconomic indicators such as interest and inflation rates.

---

## 📌 Project Goals

- 📈 Forecast daily or custom-period gold price trends in IDR.
- 🔄 Integrate real-time data via APIs.
- 🤖 Build predictive models (ARIMA, LSTM, XGBoost, etc.).
- 🌐 Deploy as a simple dashboard or alerting system.

---

## 📊 Features Used

- Gold price (XAU/IDR)
- USD/IDR exchange rate
- Indonesia interest rate (BI 7-Day Repo)
- Inflation rate (CPI or monthly YoY%)
- (Optional) Stock market index, oil price, global trends

---

## 🔧 Technologies & Tools

- **Python** (pandas, requests, scikit-learn, etc.)
- **APIs**:
  - [GoldAPI](https://www.goldapi.io/)
  - [Metals-API](https://metals-api.com/)
  - [Bank Indonesia](https://www.bi.go.id/) (manual/scraped if no API)
  - [TradingEconomics](https://tradingeconomics.com/)
- **Jupyter Notebooks / VSCode**
- **ML Models**: ARIMA, XGBoost, LSTM (planned)
- **Deployment**: Streamlit, Flask (planned)

---

## 📦 Project Structure

```bash
gold-price-prediction/
│
├── data/                  # Saved historical CSVs
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── scripts/               # Python scripts for API data collection
│   └── fetch_gold_price.py
├── models/                # Saved model files
├── app/                   # Future dashboard or bot
│
├── README.md
└── requirements.txt
