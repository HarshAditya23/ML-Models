# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:26:39 2021

@author: Dell
"""

import yfinance as yf
import streamlit as st

st.title("Stock Price App")
st.markdown("Experience the new way of Browsing Stocks")

st.sidebar.title("Stock Price App")

text = st.sidebar.text_input('Enter the name of company -')
tickerSymbol = text
tickerData = yf.Ticker(tickerSymbol)

start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

st.sidebar.title("Select the graphs you want -")

if st.sidebar.checkbox("Opening Price", False):
    st.write("""## Opening Price""")
    st.line_chart(tickerDf.Open)

if st.sidebar.checkbox("High Price", False):
    st.write("""## High Price""")
    st.line_chart(tickerDf.High)
    
if st.sidebar.checkbox("Low Price", False):
    st.write("""## Low Price""")
    st.line_chart(tickerDf.Low)

if st.sidebar.checkbox("Closing Price", False):
    st.write("""## Closing Price""")
    st.line_chart(tickerDf.Close)

if st.sidebar.checkbox("Volume", False):
    st.write("""## Volume""")
    st.line_chart(tickerDf.Volume)
    
st.sidebar.title("Explore Raw Stock Data")     

option = st.sidebar.selectbox('View and Download Data in Excel',('','Yes', 'No'))
if option == "Yes":
    st.write("""## Stock data""")
    st.write(tickerDf)
    
    def download(tickerDf):
        tickerDf = yf.download(text, start=start_date, end=end_date)
        data = tickerDf.to_csv('data.csv')
        return data
    
    if st.button('Download'):
        result = download(tickerDf)
        st.write('Download Successful')
    else:
        st.write("Download Failed")

elif option == "No":
    pass