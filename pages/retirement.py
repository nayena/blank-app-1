import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Retirement Investment Guide", layout="wide")
    
    # Header
    st.title("💰 Retirement Investment Guide")
    st.markdown("Learn about different investment options for your retirement planning.")
    
    # Investment Options Overview
    st.header("Investment Options")
    
    # Create tabs for different investment types
    tabs = st.tabs(["Roth IRAs", "Brokerage Accounts", "Index Funds", "Stocks"])
    
    with tabs[0]:
        st.subheader("Roth IRAs")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A retirement account that offers tax-free growth and tax-free withdrawals in retirement.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")
            
        # Add an example compound interest calculator
        st.markdown("### 📊 Compound Interest Calculator")
        initial = st.number_input("Initial Investment ($)", min_value=0, value=1000)
        monthly = st.number_input("Monthly Contribution ($)", min_value=0, value=100)
        years = st.number_input("Investment Period (Years)", min_value=1, max_value=50, value=30)
        rate = st.slider("Expected Annual Return (%)", min_value=1, max_value=12, value=7)
        
        # Calculate future value
        rate_decimal = rate / 100
        periods = years * 12
        future_value = initial * (1 + rate_decimal) ** years
        future_value += monthly * (((1 + rate_decimal/12) ** periods - 1) / (rate_decimal/12))
        
        st.markdown(f"### Estimated Future Value: ${future_value:,.2f}")
    
    with tabs[1]:
        st.subheader("Brokerage Accounts")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("Accounts that allow you to buy and sell investments like stocks, bonds, and mutual funds.")
        with col2:
            st.markdown("### Tips")
            st.write("- Choose low-fee brokers")
            st.write("- Diversify your investments to manage risk")
            
        # Add comparison table of popular brokers
        st.markdown("### Popular Online Brokers Comparison")
        broker_data = {
            'Broker': ['Fidelity', 'Charles Schwab', 'Vanguard', 'E*TRADE'],
            'Stock Trade Fee': ['$0', '$0', '$0', '$0'],
            'Minimum Investment': ['$0', '$0', '$0', '$0'],
            'Mutual Fund Fees': ['$0-$49.95', '$0-$49.95', '$0-$50', '$0-$49.99']
        }
        st.table(pd.DataFrame(broker_data))
    
    with tabs[2]:
        st.subheader("Index Funds")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("Funds that track a market index, offering a simple, low-cost way to invest.")
        with col2:
            st.markdown("### Tips")
            st.write("- Great for beginners")
            st.write("- Provide broad market exposure with lower fees than many managed funds")
            
        # Add popular index funds comparison
        st.markdown("### Popular Index Funds")
        index_data = {
            'Fund Name': ['S&P 500 Index Fund', 'Total Stock Market Index Fund', 'International Stock Index Fund'],
            'Type': ['Large-Cap US Stocks', 'Full US Market', 'International Stocks'],
            'Typical Expense Ratio': ['0.03% - 0.15%', '0.03% - 0.15%', '0.05% - 0.20%']
        }
        st.table(pd.DataFrame(index_data))
    
    with tabs[3]:
        st.subheader("Stocks")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("Shares in a company that can be bought and sold, offering potential for growth.")
        with col2:
            st.markdown("### Tips")
            st.write("- Research before buying")
            st.write("- Avoid investing money you may need soon, as stocks are more volatile")
        
        # Add risk assessment tool
        st.markdown("### 📊 Risk Assessment Tool")
        st.write("Answer these questions to gauge if individual stock investing is right for you:")
        
        risk_score = 0
        emergency_fund = st.radio("Do you have an emergency fund of 3-6 months of expenses?", ["Yes", "No"])
        risk_score += 1 if emergency_fund == "Yes" else 0
        
        debt = st.radio("Are you free of high-interest debt?", ["Yes", "No"])
        risk_score += 1 if debt == "Yes" else 0
        
        timeline = st.radio("Is your investment timeline longer than 5 years?", ["Yes", "No"])
        risk_score += 1 if timeline == "Yes" else 0
        
        knowledge = st.radio("Do you understand basic financial statements and stock analysis?", ["Yes", "No"])
        risk_score += 1 if knowledge == "Yes" else 0
        
        st.markdown(f"### Your Stock Investment Readiness Score: {risk_score}/4")
        if risk_score <= 2:
            st.warning("Consider starting with index funds before investing in individual stocks.")
        else:
            st.success("You appear to be well-positioned for stock investing. Remember to start small and diversify!")
    
    # Footer with disclaimer
    st.markdown("---")
    st.caption("Disclaimer: This information is for educational purposes only and should not be considered financial advice. Always consult with a qualified financial advisor for personalized recommendations.")

if __name__ == "__main__":
    main()
