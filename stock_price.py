import pandas as pd
import streamlit as st
import yfinance as yf

st.write("""
# simple stock price app, 
shown are the stock **closing price** and ***volume of Apple.!***
""")

tickerSymbol="AAPL"
tickerData=yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period="1d",start="2010-5-31",end="2020-5-31")

st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)