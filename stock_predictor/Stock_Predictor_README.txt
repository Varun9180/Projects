
===========================================
Stock Health Predictor (ML Web App using Streamlit)
===========================================

Description:
---------------
This is a machine learning web application built using **Streamlit** and **Linear Regression** to predict the next day's closing price of a given stock. It uses historical stock data fetched live via the **Yahoo Finance API (yfinance)**.

Features:
------------
- Enter any valid stock ticker (e.g., AAPL, RELIANCE.NS)
- Automatically fetches last 180 days of stock data
- Predicts next day closing price using Linear Regression
- Shows uptrend/downtrend analysis
- Investment suggestion: Buy, Sell, or Wait
- Visualizes the last 30 days of stock price

How to Run:
--------------
1. Install dependencies:
   ```
   pip install streamlit yfinance pandas numpy matplotlib scikit-learn
   ```

2. Save the script as `stock_predictor.py`.

3. Run the Streamlit app:
   ```
   streamlit run stock_predictor.py
   ```

4. Enter a stock ticker (like `AAPL` or `RELIANCE.NS`) in the input box and view the prediction.

Visualization:
------------------
- Line chart showing last 30 days of closing prices
- Dashed line showing predicted closing price for the next day

Suitable For:
-----------------
- Students learning basic stock price modeling
- Beginners working with regression algorithms
- Finance & data science hobbyists

Utilities Used:
------------------------
- Python
- Streamlit
- yfinance
- Linear Regression (scikit-learn)
- Matplotlib
- Pandas, NumPy