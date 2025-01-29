import streamlit as st
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import pickle

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
    st.date_input('Data Desejada', value=None, min_value='2015-12-01', key='pred_time')
    
    col1, col2 = st.columns(2)
    with col1:
            prev = st.button('Enviar', type="primary", use_container_width=True, key='btn_prev')
    with col2:
            st.button('Limpar', type="primary", use_container_width=True, key='btn_reset')

st.divider()

if st.session_state.pred_time is not None:
    pred_time = (st.session_state.pred_time.year * 12 + st.session_state.pred_time.month) 
    # - (2015*12 + 12)

# Previsão
if prev:
    if st.session_state.pred_time is None:
        st.error('Selecione uma data válida para fazer a previsão.')
    else:
        if pred_time is not None:
            st.toast('Previsão feita! Carregando Resultados...', icon=":material/check_circle_outline:")
            st.write(f'Previsão de Temperatura Média da Superfície da Terra para o mês {st.session_state.pred_time.month} de {st.session_state.pred_time.year}')
            
            with open('./assets/forecasts/sarima_model.pkl', 'rb') as f:
                model = pickle.load(f)  

            df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')
            pred = model.forecast(start=2226, end=pred_time)

            y = df.iloc[-200:]
            y.index = pd.to_datetime(y['dt'])

            fig, ax = plt.subplots()
            fig.set_size_inches(20, 5)
            ax.plot(y.index, y['LandAverageTemperature'], label='Original')
            ax.plot(pred.index, pred, label='Predicted')
            ax.legend()
            ax.grid()
            st.pyplot(fig)

##################

