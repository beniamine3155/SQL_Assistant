import streamlit as st
import pandas as pd

# from dotenv import load_dotenv
# load_dotenv()

st.set_page_config(page_title="SQL Assistant", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



# Chat interface
st.title("Chat With Your Current Database")
st.markdown("Ask in text. This sql assistant will convert it to SQL and run it on your current DB.")

# Display chat history
for role, content in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    elif role == "assistant":
        with st.chat_message("assistant"):
            st.code(content, language="sql")
    elif role == "error":
        with st.chat_message("assistant"):
            st.error(content)
    elif role == "result":
        result, columns = content
        with st.chat_message("assistant"):
            if result:
                df = pd.DataFrame(result, columns=columns)
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("No results found.")
