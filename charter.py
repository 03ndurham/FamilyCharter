import streamlit as st

pg = st.navigation([st.Page("charter-text.py"), st.Page("ammendments.py")])
pg.run()