import streamlit as st
from style import apply_style, cta_button

st.set_page_config(page_title="Husnain", page_icon="🔷", layout="centered")
apply_style()

st.markdown("""
<div style="display:flex; flex-direction:column; align-items:center; text-align:center; padding: 40px 0 20px 0;">
    <div style="width:64px; height:64px; border-radius:14px; background:#3B5BDB; display:flex; align-items:center; justify-content:center; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:24px; color:#FAFAF8; margin-bottom:24px;">MH</div>
    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:40px; color:#1A1A1A; margin-bottom:12px;">Husnain</div>
    <div style="font-family:'Inter',sans-serif; font-size:18px; color:#55554F; max-width:480px; line-height:1.5;">I build RAG pipelines that connect to real data, not demos — with the numbers to prove it.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="proof-number" style="text-align:center;">A model I built beat a hand-written rule 74% → 24% on real search data.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<span class="case-tag">Work</span>', unsafe_allow_html=True)
    st.markdown("**FlyRank ML internship**")
    st.caption("A ranked review queue that beats a hand-written rule 3x on real search data.")
with col2:
    st.markdown('<span class="case-tag">Work</span>', unsafe_allow_html=True)
    st.markdown("**RAG chatbot**")
    st.caption("A deployed retrieval pipeline, built end-to-end to actually understand RAG.")

st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
cta_button()
st.markdown("</div>", unsafe_allow_html=True)

st.caption("Use the sidebar to see the full work, about me, and how to reach me.")
