import streamlit as st

from langchain.chat_models.gigachat import GigaChat
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

from ml.summarization import get_summarization


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
st.markdown("# Суммаризация статьи")
st.sidebar.header("Суммаризация статьи")

st.write("Для суммаризации необходим .pdf файл")
uploaded_file = st.file_uploader("Загрузите PDF файл", type=['pdf']) # или укажите ссылку на него:
print("uploaded_file",type(uploaded_file))
submit_button = st.button("Отправить")
if submit_button and uploaded_file is not None:
    file_path = "input.pdf"

    # Write the contents of the uploaded file to the specified file path
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    print(uploaded_file.__dict__)
    st.markdown("# Краткое содержание документа:")
    st.markdown("\n\n\n\n")
    
    st.markdown(get_summarization(file_path, settings_init["llm"])["text"])