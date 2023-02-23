import streamlit as st

GPT_RAW_TXT_FILENAME="chatgpt_raw_copy_from_chat_openai_com.txt"

with open(GPT_RAW_TXT_FILENAME,"r") as gpt_raw_file:
    gpt_raw=gpt_raw_file.readlines()

for gpt_line in gpt_raw:
    if gpt_line.startswith("$"):
        gpt_eqt=gpt_line.split("$")[1]
        st.latex(gpt_eqt)
    else:
        st.write(gpt_line)