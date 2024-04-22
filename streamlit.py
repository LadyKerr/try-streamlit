import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Flight Data Analysis ✈️")
st.write("This is a simple example of a Streamlit app")

@st.cache_resource
def load_data():
    return pd.read_csv('flights.csv')

data = load_data()

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Summary statistics')
st.write(data.describe())

# Bar chart of flights per Carrier
st.subheader('Bar plot of flights per Carrier')
data['Carrier'].value_counts().plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
st.pyplot(plt)

# create a bar chart of flights delayed
st.subheader('Bar plot of flights delayed')
delayed_flights = data[data['ArrDelay'] > 0]
st.bar_chart(delayed_flights['Carrier'].value_counts())
