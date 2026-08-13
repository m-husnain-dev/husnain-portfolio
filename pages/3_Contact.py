import streamlit as st
from style import apply_style, cta_button

st.set_page_config(page_title="Contact — Husnain", page_icon="🔷", layout="centered")
apply_style()

st.title("Contact")

st.markdown('<div class="claim-banner">I build RAG pipelines that connect to real data, not demos — with the numbers to prove it.</div>', unsafe_allow_html=True)

st.write("If you're building something and need someone who can take a real data problem and ship a working pipeline — not just a demo — the fastest way to talk is a short call.")

cta_button(label="Book a call →")

st.caption("Or reach me directly: m.husnain0405@gmail.com")
