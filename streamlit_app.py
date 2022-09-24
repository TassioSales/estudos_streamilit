#criar questionario com streamlitApp

import streamlit as st
import pandas as pd

#criar titulo
st.title('Questionário de avaliação de desempenho')

#criar subtitulo
st.subheader('Avalie o desempenho do funcionário')

#criar um texto
st.text('Avalie o desempenho do funcionário')


#criar um checkbox
st.checkbox('Avaliar')

#criar um radio
st.radio('Avaliar', ('Sim', 'Não'))