# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:26:39 2021

@author: Dell
"""
import base64
import yfinance as yf
import streamlit as st

st.title("Stock Price App")
st.markdown("Experience the new way of Browsing Stocks")

st.sidebar.title("Stock Price App")

text = st.sidebar.text_input('Enter the code of company -')
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

option = st.sidebar.selectbox('View and Download Data in Excel',('<Select>','Yes', 'No'))
if option == "Yes":
    st.write("""## Stock data""")
    st.write(tickerDf)
    
    def download():
        csv = tickerDf.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="file.csv">Download Excel File</a>'
        st.markdown(href, unsafe_allow_html=True) 
      
    if st.button('Download'):
        result = download()

elif option == "No":
    pass