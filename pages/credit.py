import streamlit as st

import google.generativeai as genai

st.title ("Credit")

st.header  ("What is it? ")
st.write  ("A numerical rating that indicates your creditworthiness, impacting your ability to get loans and favorable rates. Tips: Regularly check your credit report, and try to keep a good payment history and low credit utilization.")


# with st.sidebar:
#     st.["credit"]



with st.expander ("Opening Credit Cards"):
    st.write ('''
              What is it? A numerical rating that indicates your creditworthiness, impacting your ability to get loans and favorable rates. Tips: Regularly check your credit report, and try to keep a good payment history and low credit utilization.
              ''')

with st.expander ("Fees and Interest"):
    st.write ('''
              What are they? Costs associated with borrowing, including annual fees and interest rates. Tips: Understand the terms before you sign up. Look for cards with low or no annual fees and pay on time to avoid interest.
              ''')

with st.expander ("Credit Bureaus"):
    st.write ('''
              What are they? Agencies (Equifax, Experian, and TransUnion) that compile your credit history. Tips: Review your credit report annually for errors, which you can do for free at AnnualCreditReport.com.
              ''')

with st.expander ("Collections"):
    st.write (''' 
What is it? When debts go unpaid, they may be sent to a collection agency, impacting your credit score. Tips: If facing debt, communicate with creditors early to explore options before it reaches collections.
              ''')


 #st.image("credit.jpeg",caption = "an animated person holding a credit card")