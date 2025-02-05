import streamlit as st

# Se o usuário não estiver autenticado, redirecione para login
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/account.py")

st.title('Informações')

with open('./assets/src/info.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.html(
    """
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="./assets/src/menu.css" media="screen"/> 
        </head>

        <body>
            <div class="menu">
            <div style="display: flex; width: 100%; padding: 10px; border-radius: 10px;">
                <h1 style="margin-inline: 3.8%">Sobre o modelo</h1>
            </div>

                <p style="margin-inline: 5%">                    
                    📊 Bem-vindo à Análise de Séries Temporais! Aqui, você pode explorar dados ao longo do tempo, identificar padrões e prever tendências futuras de forma intuitiva. Séries Temporais são dados registrados em intervalos regulares, amplamente usados em setores como vendas, finanças e logística. Nossa ferramenta permite que você carregue seus dados, visualize gráficos interativos e crie previsões com modelos de Machine Learning sem precisar de conhecimentos avançados. Basta fazer o upload do seu arquivo, explorar os insights gerados e ajustar parâmetros para obter análises mais precisas. Tudo de forma simples e acessível! 🚀
                </p>    
            </div>

            <div class="extra">
                <a class="link" href="https://www.quanta.org.br/">
                    <div class="text">
                        <p class="link">Feedback</p>
                    </div>
                </a>

                <a class="link" href="https://www.quanta.org.br/">
                    <div class="text">
                        <p class="link">Quanta</p>
                    </div>
                </a>

                <a class="link" href="https://www.quanta.org.br/">
                    <div class="text">
                        <p class="link">Reporte Bugs</p>
                    </div>
                </a>
                </div>
        </body>
    </html>
    """


)