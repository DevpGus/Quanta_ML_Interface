# Interface de Machine Learning da Quanta Júnior.
Esta é uma aplicação Streamlit com o objetivo de padronizar/facilitar o desenvolvimento de interfaces pelo time de projetos da Quanta Júnior.
Para acessar a página e visualizar o projeto, acesse: https://quanta-std-interface.streamlit.app/.

# Estrutura do Projeto.
Este arquivo está estruturado da seguinte forma:
```bash
Quanta_ML_Interface/
|   .gitignore
|   .gitattribbutes     # Usado pelo Git LFS (Large File Storage)
│   st_app.py           # Arquivo principal da aplicação Streamlit
│   requirements.txt    # Dependências do projeto
│   README.md           # Este arquivo
│
└───assets/             # Notebooks python, imagens, arquivos de estilização (CSS) e Datasets
└───pages/              # Páginas adicionais da aplicação Streamlit
└───.streamlit/         # Arquivo com as personalizações da página

```

## Como utilizar?

1. **Clone o repositório:**  
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```
2. **Instale as dependências**
```bash
pip install -r requirements.txt
```
3. **Execute a aplicação**
```bash
streamlit run st_app.py
````
Lembre-se de adicionar um arquivo secrets.toml em .streamlit, com as configurações abaixo para hospedar localmente.
```bash
[auth]
usernames = ["Usuário 1", "Usuario 2"]
passwords = ["Senha hashada 1", "Senha hashada 2"]
names = ["Empresa 1", "Empresa 2"]
```
OBS: Utilize o *bcrypt* para gerar senhas hashadas e as insira no campo indicado.


