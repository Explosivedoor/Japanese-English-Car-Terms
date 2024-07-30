import streamlit as st
import pandas as pd
import numpy as np





@st.cache_data(show_spinner =True)
def load_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    return df
df = load_data("D:\\Downloads\\Auction-Sheet-Terms.xlsx")

columns_to_drop = range(0, 3)
rows_to_drop = range(0,17)
df.drop(df.columns[columns_to_drop], axis=1, inplace=True)
df.drop(rows_to_drop, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
En={}
Jp={}
df.columns = ['Jp', 'En', 'Mg', 'Sp','Cat']

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

#st.write(test2) 
#st.dataframe(df)

#st.write(df.iloc[0,0]) 

test_key = dic.keys()
test_values = dic.values()

option = st.selectbox(
    "Term Search",
    test_values,index=None,
    placeholder="<search here>", key = "tim"
)
try:
    filtered_rows = df[df[lang].str.contains(option, case=False, na=False)]
    #st.write(filtered_rows)
    for i in df.iloc[filtered_rows.index,print_lang]:
        st.write(i)
except:
    st.write("No Result")


