import streamlit as st 
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Analysis on CSV")
st.header("Pls! Upload your CSV file for analysis")

data = st.file_uploader("Upload CSV:", type="csv")

query = st.text_input("Enter your query:")
button = st.button("Generate")

if button:
    answer = query_agent(data, query)
    st.write(answer)