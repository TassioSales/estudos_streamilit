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

#salvar o resultado em um dataframe
df = pd.DataFrame(columns=['Nome do funcionário', 'Data', 'Avaliar'])

#criar um botão
if st.button('Salvar'):
    df = df.append({'Nome do funcionário': st.text_input('Nome do funcionário'), 'Data': st.date_input('Data'), 'Avaliar': st.radio('Avaliar', ('Sim', 'Não'))}, ignore_index=True)
    st.write(df)
    



