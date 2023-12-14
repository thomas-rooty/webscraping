from webscraping import *
from beautiful import *
from doctolib import *
from doctolib_beautiful import *
from myanimelist import *
from openai_page import *
from chatbot import *

st.set_page_config(page_title="Capybar'App", page_icon="🦫", layout="wide")

PAGES = {
  "BDM Scraping": show_capybar_app,
  "Beautiful Scraping": show_beautiful,
  "Dentistes les plus proches": show_nearby_dentists,
  "Liste des dentistes (DB)": show_dentists_beautiful,
  "Liste des animés (DB)": show_animes,
  "OpenAI": show_ai,
  'Chatbot': chatbot_page,
}

st.sidebar.title("")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()

# /summary J'aime les capybaras alors que j'ai 22 ans, j'aime egalement beaucoup les pommes de terre
