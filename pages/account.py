import streamlit as st
import streamlit_authenticator as stauth
import bcrypt
import base64

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Função para converter a imagem em base64 para adicioná-la ao HTML.
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

with open('./assets/src/account.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Login
usernames = st.secrets["auth"]["usernames"] # Usuários cadastrados // Alterar em secrets.toml
passwords = st.secrets["auth"]['passwords'] # Senhas cadastradas // Alterar em secrets.toml
name = st.secrets["auth"]['names'] # Nomes cadastrados // Alterar em secrets.toml

# Verificação de nome e senha com bcrypt.
def verificar_senha(username, password):
    if username in usernames:
        index = usernames.index(username)
        if bcrypt.checkpw(password.encode(), passwords[index].encode()):
             return True
    return False 

# Construção da página de login e execução.
def login():
    st.title("Login")
    with st.container(border=True):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login", type="primary"):
            if verificar_senha(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.user_company = name[usernames.index(username)]
                st.toast("Login efetuado com sucesso! \nRedirecionando...", icon=":material/check_circle_outline:")
                st.switch_page("pages/menu.py")
            else:
                st.error("Usuário ou senha incorretos")
    return

# Verificação de autenticação
if not st.session_state.authenticated:
    login()
else:

    # Caminho da imagem local
    image_path_1 = "./assets/src/img/perfil.png"
    image_path_2 = "./assets/src/img/help.png"

    # Convertendo a imagem para base64
    image_base64 = get_base64_of_image(image_path_1)
    image_base64_2 = get_base64_of_image(image_path_2)


    st.write("Aqui você pode acessar informações privadas.")    

    # HTML da página de perfil: Aqui você pode alterar o conteúdo conforme sua necessidade.
    # Para modificar os links dos itens do menu, basta susbstituir as tags <a> com os links desejados (em href).
    # Para alterar as imagens, basta alterar o caminho das imagens em image_path_1 e image_path_2.

    with st.container(): 
        st.html(f""" 
            <head>
            </head>    
            <body>       
                <div class="login-header">
                    <div class="avatar">
                        <div style="text-align: center;">
                            <img src="data:image/png;base64,{image_base64}" width="50%">
                        </div>
                        <div class="perfil">
                            <p class="username">{st.session_state.username}</p>
                            <p class="company">{st.session_state.user_company}</p>
                        </div>
                    </div>
                    <div class="menu">
                        <div class="title">
                            <p>Detalhes</p>
                            <div class="line"></div> 
                        </div>
                        <div class="menu-item">
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Manual do Projeto 🗎</a>
                        </div>
                    </div>
                </div> 

                <div class="login-body">
                    <div class="help">
                        <br> 
                        <img src="data:image/png;base64,{image_base64_2}" width="50%">
                        <p>Precisa de Ajuda?<p>
                        <a href="mailto:gustavo.pereira@quanta.org.br">
                            Entre em contato conosco
                        </a> 
                    </div>
                    <div class="menu"> 
                        <div class="title">
                            <p>Documentos</p>
                            <div class="line"></div> 
                        </div> 
                        <div class="menu-item">
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Escopo 🗎</a>
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Contrato 🗎</a>
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Artigo 1 🗎</a>
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Artigo 2 🗎</a>
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Artigo 3 🗎</a>
                            <a href="https://docs.google.com/document/d/1FqZyyGEbWNEpDiJgS0Imw9ac5VjycikPGWY5OE8jaE8/edit?usp=sharing">Artigo 4 🗎</a> 
                        </div>
                    </div>
                </div>
                <br>
            </body>
        """)


