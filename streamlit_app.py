#criar questionario com streamlitApp

import streamlit as st
import pandas as pd

#criar titulo
st.title('Questionário de avaliação de desempenho')

#criar subtitulo
st.subheader('Avalie o desempenho do funcionário')

#criar um texto
st.text('Avalie o desempenho do funcionário')


#criar um radio
st.radio('Avaliar', ('Sim', 'Não'))

#pergunta o nome do funcionário
st.text_input('Nome do funcionário')

#pergunta a data
st.date_input('Data')

