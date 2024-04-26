import streamlit as st

from settings import settings
from ml.sources import get_sources_links


def chat_bot():
    st.title("Чат с ботом")

    user_input = ""

    while True:
        user_input = st.text_input("Введите ваше сообщение (для завершения чата введите 'завершить'):", key=user_input)

        if user_input:
            #if user_input.lower() == 'завершить':
            #    break

            st.write(f"Вы: {user_input}")

            responce = get_sources_links(settings["llm"], settings["embeddings"], settings["text_splitter"], user_input)[0]
            
            bot_response = f"<b>{responce['title']}</b>\n{responce['link']}\n"
            expander = st.expander("Аннотация:")
            expander.write(f"{responce['annotation']}")
            if responce['outer_links']:
                bot_response += f"Дополнительные ссылки:\n{responce['outer_links']}\n"
            st.write(f"GigaChatScienceBot: {bot_response}")

st.set_page_config(page_title="Animation Demo", page_icon="📹")
st.markdown("# Подбор литературы и источников")
st.sidebar.header("Подбор литературы")
