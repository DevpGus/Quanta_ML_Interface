import streamlit as st
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

with open('./assets/src/forecast.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')
df['Time'] = pd.to_datetime(df['dt'])
df = df.set_index('Time')

df = pd.DataFrame(df['LandAverageTemperature'])
df['LandAverageTemperature'] = df['LandAverageTemperature'].fillna(df['LandAverageTemperature'].rolling(window=6, min_periods=1).mean())


st.title('Fazer Previsão')

# Example Inputs
# c1, c2 = st.columns(2)
# with c1:
#     input_0 = st.selectbox('Selecione o tipo de dado', ['Dado 1', 'Dado 2', 'Dado 3'])
#     input_1 = st.selectbox('Selecione o tipo de dado', ['Dado 4', 'Dado 5', 'Dado 6'])
#     input_2 = st.selectbox('Selecione o tipo de dado', ['Dado 7', 'Dado 8', 'Dado 9'])
#     input_3 = st.selectbox('Selecione o tipo de dado', ['Dado 10', 'Dado 11', 'Dado 12'])
#     input_4 = st.number_input('Número 1')

# with c2:
#     input_5 = st.text_input('Nome')
#     input_6 = st.text_input('Idade')
#     input_7 = st.text_input('Sexo')
#     input_8 = st.text_input('Peso')
#     input_9 = st.number_input('Número 2')

st.write('Selecione o período (em meses) para previsão da Temperatura Média da Superfície da Terra.')
st.date_input('Data Desejada', value=None, min_value='2015-12-01', key='pred_time')

if st.session_state.pred_time is not None:
    pred_time = (st.session_state.pred_time.year * 12 + st.session_state.pred_time.month) - (2015*12 + 12)

     
model = sm.tsa.statespace.SARIMAX(df['LandAverageTemperature'],
                                order=(2, 0, 2),
                                seasonal_order=(2, 1, 0, 12),
                                trend='t').fit()

# Botões de Previsão e Reset
with st.container():
    col1, col2 = st.columns(2)
    with col1:
            st.button('Enviar', type="primary", use_container_width=True, key='btn_prev')
    with col2:
            st.button('Limpar', type="primary", use_container_width=True, key='btn_reset')

st.divider()

# Previsão
if st.session_state.btn_prev:
    if st.session_state.pred_time is None:
        st.error('Selecione uma data válida para fazer a previsão.')
    else:
        if pred_time is not None:
            st.toast('Previsão feita com sucesso!', icon=":material/check_circle_outline:")
            st.write(f'Previsão de Temperatura Média da Superfície da Terra para o mês {st.session_state.pred_time.month} de {st.session_state.pred_time.year}')
            
            df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')
            pred = model.forecast(pred_time)

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

