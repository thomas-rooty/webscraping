from functions import *
import streamlit as st
import bs4
import pandas as pd


def show_capybar_app():
  st.markdown("<h1 style='text-align: center;'>Cliquez sur le Capybara pour voir mon profil</h1>", unsafe_allow_html=True)

  # Sidebar with links to other pages
  st.sidebar.title("Capybar'App")

  # Banner image
  st.markdown(
    """
    <div style='text-align: center;'>
      <a href='https://github.com/thomas-rooty' target='_blank'>
        <img src='https://i.imgur.com/TWU2hzI.png' alt='Capybar'App' style='width: 25%;'>
      </a>
    </div>
    """,
    unsafe_allow_html=True
  )

  # Text form
  search_param = st.text_input('Rechercher sur BDM', placeholder='IA, Tech, Adobe, ...')

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
    st.download_button(
      label="Télécharger les résultats au format CSV",
      data=df.to_csv().encode('utf-8'),
      file_name='dataframe.csv',
      mime='text/csv',
    )

    # Save dataframe as json in the server
    df.to_json('dataframe.json')
