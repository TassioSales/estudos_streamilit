#criar nuvens de palavras com base em um texto digitado
import streamlit as st
import pandas as pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title('Word Cloud Generator')

st.markdown('''
This app generates a word cloud from a text input.
''')

st.sidebar.header('User Input Features')

def get_input():
    '''Retorna o texto digitado pelo usuário'''
    return st.sidebar.text_area('Text Input')

def get_wordcloud(text):
    '''Retorna a nuvem de palavras'''
    wordcloud = WordCloud().generate(text)
    return wordcloud.to_image()

text = get_input()
st.subheader('Word Cloud')
st.image(get_wordcloud(text))

st.markdown('''Retorna o texto digitado pelo usuário''')

st.markd