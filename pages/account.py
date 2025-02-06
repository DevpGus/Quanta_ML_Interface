import streamlit as st
import bcrypt

with open('./assets/src/account.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Login
USERS_DB = {
    "admin": [bcrypt.hashpw("123".encode(), bcrypt.gensalt()), "Quanta Júnior"],
    "user": [bcrypt.hashpw("user123".encode(), bcrypt.gensalt()), "Quanta Júnior"],
}

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def verificar_senha(username, password):
    if username in USERS_DB:
        if bcrypt.checkpw(password.encode(), USERS_DB[username][0]):
            return True
    return False

def login():
    st.title("Login")
    with st.container(border=True):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login", type="primary"):
            if verificar_senha(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.user_company = USERS_DB[username][1]
                st.success("Login efetuado com sucesso! Redirecionando...")
                st.switch_page("pages/menu.py")
            else:
                st.error("Usuário ou senha incorretos")
    return

if not st.session_state.authenticated:
    login()
else:

    st.success(f"Logado como {st.session_state.username}")
    st.write("Aqui você pode acessar informações privadas.")    

    with st.container():
        c1, c2 = st.columns([1,4], border=True)
        with c1:
            st.image('./assets/src/img/perfil.png')
            st.html(f"""
                <div class="perfil">
                    <p class="username">{st.session_state.username}</p>
                    <p class="company">{st.session_state.user_company}</p>
                </div>
                <br>
            """)
        with c2:
            col1, col2, col3, col4 = st.columns([0.7,1,1,3.7])
            with col1:
                st.button("Perfil", key="perfil", type="secondary", use_container_width=True)
            with col2:
                st.button("Empresa", key="empresa", type="secondary", use_container_width=True)
            with col3:
                st.button("Documentos", key="documentos", type="secondary", use_container_width=True)
            

