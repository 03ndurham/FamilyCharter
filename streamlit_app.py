import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([st.Page("charter.py", title="Charter"), 
                    st.Page("changes.py", title="Proposed Changes"),
                    st.Page("agenda.py", title="Agenda"),
                    st.Page("minutes.py", title="Meeting Minutes")])
pg.run()