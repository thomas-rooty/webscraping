import streamlit as st
from functions import *
import pandas as pd
import bs4

st.set_page_config(
  page_title="Capybar'App",
  page_icon="🦫",
  layout="wide",
)

st.title("Capybar'App")

# Text form
search_param = st.text_input('Rechercher sur BDM', 'IA, Adobe, Tech, Dev, ...')

# Search articles
if st.button('Search'):
  # Generate search result
  search_result = search_on_bdm(search_param, '1')
  st.write('Status code: ', search_result.status_code)
  st.write('URL: ', search_result.url)

  # Datafrane
  soup = bs4.BeautifulSoup(search_result.text)
  json = build_json(soup)
  df = pd.DataFrame.from_dict(json, orient='index')
  st.write(df)
