import streamlit as st
import google.generativeai as genai

st.set_page_config(layout="wide")

# Method 1: Inject CSS directly with markdown
st.markdown("""
<style>
@keyframes colorChange {
    0% { color: grey; }
    25% { color: #CCA4EC; }
    50% { color: #75DFAA; }
    75% { color: #F8AA7D; }
    100% { color: #FD8282; }
}

.stHeading {
    display: flex;
    text-align: center;
    animation: colorChange 3s infinite; 
    width: 100%;
}      
        
.stMarkdown p {
    text-align: center;
    font-size: 21px;
}    

[data-testid="stVerticalBlockBorderWrapper"]{
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 1rem;
    width: 100%;
} 

.stHorizontalBlock{
    width: 100%
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


st.title("Welcome to Cash Course!")

st.write("Navigating finances for the first time can feel overwhelming, especially as a first-generation or low-income student. Our goal is to provide clear, practical information on financial topics to help you make informed decisions. From understanding student aid to managing credit and planning for retirement, we're here to support you every step of the way.")
st.write("Just click on the widgets below to access information, quizzes, resources, and more about the topics you'd wish to get familiar with")
st.write("")

c1, c2, c3 = st.columns(3)
with c1:
    st.image("img/peep-21.png", width=325)

with c2:
    c4 = st.container()
    with c4:
        c4.page_link("pages/federal_aid.py", label="Federal Student Aid", icon="🤝")
        c4.page_link("pages/credit.py", label="Building Credit", icon="💳")
        c4.page_link("pages/retirement.py", label="Investing for Retirement", icon="💰")

with c3:
    st.image("img/peep-30.png", width=325)
    

