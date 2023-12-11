from functions import *
import streamlit as st
import pandas as pd
import bs4
import pandas as pd

def show_capybar_app():
 st.title("Capybar'App")

 # Sidebar with links to other pages
 st.sidebar.title("Capybar'App")

 # Text form
 search_param = st.text_input('Rechercher sur BDM', 'IA, Adobe, Tech, Dev, ...')

 # Number form
 page_nb = str(st.number_input('Page', min_value=1, max_value=100, value=1))

 # Search articles
 if st.button('Rechercher'):
   # Generate search result
   search_result = search_on_bdm(search_param, page_nb)
   st.write('Status: ', search_result.status_code)
   st.write('URL: ', search_result.url)

   # Datafrane
   soup = bs4.BeautifulSoup(search_result.text)
   json = build_json(soup)
   df = pd.DataFrame.from_dict(json, orient='index')
   st.write(df)
   st.write('Nombre d\'articles trouvés: ', len(df.index))

   # Download CSV
   st.markdown(download_csv(df), unsafe_allow_html=True)

   # Save dataframe as json in the server
   df.to_json('dataframe.json')
