import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Capybar'App",
  page_icon="🦫",
  layout="wide",
)

st.title("Capybar'App")

df = pd.read_json("bdm.json")

if st.checkbox("Afficher la base de données"):
  st.write(df)
