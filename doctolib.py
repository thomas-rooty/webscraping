import streamlit as st
from functions import *
from db import DataBase
import sqlalchemy as db
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def show_nearby_dentists():
  st.title("Trouver votre dentiste chez vous !")

  # Search bar with an action button
  search_city = st.text_input("Pour des dents soinggg")
  search_button = st.button("Search")

  # If the search button is clicked
  if search_button:
    # Display search information
    st.write("Searching for dentists in " + search_city + "...")
    st.write("URL: https://www.doctolib.fr/dentiste/" + search_city)

    # Init webdriver
    driver_path = "./chromedriver.exe"
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("--incognito")
    #option.add_argument("--headless")

    # Specify service
    service = Service(executable_path=driver_path)

    # Create new Instance of Brave
    browser = webdriver.Chrome(service=service, options=option)

    # Open website
    browser.get("https://www.doctolib.fr/dentiste/" + search_city)

    # Agree with cookies
    browser.find_element(By.ID, "didomi-notice-agree-button").click()

    # Collect data
    nearby_dentists = collect_dentists(browser)
    st.write(nearby_dentists)

    # Store them in db, create table dentists if not exists
    database = DataBase()
    try:
      database.create_table('dentists', 'name', 'photo', 'addresse', 'city')
    except:
      pass

    # Populate DB with dentists
    for dentist in nearby_dentists:
      database.add_row('dentists', **dentist, city=search_city)

    # Close the browser
    browser.quit()
