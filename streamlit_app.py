import streamlit as st

st.markdown(
    """
    <meta name="robots" content="noindex, nofollow">
    """,
    unsafe_allow_html=True
)

st.set_page_config(layout="wide")

pg = st.navigation([st.Page("charter.py", title="Charter"), 
                    st.Page("changes.py", title="Proposed Changes"),
                    st.Page("agenda.py", title="Agenda"),
                    st.Page("minutes.py", title="Meeting Minutes")])
pg.run()