import streamlit as st

st.title("💬 Feedback")
st.markdown("### We'd love to hear from you!")

st.markdown("""
Your feedback helps us improve and create better financial education tools. 
Whether you have suggestions, found a bug, or just want to share your experience, 
we're all ears!
""")

st.markdown("---")

# Feedback form
feedback_type = st.selectbox(
    "What type of feedback do you have?",
    [
        "General Feedback",
        "Feature Request",
        "Bug Report",
        "Content Suggestion",
        "Compliment 😊",
        "Question"
    ]
)

st.markdown("### Your Feedback")

# Rating
rating = st.slider(
    "How would you rate your experience?",
    min_value=1,
    max_value=5,
    value=4,
    help="1 = Poor, 5 = Excellent"
)

# Display stars based on rating
stars = "⭐" * rating
st.markdown(f"#### {stars}")

# Feedback text
feedback_text = st.text_area(
    "Tell us more:",
    placeholder="Share your thoughts, suggestions, or describe any issues you encountered...",
    height=150
)

# Optional contact
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name (optional)", placeholder="Your name")

with col2:
    email = st.text_input("Email (optional)", placeholder="your.email@example.com")

# Feature-specific feedback
st.markdown("---")
st.markdown("### Rate Our Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    quiz_rating = st.radio(
        "Knowledge Quiz",
        ["😍 Love it", "👍 Good", "😐 Okay", "👎 Needs work"],
        horizontal=True
    )
    
    analyzer_rating = st.radio(
        "Expense Analyzer",
        ["😍 Love it", "👍 Good", "😐 Okay", "👎 Needs work"],
        horizontal=True
    )

with feature_col2:
    lessons_rating = st.radio(
        "Lessons & AI Tutor",
        ["😍 Love it", "👍 Good", "😐 Okay", "👎 Needs work"],
        horizontal=True
    )
    
    budget_rating = st.radio(
        "Budget Planner",
        ["😍 Love it", "👍 Good", "😐 Okay", "👎 Needs work"],
        horizontal=True
    )

# Topics you'd like to see
st.markdown("---")
st.markdown("### What topics would you like us to add?")

topics_wanted = st.multiselect(
    "Select all that apply:",
    [
        "Cryptocurrency & Digital Assets",
        "Side Hustles & Passive Income",
        "Small Business Finance",
        "College Planning & Student Loans",
        "Insurance (life, health, auto)",
        "Estate Planning & Wills",
        "International Finance",
        "Financial Psychology & Behavior",
        "Ethical & Sustainable Investing",
        "Other (please specify in feedback)"
    ]
)

st.markdown("---")

# Submit button
if st.button("Submit Feedback", type="primary", use_container_width=True):
    if not feedback_text.strip():
        st.warning("Please share your thoughts in the feedback box!")
    else:
        # In a real app, you'd save this to a database or send via email
        st.success("🎉 Thank you for your feedback!")
        st.balloons()
        
        st.markdown(f"""
        ### Feedback Received!
        
        **Type:** {feedback_type}  
        **Rating:** {stars}  
        **Features Feedback:**
        - Quiz: {quiz_rating}
        - Analyzer: {analyzer_rating}
        - Lessons: {lessons_rating}
        - Budget: {budget_rating}
        
        **Requested Topics:** {', '.join(topics_wanted) if topics_wanted else 'None'}
        
        We really appreciate you taking the time to help us improve! 🙏
        """)
        
        st.info("💡 For urgent issues or questions, please use the support channels in the About Us page.")

st.markdown("---")

# Quick links
st.markdown("### Other Ways to Reach Us")

quick_col1, quick_col2, quick_col3 = st.columns(3)

with quick_col1:
    st.markdown("""
    #### 📧 Email
    support@financialliteracyhub.com
    *(example address)*
    """)

with quick_col2:
    st.markdown("""
    #### 💬 Community
    Join our Discord/Slack
    *(example link)*
    """)

with quick_col3:
    st.markdown("""
    #### 🐛 Bug Reports
    GitHub Issues
    *(example link)*
    """)

st.markdown("---")

st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Thank you for being part of our financial literacy community!</p>
    <p style='font-size: 12px;'>Your feedback helps us create better tools for everyone.</p>
</div>
""", unsafe_allow_html=True)
