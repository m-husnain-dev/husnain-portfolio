import streamlit as st

st.set_page_config(page_title="Husnain", page_icon="🔷", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500&display=swap');

.stApp {
    background-color: #FAFAF8;
}

.hero-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 70vh;
    text-align: center;
}

.logo-mark {
    width: 64px;
    height: 64px;
    border-radius: 14px;
    background: #3B5BDB;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 24px;
    color: #FAFAF8;
    margin-bottom: 24px;
}

.hero-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 40px;
    color: #1A1A1A;
    margin-bottom: 12px;
}

.hero-claim {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-size: 18px;
    color: #55554F;
    max-width: 480px;
    line-height: 1.5;
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>

<div class="hero-wrap">
    <div class="logo-mark">MH</div>
    <div class="hero-name">Husnain</div>
    <div class="hero-claim">I build RAG pipelines that connect to real data, not demos — with the numbers to prove it.</div>
</div>
""", unsafe_allow_html=True)