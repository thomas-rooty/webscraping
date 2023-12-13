import streamlit as st


def show_animes():
    st.markdown(
        """
        <iframe src="http://localhost:8000/docs" width="100%" height="800px" style="border:none;"></iframe>
        """,
        unsafe_allow_html=True
    )

