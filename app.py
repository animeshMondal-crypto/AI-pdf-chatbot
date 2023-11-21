import streamlit as st

def main():
    st.set_page_config(page_title="Chat With PDF", page_icon=":books:")

    st.header("Chat PDF :books:")
    st.text_input("Ask a question about your document:")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your PDF's Here")
        st.button("Process")



if __name__ == '__main__':
    main()
