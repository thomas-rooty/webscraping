import os
import streamlit as st
from functions import collect_dentists
from db import DataBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Constants and Environment Variables
DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", "./chromedriver.exe")
BRAVE_PATH = os.getenv("BRAVE_BROWSER_PATH", "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")
DOCTOLIB_URL = "https://www.doctolib.fr/dentiste/"


# Functions
def initialize_browser():
  options = Options()
  options.binary_location = BRAVE_PATH
  options.add_argument("--incognito")
  # options.add_argument("--headless")  # Uncomment for headless mode
  service = Service(executable_path=DRIVER_PATH)
  return webdriver.Chrome(service=service, options=options)


def accept_cookies(browser):
  try:
    cookie_button = browser.find_element(By.ID, "didomi-notice-agree-button")
    cookie_button.click()
  except Exception as e:
    st.error("Error accepting cookies: " + str(e))


def store_dentists_in_db(dentists, city):
  database = DataBase()
  try:
    database.create_table('dentists', 'name', 'photo', 'address', 'city')
  except Exception as e:
    st.error("Database error: " + str(e))
    return

  for dentist in dentists:
    database.add_row('dentists', **dentist, city=city)


# Streamlit UI
def show_nearby_dentists():
  st.title("Trouver votre dentiste chez vous !")
  search_city = st.text_input("Enter a city name", placeholder="Paris, Marseille City, OM<PSG, ...")
  num_pages = st.slider("Combien de page à prendre en compte ?", 1, 10, 1)
  search_button = st.button("Lancer la recherche")

  if search_button:
    st.write(f"Recherche des dentistes à {search_city} sur {num_pages} pages...")
    url = DOCTOLIB_URL + search_city
    st.write(f"URL: {url}")

    browser = initialize_browser()
    try:
      browser.get(url)
      accept_cookies(browser)
      dentists = collect_dentists(browser, num_pages, search_city)
      store_dentists_in_db(dentists, search_city)
      st.write(dentists)
    except Exception as e:
      st.error("Error during scraping: " + str(e))
    finally:
      browser.quit()


show_nearby_dentists()
