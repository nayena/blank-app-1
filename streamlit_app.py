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
.stMarkdown {
    text-align: center;
}            
            
.stPageLink {
    border-style: solid;
    border-radius: 5px;
    text-align: center;
    padding: 1em;
    max-width: 50%;
}

</style>
""", unsafe_allow_html=True)


st.header("Financial Literacy App Title")

st.write("Introduction Blurb. Description of the motivation Introduction Blurb. Mission Statement. Information about how to navigate the page")

st.page_link("pages/federal_aid.py", label="Federal Student Aid", icon="1️⃣")


st.page_link("pages/credit.py", label="Building Credit", icon="2️⃣")


st.page_link("pages/retirement.py", label="Investing for Retirement", icon="3️⃣")

# response = model.generate_content("How many planets are in our solar system?")

st.write("Testing Gemini Output")
#st.write(response.text)


st.write("Hello, can you see this?????")
