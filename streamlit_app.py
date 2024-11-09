import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAB7IqPaUC3lNWFL5YfKpb2zlAVizz06ag")
model = genai.GenerativeModel("gemini-1.5-flash")

# Method 1: Inject CSS directly with markdown
st.markdown("""
<style>
.stHeading {
    display: flex;
    text-align: center;
}
.stMarkdown p {
    text-align: center;
    font-size: 21px;
}    

[data-testid="stVerticalBlockBorderWrapper"]{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    width: 100%;
}      
            
.stPageLink {
    border-style: solid;
    border-radius: 5px;
    padding: 1em;
    max-width: 100%;
}
            
.stPageLink p {
    font-size: 17px;
    text-align: center;  
}
            
.stPageLink:hover {
    background-color: #89C7FA;
    color: black;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

</style>
""", unsafe_allow_html=True)


st.header("Welcome to [App Title]")

st.write("Navigating finances for the first time can feel overwhelming, especially as a first-generation or low-income student. Our goal is to provide clear, practical information on financial topics to help you make informed decisions. From understanding student aid to managing credit and planning for retirement, we're here to support you every step of the way.")
st.write("Just click on the widgets below to access information, quizzes, resources, and more about the topics you'd wish to get familiar with")
st.write("")
c1 = st.container()
with c1:
    c1.page_link("pages/federal_aid.py", label="Federal Student Aid", icon="1️⃣")
    c1.page_link("pages/credit.py", label="Building Credit", icon="2️⃣")
    c1.page_link("pages/retirement.py", label="Investing for Retirement", icon="3️⃣")

# response = model.generate_content("How many planets are in our solar system?")
