import streamlit as st
import pandas as pd
import numpy as np

# Se o usuário não estiver autenticado, redirecione para login
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/account.py")

# Funções para as abas de adição dos dados (manualmente ou por dataset).
def add_data():
    st.session_state['add_data'] = 1
    return

def add_dataset():
    st.session_state['add_data'] = 0
    return

# Início da página
st.title('Inserir Dados')
st.warning('Esta página está em construção.')

# Link do CSS
with open('./assets/src/data.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Estrutura da página
if 'add_data' not in st.session_state:
    st.session_state['add_data'] = 1

c = st.container()
col1, col2 = st.columns(2)
with c:
    with col1:
        btn1 = st.button('Inserir Dados Manualmente', on_click=add_data, use_container_width=True)
    with col2:
        btn2 = st.button('Inserir Banco de Dados', on_click=add_dataset, use_container_width=True)

with st.container():  
# Inserir Manualmente
    if st.session_state['add_data'] == 1:
            with st.container(border=1):
                c1, c2 = st.columns(2)
                with c1:
                    input_0 = st.selectbox('Selecione o tipo de dado', ['Dado 1', 'Dado 2', 'Dado 3'])
                    input_1 = st.selectbox('Selecione o tipo de dado', ['Dado 4', 'Dado 5', 'Dado 6'])
                    input_2 = st.selectbox('Selecione o tipo de dado', ['Dado 7', 'Dado 8', 'Dado 9'])
                    input_3 = st.selectbox('Selecione o tipo de dado', ['Dado 10', 'Dado 11', 'Dado 12'])
                    input_4 = st.number_input('Número 1')

                with c2:
                    input_5 = st.text_input('Nome')
                    input_6 = st.text_input('Idade')
                    input_7 = st.text_input('Sexo')
                    input_8 = st.text_input('Peso')
                    input_9 = st.number_input('Número 2')
            btn3 = st.button('Enviar', type="primary", use_container_width=False)
            
# Inserir Banco de Dados (por padrão csv) // Concatenar com GitHub
    if st.session_state['add_data'] == 0:
        st.warning("Para adicionar novos dados, arraste o arquivo para a área abaixo.")

        upload_file = st.file_uploader('Escolha o arquivo', type='csv')
        if upload_file is not None:
            data = pd.read_csv(upload_file)
            st.write(data)

        with st.expander("Modelo de arquivo CSV para Upload"):
            df = pd.read_csv('./assets/forecasts/data/pokemon_dataset.csv')
            st.dataframe(df.head(10), use_container_width=True)
        
        btn4 = st.button('Concatenar com GitHub', type="primary", use_container_width=False)

