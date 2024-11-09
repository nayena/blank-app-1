import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAB7IqPaUC3lNWFL5YfKpb2zlAVizz06ag")
model = genai.GenerativeModel("gemini-1.5-flash")



st.title("Financial Literacy App Title")
st.subheader("Introduction Blurb.")

# response = model.generate_content("How many planets are in our solar system?")

st.write("Testing Gemini Output")
st.write(response.text)


st.write("Hello, can you see this?????")
