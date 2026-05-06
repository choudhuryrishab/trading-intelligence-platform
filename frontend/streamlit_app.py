import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/portfolio"

st.title("📊 Trading Dashboard")

try:
    data = requests.get(API_URL, timeout=3).json()

    # Cash
    st.subheader("💰 Cash")
    st.write(f"${data['cash']}")

    # Stocks
    st.subheader("📈 Positions")

    stocks = data.get("stocks", [])

    if not stocks:
        st.warning("No stocks found")

    for s in stocks:
        col1, col2, col3 = st.columns(3)

        col1.write(s["ticker"])
        col2.write(f"Qty: {s['quantity']}")
        col3.write(f"Avg: {s['avg_price']}")

    # Summary
    st.subheader("📊 Summary")
    st.write(f"Total positions: {data.get('total_positions', len(stocks))}")

except Exception as e:
    st.error(f"Backend error: {e}")