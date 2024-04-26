import streamlit as st
from streamlit_chat import message

from langchain.chat_models.gigachat import GigaChat
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

#from ..settings import settings_init
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
st.markdown("# Подбор литературы и источников")
st.write("Умный поиск по популярному агрегатору англоязычных научных статей. Формулируйте запрос на английском")
st.sidebar.header("Подбор литературы на arxiv.org")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type keywords for your research"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        #responce = get_sources_links(settings_init.llm, settings_init.embeddings, settings_init.text_splitter, prompt)[0]
        responce = get_sources_links(settings_init["llm"], settings_init["embeddings"], settings_init["text_splitter"], prompt)
        bot_response = "Наиболее подходящие статьи по вашему запросу"
        for i, resp in enumerate(responce):
            bot_response += f"**{i+1}){resp['title']}**\n\n{resp['link']}\n\n"
            #expander = st.expander("Аннотация:")
            #expander.write(f"{resp['annotation']}")
            bot_response+=f"Аннотация:\n\n{resp['annotation']}"
            if resp['outer_links']:
                bot_response += f"\n\nДополнительные ссылки:\n\n{resp['outer_links']}\n\n"
            #st.write(f"GigaChatScienceBot: {bot_response}")
            bot_response += "\n\n"
            
        bot_response += "\n\n\n\n\n\n*Надеюсь, в списке выше вы найдете подходящие статьи. Если же эта подборка вам не подошла, попробуйте сформулировать запрос проще, как для поисковой системы*"
        message_placeholder.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})