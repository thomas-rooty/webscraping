import streamlit as st
import pandas as pd
import json


def show_beautiful():
  # Sample JSON data (replace with your JSON data)
  data = pd.read_json('dataframe.json').to_json(orient='records')

  # Parse the JSON into a DataFrame
  data_dict = json.loads(data)
  df = pd.DataFrame(data_dict)

  # Streamlit page layout
  st.title("Latest Tech Articles")

  for index, row in df.iterrows():
    st.subheader(row['name'])
    st.image(row['img'], width=100)
    st.write(f"Catégorie: {row['category']}")
    st.write(f"Publié le: {row['date']}")
    st.markdown(f"[Voir l'article original]({row['link']})", unsafe_allow_html=True)
    st.write("---")  # Separator line
