import streamlit as st
from openai_class import *


def show_ai():
    textprocessor = TextProcessor()

    # Translation
    language = st.text_input("Language:", placeholder="English, Spanish, German, ...")
    text = st.text_input("Texte à traduire de Francais à" + language + ":", placeholder="Bonjour, je m'appelle Capybara.")

    if st.button("Traduire"):
        st.write(textprocessor.openai_translate(text, language))

    # Separator
    st.markdown("---")

    # Summary
    text = st.text_input("Texte à résumer:", placeholder="Bonjour, je m'appelle Capybara.")

    if st.button("Résumer"):
        st.write(textprocessor.openai_text_summary(text))

    # Separator
    st.markdown("---")

    # Text generator
    theme = st.text_input("Thème:", placeholder="Tech, IA, ...")
    text = st.text_input("Texte à générer:", placeholder="Bonjour, je m'appelle Capybara.")

    if st.button("Générer"):
        st.write(textprocessor.openai_text_generator(theme, text))

    # Separator
    st.markdown("---")

    # Codex
    code = st.text_input("Code:", placeholder="print('Hello World')")

    if st.button("Codex"):
        st.write(textprocessor.openai_codex(code))

    # Separator
    st.markdown("---")

    # Image generation
    image_prompt = st.text_input("Image à générer:", placeholder="Un gros capybara.")

    if st.button("Générer l'image"):
        st.write(textprocessor.openai_image(image_prompt))
