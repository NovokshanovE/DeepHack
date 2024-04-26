import streamlit as st


def run():
    st.set_page_config(
        page_title="Science GigaChat Bot",
        page_icon="👋",
    )

    st.write("# Welcome to Science GigaChat Bot! 👋")
    st.write("It can:\n* Find relevant papers for your research\n* Summarize the paper and show it's visual content\n* Format the paper for the list of references \n* Generate LaTex code by images and tables")

    st.sidebar.success("Select a mode above")
    
    
if __name__ == "__main__":
    run()
