import streamlit as st

pg = st.navigation([st.Page("charter-text.py", title="Charter"), st.Page("ammendments.py", title="Proposed Ammendments")])
pg.run()