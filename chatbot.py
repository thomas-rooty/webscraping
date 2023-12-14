import streamlit as st
from openai_class import *


def chatbot_page():
    textprocessor = TextProcessor()

    # Chatbot input
    text = st.text_input("Chatbot:", placeholder="Entrez votre commande...")

    if st.button("Envoyer"):
        try:
            if text.startswith('/'):
                command, *args = text[1:].split(' ', 1)
                args = args[0] if args else ""

                if command == 'translate':
                    result = textprocessor.openai_translate(args, "English")
                elif command == 'summary':
                    result = textprocessor.openai_text_summary(args)
                elif command == 'imagine':
                    result = textprocessor.openai_image(args)
                else:
                    result = 'Commande non reconnue'

                # Write result as text or as image
                if result.startswith('https://'):
                    st.image(result)
                else:
                    st.write(result)
            else:
                st.write('Veuillez entrer une commande valide.')
        except Exception as e:
            st.write(f"Une erreur s'est produite: {e}")
