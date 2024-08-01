import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import json
import re

st.title("Car Terms Search")
conn = sqlite3.connect('carterms.db')
cursor = conn.cursor()



@st.cache_data(show_spinner =True)
def load_data():
    # Read the Excel file
    df = pd.read_sql_query("SELECT * FROM terms", conn)
    #df = pd.DataFrame({ "Japanese": json_object.keys(), 'English': json_object.values()})
    return df
df = load_data()
#st.dataframe(df)
    
En={}
Jp={}
df.columns = ['Jp', 'En']
toggle_label = (
    "English to Japanese"
    if st.session_state.get("my_toggle", False)
    else "Japanese to English"
)
toggle_value = st.session_state.get("my_toggle", False)


for i in range(len(df)):
        x = df.iloc[i,0]
        y = df.iloc[i,1]
        En[x] = y
        Jp[y] = x


on = st.toggle(toggle_label, value = toggle_value,key="my_toggle")
if on == True:
    
        lang = "En"
        print_lang = 0
        dic = En
else:
        Jp[x] = y
        lang = "Jp"
        print_lang = 1
        dic = Jp

test_values = dic.values()

option = st.selectbox(
    "Term Search",
    test_values,index=None,
    placeholder="<search here>", key = "tim"
)
try:
    escaped_option = re.escape(option)
   
    pattern = f"({escaped_option})"
    
    filtered_rows = df[df[lang].str.contains(pattern, case=False, na=False)]
    #st.write(filtered_rows)
    for i in df.iloc[filtered_rows.index,print_lang]:
        st.write(i)
except:
    st.write("No Result")