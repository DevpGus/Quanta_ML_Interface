import streamlit as st
import bcrypt

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
        c1, c2 = st.columns([1,3], border=True)
        with c1:
            st.image("./assets/src/img/perfil.png", use_container_width=True)
            st.markdown(f"***{st.session_state.username}***")
            st.markdown(f"{st.session_state.user_company}")
