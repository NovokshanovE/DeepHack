# Перевод визуальных элементов в LaTEX
import streamlit as st
from streamlit_chat import message

from langchain.chat_models.gigachat import GigaChat
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

from ml.sources import get_sources_links


credentials = 'Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OmQ4MWMxZGZiLTFmNGYtNDk5NS05OGQzLTBiMzYyYWJmNjk3OA=='
llm = GigaChat(credentials=credentials, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")
embeddings = GigaChatEmbeddings(credentials=credentials, verify_ssl_certs=False, scope="GIGACHAT_API_CORP")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50,
)
settings_init =  {"llm": llm, "embeddings": embeddings, "text_splitter": text_splitter}


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style.css")
st.markdown("# Перевод визуальных элементов в LaTEX")
st.sidebar.header("Перевод визуальных элементов в LaTEX")

st.markdown("## Еще разрабатывается...")
st.markdown("\n\n\n\n")
st.markdown("## Но скоро появится!")

# uploaded_file = st.file_uploader("Загрузите PDF файл", type=['pdf']) # или укажите ссылку на него:
# uploaded_img = st.file_uploader("Загрузите изображение элемента (например, график)", type=['jpeg', 'jpg', 'png']) # или укажите ссылку на него:
# submit_button = st.button("Отправить")
# if submit_button and (uploaded_file is not None or uploaded_img is not None):
#     st.write("Текстовый ответ после суммаризации")