import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title of your app
st.title('Music Track Analysis Dashboard')

# Loading the data
@st.cache  # This decorator caches the data to speed up load times
def load_data():
    df = pd.read_csv('artist_tracks.csv')
    return df

df = load_data()

# Display the DataFrame
if st.checkbox('Show DataFrame'):
    st.write(df)

# Descriptive Statistics
if st.sidebar.button('Show Descriptive Statistics'):
    st.write(df.describe())

# Histogram
if st.sidebar.checkbox('Show Histogram for Danceability'):
    fig, ax = plt.subplots()
    df['danceability'].hist(ax=ax)
    ax.set_title('Distribution of Danceability')
    ax.set_xlabel('Danceability')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Correlation Matrix
if st.sidebar.checkbox('Show Correlation Matrix'):
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

# Energy Distribution by Key (Box Plot)
if st.sidebar.checkbox('Show Box Plot of Energy by Key'):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='key', y='energy', ax=ax)
    ax.set_title('Energy Distribution by Key')
    st.pyplot(fig)
