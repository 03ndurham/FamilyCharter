import streamlit as st

st.title("Cruikshank Family Trust")

pg = st.navigation([st.Page("charter-text.py", title="Charter"), st.Page("ammendments.py", title="Proposed Ammendments")])
pg.run()