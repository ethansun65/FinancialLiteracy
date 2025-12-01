import streamlit as st

st.title("💰 Financial Literacy Hub")
st.markdown("### Your Personal Finance Education Platform")

st.markdown("""
Welcome to your comprehensive financial literacy companion! Whether you're just starting your financial 
journey or looking to deepen your knowledge, we're here to help you make informed decisions about your money.
""")

st.markdown("---")

# Main features showcase
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 Knowledge Quiz")
    st.markdown("""
    **Start here!** Take our personalized quiz to:
    - Assess your current financial knowledge
    - Get your financial literacy level
    - Receive customized learning recommendations
    - Track your progress over time
    """)
    st.info("👉 Not sure where to begin? Start with the Knowledge Quiz!")

with col2:
    st.markdown("### 💸 Expense Analyzer")
    st.markdown("""
    **Make smart purchases!** Upload bills or receipts to:
    - Analyze if purchases are financially wise
    - Get AI-powered advice on spending
    - Find cheaper alternatives
    - Learn from your buying decisions
    """)
    st.success("💡 Great for evaluating big purchases!")

with col3:
    st.markdown("### 📚 Learn & Grow")
    st.markdown("""
    **Master personal finance!** Access:
    - Structured lessons at your level
    - Interactive AI tutor for questions
    - Practice quizzes
    - Personalized budget planning
    """)
    st.warning("🌟 Build lasting financial skills!")

st.markdown("---")

# How it works section
st.markdown("## 🚀 How It Works")

steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4)

with steps_col1:
    st.markdown("#### 1️⃣ Quiz")
    st.markdown("Take the quiz to discover your level")

with steps_col2:
    st.markdown("#### 2️⃣ Learn")
    st.markdown("Study lessons tailored to you")

with steps_col3:
    st.markdown("#### 3️⃣ Practice")
    st.markdown("Test knowledge with quizzes")

with steps_col4:
    st.markdown("#### 4️⃣ Apply")
    st.markdown("Use tools for real decisions")

st.markdown("---")

# Key benefits
st.markdown("## ✨ Why Financial Literacy Matters")

benefit_col1, benefit_col2 = st.columns(2)

with benefit_col1:
    st.markdown("""
    #### 🎓 Build Essential Skills
    - Understand budgeting and saving
    - Learn about credit and debt
    - Master investing basics
    - Plan for your future
    """)
    
    st.markdown("""
    #### 💪 Make Confident Decisions
    - Evaluate purchases wisely
    - Avoid financial pitfalls
    - Set and achieve money goals
    - Build wealth over time
    """)

with benefit_col2:
    st.markdown("""
    #### 🤖 AI-Powered Learning
    - Personalized to your level
    - Get instant answers to questions
    - Real-time expense analysis
    - Custom budget recommendations
    """)
    
    st.markdown("""
    #### 📈 Track Your Progress
    - Monitor learning achievements
    - See knowledge improvements
    - Adapt as you grow
    - Unlock advanced content
    """)

st.markdown("---")

# Quick stats or testimonial section
st.markdown("## 📊 Financial Literacy by the Numbers")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Topics Covered", "15+", delta="All Levels")

with stat_col2:
    st.metric("AI Features", "4", delta="Personalized")

with stat_col3:
    st.metric("Learning Paths", "3", delta="Beginner to Advanced")

with stat_col4:
    st.metric("Interactive Tools", "5+", delta="Hands-on")

st.markdown("---")

# Call to action
st.markdown("## 🎯 Ready to Get Started?")

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3>Begin Your Financial Journey Today!</h3>
    <p>Use the navigation menu on the left to explore all features.</p>
</div>
""", unsafe_allow_html=True)

st.info("💡 **Pro Tip:** Start with the Knowledge Quiz to get personalized recommendations for your learning path!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Financial Literacy Hub | Empowering Smart Financial Decisions</p>
    <p style='font-size: 12px;'>Remember: Never share sensitive information like SSN, account numbers, or passwords</p>
</div>
""", unsafe_allow_html=True)
