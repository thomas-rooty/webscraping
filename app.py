from webscraping import *
from beautiful import *

st.set_page_config(page_title="Capybar'App", page_icon="🦫", layout="wide")

PAGES = {
  "BDM Scraping": show_capybar_app,
  "Beautiful Scraping": show_beautiful
}

st.sidebar.title("")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()
