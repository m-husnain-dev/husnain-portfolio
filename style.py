import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500&display=swap');

    .stApp { background-color: #FAFAF8; }

    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: #1A1A1A !important; }
    p, li { font-family: 'Inter', sans-serif; }

    .claim-banner {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 22px;
        color: #1A1A1A;
        background: #EEF1FC;
        border-left: 4px solid #3B5BDB;
        border-radius: 6px;
        padding: 18px 22px;
        margin: 18px 0 28px 0;
    }

    .proof-number {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 15px;
        color: #3B5BDB;
        margin-bottom: 24px;
    }

    .case-tag {
        display: inline-block; background: #E1F5EE; color: #085041;
        font-size: 12px; font-weight: 500; padding: 3px 10px; border-radius: 5px; margin-bottom: 8px;
    }

    .cta-button {
        display: inline-block;
        background: #FF6B4A;
        color: #FAFAF8 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 15px;
        padding: 10px 22px;
        border-radius: 8px;
        text-decoration: none !important;
        margin-top: 12px;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


def cta_button(label="Book a call →", href="mailto:m.husnain0405@gmail.com?subject=Let's talk"):
    st.markdown(f'<a class="cta-button" href="{href}">{label}</a>', unsafe_allow_html=True)
