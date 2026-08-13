import streamlit as st
from style import apply_style, cta_button

st.set_page_config(page_title="About — Husnain", page_icon="🔷", layout="centered")
apply_style()

st.title("About")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/about_photo.png", width=180)
with col2:
    st.markdown("""
    I'm Husnain — a BS Artificial Intelligence student at NTU Faisalabad, currently interning
    on FlyRank's ML track and building backend systems in Go and Python on the side.

    I like taking messy real data and turning it into something that actually beats the
    simple version. Currently figuring out my next move toward an AI/ML engineering role.
    """)

st.markdown('<div class="claim-banner">Everything on this site comes back to one thing: I build systems that connect to real data and prove it — not demos.</div>', unsafe_allow_html=True)

cta_button()
