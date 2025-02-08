import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Se o usuário não estiver autenticado, redirecione para login
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/account.py")

# Função de session_state dos gráficos.
def graphs():
    st.session_state['graphs'] = True

# Função de download dos dados.
def download_data():
    with st.spinner('Baixando dados...'):
        time.sleep(3)
    df.to_excel(df, index=False)
    st.sucess('Dados baixados com sucesso!')


# Link do CSS
with open('./assets/src/dashboard.css') as d:
    css = d.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Leitura dos datasets.
df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')

# Leitura do dataset de países & tratamento.
df_countries = pd.read_csv('./assets/forecasts/data/GlobalLandTemperaturesByCountry.csv')
df_countries['time'] = pd.to_datetime(df_countries['dt'], errors='coerce')
df_countries = df_countries.dropna(subset=['time'])

# Estrutura da página
st.title('Análise Gráfica')
st.write('Descrevendo o propósito do modelo, por exemplo: "Este dashboard apresenta previsões baseadas em séries temporais, destacando tendências de temperatura média da superfície global e/ou regional')

st.divider()

# Filtros de seleção
graph = df_countries
with st.container():
    c1, c2, c3 = st.columns(3, gap='medium')
    
    # Filtro de País
    with c1:
        selected_country = st.selectbox('Selecione o País', ['Global'] + sorted(df_countries['Country'].unique().tolist()), key='country')    
    if st.session_state.country == 'Global':
        graph = df_countries.copy()
    else:
        graph = df_countries[df_countries['Country'] == selected_country]
    graph['time'] = graph['time'].dt.date
    
    # Filtro de Intervalo de Tempo
    with c2:
        min_slider = int(graph['time'].min().year)
        max_slider = int(graph['time'].max().year)
        selected_interval = st.slider('Selecione o Período', min_value=min_slider, max_value=max_slider,  value=(min_slider, max_slider) , step=1, key='interval_time')
    
        # Intervalo Seleciondo (em meses)
        inf = st.session_state['interval_time'][0]*12 - (min_slider*12)
        sup = st.session_state['interval_time'][1]*12 - (min_slider*12) 

    # Filtro de Tipo de Dado
    with c3:
        st.selectbox('Selecione o Tipo de Dado', ['Média do Dataset', 'Máxima', 'Mínima'], key='temp_type')
        if st.session_state.temp_type == 'Média do Dataset':
            temp = graph['AverageTemperature'][inf:sup].mean()
        elif st.session_state.temp_type == 'Máxima':
            temp = graph['AverageTemperature'][inf:sup].max()
        else:
            temp = graph['AverageTemperature'][inf:sup].min()

st.write(" ")

# Gráfico e Métricas
with st.container():
    c1, c2 = st.columns([3, 1], gap='medium')
    # Gráfico
    with c1:
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 7)

        # Removendo background
        fig.patch.set_alpha(0)  # Fundo da figura
        ax.set_facecolor((0, 0, 0, 0))  # Fundo dos eixos


        ax.plot(graph['time'][inf:sup], graph['AverageTemperature'][inf:sup], label='Original')
        ax.legend()
        x_labels = graph['time'][inf:sup]
        ax.set_xticks(x_labels[::60])  # Exibe 1 rótulo a cada 30 entradas
        ax.set_xticklabels(x_labels[::60], rotation=45) # Rótulos rotacionados
        st.pyplot(fig)

    # Métricas
    with c2:
        st.metric(label='Temperatura (Celsius)', value='%.2f°C' % temp, delta="", border=True)

        pct_change = graph['AverageTemperature'][inf:sup].pct_change().mean()
        last_change = graph['AverageTemperature'][inf:sup].pct_change().iloc[-1]
        var = (pct_change - last_change)
        st.metric(label='Variação Percentual (Extremos)', value='%.2f%%' % pct_change, delta='%.2f%%' % var, border=True)

st.divider()

# Download dos Dados
data = st.download_button(
    label="Baixar Dados",
    data=graph.to_csv(index=False),
    type="primary",
    file_name="AverageTemperature.csv",
    mime="text/csv"
)
