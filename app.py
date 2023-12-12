from webscraping import *
from beautiful import *
from doctolib import *

st.set_page_config(page_title="Capybar'App", page_icon="🦫", layout="wide")

PAGES = {
  "BDM Scraping": show_capybar_app,
  "Beautiful Scraping": show_beautiful,
  "Dentistes les plus proches": show_nearby_dentists
}

st.sidebar.title("")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()
