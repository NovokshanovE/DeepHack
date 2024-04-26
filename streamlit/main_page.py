import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
def run():
    local_css("style.css")
    st.set_page_config(
        page_title="Science GigaChat Bot",
        page_icon="👋",
    )

    st.write("# Welcome to Science GigaChat Bot! 👋")
    st.write("It can:\n* Find relevant papers for your research\n* Summarize the paper and show it's visual content")

    st.sidebar.success("Select a mode above")
    
    
if __name__ == "__main__":
    run()
