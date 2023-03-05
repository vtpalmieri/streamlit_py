import streamlit as st
from PIL import Image
from json import loads
from pandas import read_csv
from pandas import read_excel
# from spacy import load
# from streamlit_ace import st_ace, THEMES, LANGUAGES

st.title("Hello Internet")
st.write("texto")
st.markdown(''' Olá!!! ''')

st.markdown('''**Login:**''')
st.text_input('E-mail')
st.text_input('Senha', type='password')
st.date_input('Data')
st.time_input('Hora')
st.number_input('Número', min_value= 0, max_value= 100)
st.color_picker('Cor')
st.button('Submit', type='primary')


st.image("https://placekitten.com/400/500")

st.markdown('''#Exibidor de arquivos:''')

arquivo = st.file_uploader('Upload', type=['jpg', 'png', 'py', 'wav', 'csv', 'json', 'mp4'])

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'image', _:
            st.image(arquivo)
        case 'video', _:
            st.video(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
else:
    st.error('Nenhum arquivo carregado.')


    
# nlp = load('pt_core_news_lg')

# bar = st.sidebar

# categoria = bar.selectbox('Categoria', ['Exportivo', 'Econômico'])

# text = st.text_area('Texto:')

# doc = nlp(text)

# if text and categoria == 'Eportivo':
#    filtro = bar.multiselect(
#        'Sub-categoria',
#        ['Importado', 'Nacional', 'Exclusivo']
#        )


# st.title('Editor de texto:')

# c1, c2 = st.columns([3, 1])
# with c1:
#     content = st_ace(
#         theme=c2.selectbox('Tema',options=THEMES),
#         language=c2.selectbox('Linguagem',options=LANGUAGES)
#     )
