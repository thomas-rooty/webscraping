import streamlit as st
from db import DataBase


def get_dentists_from_db(city_filter=None):
  database = DataBase()
  try:
    database.read_table('dentists')
  except Exception as e:
    st.error("Database error: " + str(e))
    return

  dentists = database.select_table('dentists')

  if city_filter:
    dentists = [dentist for dentist in dentists if dentist['city'].lower() == city_filter.lower()]

  return dentists


# Streamlit UI
def show_dentists_beautiful():
  st.title("Trouver votre dentiste chez vous !")

  city_filter = st.text_input("Entrez la ville pour filtrer les dentistes :",
                              placeholder="Paris, Marseille, OM<PSG, ...")

  dentists = get_dentists_from_db(city_filter)

  # Use markdown to display the dentist beautifully
  for dentist in dentists:
    st.markdown(f"""
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <img src="{dentist['photo']}" alt="{dentist['name']}" style="width: 100px; height: 100px; border-radius: 50%; margin-right: 1rem;" />
            <div>
                <h3 style="margin: 0;">{dentist['name']}</h3>
                <p style="margin: 0;">{dentist['addresse']}</p>
                <p style="margin: 0;">{dentist['city']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


show_dentists_beautiful()
