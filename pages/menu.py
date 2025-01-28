import streamlit as st

st.title('Olá, @User!')

with open('./assets/src/menu.css') as f:
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
                <h1 style="margin-inline: 3.8%">Instruções</h1>
            </div>

                <p style="margin-inline: 5%">
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
                </p>    
            </div>
        </body>
    </html>
    """


)