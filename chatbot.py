import streamlit as st
from openai_class import *


def chatbot_page():
    textprocessor = TextProcessor()

    # Chatbot input
    text = st.text_input("Chatbot:", placeholder="Entrez votre commande...")

    if st.button("Envoyer"):
        try:
            if text.startswith('/'):
                parts = text[1:].split(' ', 2)  # Split into command and arguments
                command = parts[0]
                target_language = parts[1] if len(parts) > 1 else "English"  # Default to English
                theme = parts[1] if len(parts) > 1 else None
                args = parts[2] if len(parts) > 2 else parts[1] if len(parts) > 1 else None

                if command == 'translate':
                    result = textprocessor.openai_translate(args, target_language)
                elif command == 'summary':
                    result = textprocessor.openai_text_summary(args)
                elif command == 'imagine':
                    result = textprocessor.openai_image(args)
                elif command == 'actu':
                    if theme:
                        result = textprocessor.openai_text_generator(theme, args)
                    else:
                        result = "Veuillez spécifier un thème pour la commande /actu."
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
