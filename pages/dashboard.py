import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Função de session_state dos gráficos.
def graphs():
    st.session_state['graphs'] = True

# Função para selecionar as métricas no dataset.
def total(df):
    filtro = (df['primary_type'] == filtro1) & (df['category'] == filtro2) & (df['generation'] == filtro3) 
    new_df = df.loc[filtro]

    return new_df['pokemon_id'].nunique()

def mean(df):
    if filtro1 == None or filtro2 == None or filtro3 == None:
        return 0

    filtro = (df['primary_type'] == filtro1) & (df['category'] == filtro2) & (df['generation'] == filtro3) 
    new_df = df.loc[filtro]

    return '%.2f' % (new_df['attack'].mean())

def maximum(df):
    if filtro1 == None or filtro2 == None or filtro3 == None:
        return 0

    filtro = (df['primary_type'] == filtro1) & (df['category'] == filtro2) & (df['generation'] == filtro3) 
    new_df = df.loc[filtro]

    return new_df['special_attack'].max()

# Link do CSS
with open('./assets/src/dashboard.css') as d:
    css = d.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Leitura dos datasets.
pokemon = pd.read_csv('./assets/forecasts/data/pokemon_dataset.csv')
df = pd.read_csv('./assets/forecasts/data/GlobalTemperatures.csv')

# Leitura do dataset de países.
df_countries = pd.read_csv('./assets/forecasts/data/GlobalLandTemperaturesByCountry.csv')
df_countries['time'] = pd.to_datetime(df_countries['dt'], errors='coerce')
df_countries = df_countries.dropna(subset=['time'])

# Estrutura da página
st.title('Análise Gráfica')
st.write('Descrevendo o propósito do modelo, por exemplo: "Este dashboard apresenta previsões baseadas em séries temporais, destacando tendências climáticas globais e regionais')

st.divider()

# Filtros de seleção
graph = df_countries
with st.container():
    c1, c2, c3 = st.columns(3, gap='medium')

    with c1:
        selected_country = st.selectbox('Selecione o País', ['Global'] + sorted(df_countries['Country'].unique().tolist()), key='country')
        
    if st.session_state.country == 'Global':
        graph = df_countries.copy()
    else:
        graph = df_countries[df_countries['Country'] == selected_country]
    graph['time'] = graph['time'].dt.date
    
    with c2:
        min_slider = int(graph['time'].min().year)
        max_slider = int(graph['time'].max().year)
        selected_interval = st.slider('Selecione o Período', min_value=min_slider, max_value=max_slider,  value=(min_slider, max_slider) , step=1, key='interval_time')
    
        inf = st.session_state['interval_time'][0]*12 - (min_slider*12)
        sup = st.session_state['interval_time'][1]*12 - (min_slider*12) 

    with c3:
        st.selectbox('Selecione o Tipo de Dado', ['Temperatura Média', 'Temperatura Máxima', 'Temperatura Mínima'], key='temp_type')
        if st.session_state.temp_type == 'Temperatura Média':
            temp = graph['AverageTemperature'][inf:sup].mean()
        elif st.session_state.temp_type == 'Temperatura Máxima':
            temp = graph['AverageTemperature'][inf:sup].max()
        else:
            temp = graph['AverageTemperature'][inf:sup].min()


# Intervalo de tempo

st.write(" ")

# Gráfico e Métricas
with st.container():
    c1, c2 = st.columns([3, 1], gap='medium')
    # graph = graph.dropna(subset=['AverageTemperature']) 

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
        ax.set_xticklabels(x_labels[::60], rotation=45)
        st.pyplot(fig)


    with c2:
        st.metric(label='Temperatura (Celsius)', value='%.2f°C' % temp, delta="", border=True)

        pct_change = graph['AverageTemperature'][inf:sup].pct_change().mean()
        last_change = graph['AverageTemperature'][inf:sup].pct_change().iloc[-1]
        var = (pct_change - last_change)
        st.metric(label='Variação Percentual', value='%.2f%%' % pct_change, delta='%.2f%%' % var, border=True)
st.divider()
st.button('Baixar Dados', type="primary", on_click=graphs)