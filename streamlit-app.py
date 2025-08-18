import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([st.Page("charter-text.py", title="Charter"), st.Page("ammendments.py", title="Proposed Ammendments")])
pg.run()