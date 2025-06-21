import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Predictor", layout="centered")

st.title("Stock Health Predictor (ML App)")
st.write("Enter a stock ticker to predict the next day's closing price.")

# Input box for stock ticker
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, RELIANCE.NS):").upper()

if ticker:
    try:
        with st.spinner("Fetching and processing data..."):
            # Date range
            end_date = datetime.today().date()
            start_date = end_date - timedelta(days=180)

            # Fetch data
            df = yf.download(ticker, start=start_date, end=end_date)

        if df.empty:
            st.error("No data found for this ticker.")
        else:
            # Use Close price
            df = df[["Close"]]
            df["Next_Close"] = df["Close"].shift(-1)
            df.dropna(inplace=True)

            # ML Training
            X = df[["Close"]]
            y = df["Next_Close"]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            model = LinearRegression()
            model.fit(X_train, y_train)

            today_close = float(df["Close"].iloc[-1])
            predicted_next = model.predict(np.array(today_close).reshape(1, -1))[0]

            # Trend Analysis
            change = predicted_next - today_close
            trend = "Uptrend" if change > 0 else "Downtrend"
            suggestion = "Buy" if change > 1 else "Wait" if -1 <= change <= 1 else "Sell"

            # Show Results
            st.subheader("Prediction Result")
            st.write(f"**Today's Close:** {today_close:.2f}")
            st.write(f"**Predicted Next Day Close:** {predicted_next:.2f}")
            st.write(f"**Trend:** {trend}")
            st.write(f"**Suggestion:** {suggestion}")

            # Chart
            st.subheader("Last 30 Days Trend")
            fig, ax = plt.subplots(figsize=(10, 4))
            df["Close"].tail(30).plot(ax=ax, label="Last 30 Days")
            ax.axhline(predicted_next, color='green', linestyle='--', label="Predicted Tomorrow")
            ax.set_title(f"{ticker} - Close Price")
            ax.set_ylabel("Price")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
