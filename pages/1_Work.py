import streamlit as st
from style import apply_style, cta_button

st.set_page_config(page_title="Work — Husnain", page_icon="🔷", layout="centered")
apply_style()

st.title("Work")

# --- Case 1: FlyRank internship (leads) ---
st.markdown('<span class="case-tag">Case 1</span>', unsafe_allow_html=True)
st.header("FlyRank ML Internship — Content Refresh Scoring")

st.image("assets/ml_screenshot.png", caption="Real notebook output: eligible/declining feature build on the starter dataset.")

st.markdown("**The problem**")
st.write("FlyRank had a simple if-else rule deciding which content pages to review first for a refresh. When I checked it against real outcomes, it only got about 24% of its top picks right. Reviewers were spending limited time on pages that weren't actually the priority.")

st.markdown("**What I did**")
st.write("Before touching a model, I went through the data looking for traps — one caught early: the label I'd be predicting (whether a page was declining) was built from the same signal that looked like a tempting feature. Using it as both would let a model just copy its own answer, so I ruled it out as a feature on principle. I built the pipeline properly: baseline rule first, then compared Logistic Regression, a Decision Tree, and a Random Forest, validated with client holdout so results couldn't be inflated by the model memorizing clients it had already seen.")

st.markdown("**What came of it**")
st.write("A full pipeline, baseline to trained model to a ranked review queue. On the metric that actually matters (not a circular one), the baseline itself turned out to beat both models on this slice — a real, honest finding I wrote up rather than hid, because a metric that flatters the model isn't worth trusting.")

cta_button()

st.markdown("---")

# --- Case 2: RAG chatbot ---
st.markdown('<span class="case-tag">Case 2</span>', unsafe_allow_html=True)
st.header("Personal RAG Chatbot")

st.image("assets/rag_screenshot.png", caption="Live app: husnain-ai-chatbot.streamlit.app")

st.markdown("**The problem**")
st.write("I could describe what RAG (retrieval-augmented generation) was, but I hadn't actually built one. I wanted to understand it hands-on, not just repeat the concept.")

st.markdown("**What I did**")
st.write("Built it with LangChain, FAISS, FastEmbedEmbeddings, and Groq's LLaMA 3.1, deployed through Streamlit. The hardest part wasn't the model — it was the chunking strategy: how you split documents decides whether retrieval actually pulls the right passage or just noise that sounds relevant. Getting that right took more iteration than picking the LLM did.")

st.markdown("**What came of it**")
st.write("It's deployed and working end-to-end. More importantly, I actually understand RAG well enough now to discuss it and build with it confidently — it's not a buzzword on my CV anymore, it's something I can defend in a conversation.")

st.link_button("Try the live demo →", "https://husnain-ai-chatbot.streamlit.app")
cta_button()
