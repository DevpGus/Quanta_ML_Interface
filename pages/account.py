import streamlit as st
import streamlit_authenticator as stauth
import bcrypt
import base64

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

with open('./assets/src/account.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Login
usernames = st.secrets["auth"]["usernames"]
passwords = st.secrets["auth"]['passwords'] 
name = st.secrets["auth"]['names']

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
                st.success("Login efetuado com sucesso! Redirecionando...")
                st.switch_page("pages/menu.py")
            else:
                st.error("Usuário ou senha incorretos")
    return


# USERS_DB = {
#     "admin": [bcrypt.hashpw("123".encode(), bcrypt.gensalt()), "Quanta Júnior"],
#     "user": [bcrypt.hashpw("user123".encode(), bcrypt.gensalt()), "Quanta Júnior"],
# }

# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False

# def verificar_senha(username, password):
#     if username in USERS_DB:
#         if bcrypt.checkpw(password.encode(), USERS_DB[username][0]):
#             return True
#     return False

# def login():
#     st.title("Login")
#     with st.container(border=True):
#         username = st.text_input("Usuário")
#         password = st.text_input("Senha", type="password")

#         if st.button("Login", type="primary"):
#             if verificar_senha(username, password):
#                 st.session_state.authenticated = True
#                 st.session_state.username = username
#                 st.session_state.user_company = USERS_DB[username][1]
#                 st.success("Login efetuado com sucesso! Redirecionando...")
#                 st.switch_page("pages/menu.py")
#             else:
#                 st.error("Usuário ou senha incorretos")
#     return

if not st.session_state.authenticated:
    login()
else:


# Caminho da imagem local
    image_path_1 = "./assets/src/img/perfil.png"
    image_path_2 = "./assets/src/img/help.png"

# Convertendo a imagem para base64
    image_base64 = get_base64_of_image(image_path_1)
    image_base64_2 = get_base64_of_image(image_path_2)


    # st.success(f"Logado como {st.session_state.username}")
    st.write("Aqui você pode acessar informações privadas.")    

    with st.container():
         
            # st.image('./assets/src/img/perfil.png', width=100)
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
            # st.button("Perfil", key="perfil", type="secondary", use_container_width=True)
            # st.button("Empresa", key="empresa", type="secondary", use_container_width=True)
            # st.button("Docs", key="documentos", type="secondary", use_container_width=True)


