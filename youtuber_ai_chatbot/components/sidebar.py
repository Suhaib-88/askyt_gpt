import streamlit as st
from components.faq import faq

def sidebar():
    with st.sidebar:
        st.markdown("# AskYT 🤖")
        st.markdown("---")
        st.markdown("# How to use?")
        st.markdown(
            "- Input the URL of the video you are interested in and ask your questions in the questions box "
            "- AskYT will use its advanced semantic search "
            "capabilities to analyze the video and generate accurate and helpful answer to your questions ")

        st.markdown("# About")
        st.markdown(
            "AskYT allows you to ask questions about YouTube videos. "
        )
        st.markdown("---")
        st.markdown("Made by [suhaib](https://github.com/Suhaib-88) and [Ayush](https://github.com/ayush31dec)")
        