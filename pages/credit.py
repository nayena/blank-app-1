import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title (" 💳 Credit")

st.header  ("What is it? ")
st.write  ("A numerical rating that indicates your creditworthiness, impacting your ability to get loans and favorable rates. Tips: Regularly check your credit report, and try to keep a good payment history and low credit utilization.")

image_url = "https://naran128386/Downloads/to/your/image.jpeg"
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

# Create tabs for different investment types
tabs = st.tabs(["Opening Credits", "Fees and Interest", "Credit Bureaus", "Collections"])
 
with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A retirement account that offers tax-free growth and tax-free withdrawals in retirement.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")
    

with tabs[1]:
       
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A retirement account that offers tax-free growth and tax-free withdrawals in retirement.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")

with tabs[2]:
       
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A retirement account that offers tax-free growth and tax-free withdrawals in retirement.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")



with tabs[3]:

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A retirement account that offers tax-free growth and tax-free withdrawals in retirement.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")



#st.header ("Credit Game")

st.markdown(
    "<h2 style='text-align: center;'>Credit Card Desition Game </h2>",
    unsafe_allow_html=True
)

with st.expander("1. Choose Your Credit Card Type", expanded=True):
    card_options = {
        "Low-Interest Card": {
            "interest_rate": 10,
            "annual_fee": 0,
            "credit_limit": 1000
        },
        "Rewards Card": {
            "interest_rate": 20,
            "annual_fee": 50,
            "credit_limit": 1500,
            "rewards_rate": 0.02  # Rewards 2% cash back on purchases
        },
        "Student Card": {
            "interest_rate": 25,
            "annual_fee": 0,
            "credit_limit": 500
        }
    }
    card_type = st.selectbox("Select a Credit Card Type", list(card_options.keys()))
    selected_card = card_options[card_type]
    
    # Display Card Details
    st.write(f"**Interest Rate:** {selected_card['interest_rate']}%")
    st.write(f"**Annual Fee:** ${selected_card['annual_fee']}")
    st.write(f"**Credit Limit:** ${selected_card['credit_limit']}")

# Initialize or reset balance and credit score
if "balance" not in st.session_state:
    st.session_state.balance = 0
if "credit_score" not in st.session_state:
    st.session_state.credit_score = 700

# --- Step 2: Make a Transaction ---
with st.expander("2. Make a Transaction", expanded=True):
    transaction_options = {
        "Pay for Books": 200,
        "Emergency Expense": 300,
        "Monthly Groceries": 100,
        "Pay Credit Card Balance": -st.session_state.balance
    }
    transaction = st.selectbox("Choose a Transaction", list(transaction_options.keys()))
    amount = transaction_options[transaction]
    
    if st.button("Submit Transaction"):
        # Calculate new balance
        if transaction == "Pay Credit Card Balance":
            payment = min(amount, st.session_state.balance)
            st.session_state.balance -= payment
            st.write(f"Paid off ${payment} of your credit card balance.")
        else:
            st.session_state.balance += amount
            st.write(f"Transaction completed: {transaction} - ${amount}")
        
        # Calculate rewards if applicable
        rewards = 0
        if "rewards_rate" in selected_card and amount > 0:
            rewards = amount * selected_card["rewards_rate"]
            st.write(f"Rewards Earned: ${rewards:.2f}")
        
        # Update credit score
        if st.session_state.balance > selected_card["credit_limit"]:
            st.session_state.credit_score -= 20
            st.write("You exceeded your credit limit! Your credit score has been penalized by 20 points.")
        elif st.session_state.balance > selected_card["credit_limit"] * 0.8:
            st.session_state.credit_score -= 10
            st.write("You're using more than 80% of your credit limit. Your credit score is reduced by 10 points.")
        elif transaction == "Pay Credit Card Balance":
            st.session_state.credit_score += 5
            st.write("Great! Paying down your balance has increased your credit score by 5 points.")
        
        # Display updated balance and credit score
        st.write(f"**New Balance:** ${st.session_state.balance}")
        st.write(f"**New Credit Score:** {st.session_state.credit_score}")

# --- Step 3: Summary ---
with st.expander("3. Summary :", expanded=True):
    st.write("Track your credit card balance, credit score, and see the effects of your decisions.")
    st.write(f"**Current Balance:** ${st.session_state.balance}")
    st.write(f"**Current Credit Score:** {st.session_state.credit_score}")