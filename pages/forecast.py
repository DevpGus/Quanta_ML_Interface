import streamlit as st
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import gzip

# Se o usuário não estiver autenticado, redirecione para login
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/account.py")

# URL do arquivo no GitHub Releases
url = "https://github.com/DevpGus/Quanta_ML_Interface/releases/download/v1.0.0/sarima.pkl.gz"
output_path = "sarima_model.pkl.gz"

# Baixar o arquivo compactado
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(output_path, "wb") as file:
        file.write(response.content)
    print(f"Arquivo baixado: {output_path}")
else:
    print(f"Erro ao baixar o arquivo: {response.status_code}")


with open('./assets/src/forecast.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')
df['Time'] = pd.to_datetime(df['dt'])
df = df.set_index('Time')

df = pd.DataFrame(df['LandAverageTemperature'])
df['LandAverageTemperature'] = df['LandAverageTemperature'].fillna(df['LandAverageTemperature'].rolling(window=6, min_periods=1).mean())


st.title('Fazer Previsão')

with st.container():
    st.write('Selecione o período (em meses) para previsão da Temperatura Média da Superfície da Terra.')
    st.date_input('Data Desejada', value=None, min_value='2016-01-01', key='pred_time')
    
col1, col2 = st.columns(2)
with col1:
    prev = st.button('Enviar', type="primary", use_container_width=True, key='btn_prev')
with col2:
    st.button('Limpar', type="primary", use_container_width=True, key='btn_reset')

st.divider()

if st.session_state.pred_time is not None:
    pred_time = (st.session_state.pred_time.year * 12 + st.session_state.pred_time.month) - (1750*12)

# Previsão
if prev:
    if st.session_state.pred_time is None:
        st.error('Selecione uma data válida para fazer a previsão.')
    else:
        if pred_time is not None:
            st.toast('Previsão feita! Carregando Resultados...', icon=":material/check_circle_outline:")
            st.write(f'Previsão de Temperatura Média da Superfície da Terra para o mês {st.session_state.pred_time.month} de {st.session_state.pred_time.year}')
            
            
            with gzip.open(output_path, "rb") as f:
                model = pickle.load(f)

            df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')
            pred = []
            pred = model.predict(start=3185, end=pred_time)

            y = df.iloc[-700:]
            y.index = pd.to_datetime(y['dt'])

            fig, ax = plt.subplots()
            fig.set_size_inches(20, 5)
            ax.plot(y.index, y['LandAverageTemperature'], label='Original')
            ax.plot(pred.index, pred, label='Predicted')
            ax.legend()
            ax.grid()
            st.pyplot(fig)

##################

