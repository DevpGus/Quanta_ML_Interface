import os
from git import Repo
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

repo_url = f"https://{os.getenv('GITHUB_TOKEN')}@github.com/username/quanta_ml_interface.git"
Repo.clone_from(repo_url, 'local_path')


def wide_mode():
    st.set_page_config(layout="wide")
    return
wide_mode()

plt.style.use('_classic_test_patch')

# Menu
st.logo("./assets/src/img/logo_mini.png",
        size="large",
        link="https://quanta.org.br/",
        icon_image="./assets/src/img/logo_mini.png"
        )

pages = {
    "Minha Conta": [
        st.Page("./pages/account.py", title="Perfil", icon=":material/account_circle:", default=False),
    ],

    "Recursos": [
        st.Page("./pages/menu.py", title="Menu", icon=":material/home:", default=True),
        st.Page("./pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=False),
        st.Page("./pages/forecast.py", title="Fazer Previsão", icon=":material/search:", default=False),
        st.Page("./pages/add_data.py", title="Inserir Dados", icon=":material/insert_chart:", default=False),
        st.Page("./pages/info.py", title="Informações", icon=":material/info:", default=False),
    ],
}
pg = st.navigation(pages)
pg.run()


# Definir códigos-padrão // Filepaths
df = pd.read_csv('./assets/forecasts/data/pokemon_dataset.csv')
