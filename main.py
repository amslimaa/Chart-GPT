import os
import openai
import streamlit as st
from pandas import read_csv
import tempfile

import duckdb


openai.api_key = os.getenv("OPENAI_API_KEY")

if "comand_output" not in st.session_state:
    st.session_state["comand_output"] = ''

if "dfHead" not in st.session_state:
    st.session_state["dfHead"] = ''
    
if "question" not in st.session_state:
    st.session_state["question"] = ''

def Ask(): 
    prompt = "###Postgres SQL table, with their columns:\n#\n#"+  st.session_state["dfHead"] + "#\n" + "###"+ st.session_state["question"] + "\n SELECT"
    print(prompt)
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    print(response)
    expr = response.choices[0].text
    st.session_state["comand_output"] = expr


st.markdown("""
    ## ChartGPT
""")

arquivo = st.file_uploader("Selecione os arquivos CSV para mostrar", type=["csv"])
print((arquivo))
if arquivo:
    df = read_csv(arquivo)
    st.session_state["dfHead"] = df.head(0).to_string().split('\n')[1].replace('[','(').replace(']',')').replace(': ', '').replace("Columns", "df")
    st.dataframe(df)
    st.session_state["question"] = st.text_input("Faça uma pergunta sobre seus dados!", on_change=Ask())
    

if st.session_state["comand_output"]:
    st.write("SELECT "+ st.session_state["comand_output"])
    query = "SELECT " + st.session_state["comand_output"].replace('\n', ' ')
    print(query)
    result = duckdb.query(query).df()

    st.dataframe(result)