import streamlit as st

pages = {
    "Welcome": [
        st.Page("pages/home_page.py", title="Home", icon="🏠"),
    ],
    "Financial Tools": [
        st.Page("pages/quiz.py", title="Knowledge Quiz", icon="🎯"),
        st.Page("pages/analyzer.py", title="Expense Analyzer", icon="💸"),
        st.Page("pages/budget_planner.py", title="Budget Planner", icon="💰"),
    ],
    "Learning Center": [
        st.Page("pages/learn.py", title="Lessons & AI Tutor", icon="📚"),
        st.Page("pages/resources.py", title="Financial Resources", icon="📖"),
    ],
    "About": [
        st.Page("pages/about.py", title="About Us", icon="💼"),
        st.Page("pages/feedback.py", title="Feedback", icon="💬"),
    ],
}
pg = st.navigation(pages)
st.set_page_config(page_title="Financial Literacy Hub", page_icon="💰", layout="wide")
pg.run()
