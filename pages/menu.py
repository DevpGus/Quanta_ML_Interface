import streamlit as st

# Se o usuário não estiver autenticado, redirecione para login
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/account.py")

# Título da página
st.title(f'Bem vindo(a), {st.session_state.username}!')

# Link do CSS
with open('./assets/src/menu.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

### HTML da página de Menu
# O conteúdo pode ser personalizado conforme a necessidade.
# Altere as informações de acordo com o seu projeto na tag <p>.

st.html(
    """
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="./assets/src/menu.css" media="screen"/> 
        </head>

        <body>
            <div class="menu">
            <div style="display: flex; width: 100%; padding: 10px; border-radius: 10px;">
                <h1 style="margin-inline: 3.8%">Introdução</h1>
            </div>

                <p style="margin-inline: 5%">
                    Olá! Estamos muito felizes em apresentar a você, a plataforma personalizada que criamos especialmente para atender às necessidades e desafios do seu negócio. 
                    Sabemos que cada empresa é única, e foi pensando nisso que desenvolvemos uma solução sob medida para você, com foco em modelos de aprendizado de máquina e dashboards interativos, de forma simples e eficiente.
                    Essa plataforma foi feita para facilitar o uso de dados, tornando o processo de criação de modelos e análise de previsões algo prático e acessível, sem a necessidade de conhecimentos técnicos profundos. Nosso objetivo é ajudar a transformar seus dados em insights valiosos que podem orientar suas decisões, agilizar processos e contribuir para o sucesso da sua empresa.
                    Siga em frente e veja como nossa ferramenta pode ser a solução que você procurava. Continue lendo para entender como a plataforma foi pensada especialmente para você, usuário, e como ela pode resolver as suas necessidades de forma eficiente e personalizada.
                </p>    
            </div>
        </body>
    </html>
    """
)

# st.button("Vamos fazer previsões!", type="primary", on_click=lambda: st.switch_page("pages/forecast.py"))