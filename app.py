# Hat tip/acknowledgement to Chanin Nantasenamat - The Data Professor - and his
# Medium Blog Post titled, "How to Build a Data Science Web App in Python"
# URL: https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020

"""
File: app.py
A simple data-driven web app using the streamlit Python library in just a few lines of code.
"""

# Import libraries
import yfinance as yf
import streamlit as st

st.write("""
# Simple stock price app
Shown are the stock closing price and volume of Google
""")

tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-6-15', end='2020-6-15')

# Open  High    Low     Close   Volume  Dividends       Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
