import streamlit as st
from openai import OpenAI
import json

st.set_page_config(page_title="Financial Literacy Learning Hub", page_icon="📚", layout="wide")

# Initialize OpenAI client
if "OPENAI_API_KEY" not in st.secrets:
    st.error("Missing `OPENAI_API_KEY` in Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state
if "user_level" not in st.session_state:
    st.session_state.user_level = "beginner"
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = None
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

# Lesson content organized by level and topic
LESSONS = {
    "beginner": {
        "Budgeting Basics": {
            "content": """
            ### What is a Budget?
            A budget is a plan for your money. It helps you track income (money coming in) and expenses (money going out).
            
            **The 50/30/20 Rule:**
            - 50% for needs (rent, food, utilities)
            - 30% for wants (entertainment, dining out)
            - 20% for savings and debt repayment
            
            **Why Budget?**
            - Avoid overspending
            - Save for goals
            - Reduce financial stress
            - Build wealth over time
            """,
            "key_points": ["Track income and expenses", "Follow the 50/30/20 rule", "Prioritize needs over wants", "Save consistently"]
        },
        "Understanding Credit": {
            "content": """
            ### What is Credit?
            Credit is borrowed money that you promise to pay back, usually with interest.
            
            **Credit Score Basics:**
            - Range: 300-850
            - Higher is better
            - Affects loan rates and approvals
            
            **Building Good Credit:**
            - Pay bills on time
            - Keep credit card balances low
            - Don't open too many accounts at once
            - Check your credit report annually
            """,
            "key_points": ["Pay on time", "Keep balances low", "Monitor your credit", "Build credit history"]
        },
        "Saving Money": {
            "content": """
            ### Why Save?
            Savings provide security and help you reach financial goals.
            
            **Emergency Fund:**
            - Save 3-6 months of expenses
            - Keep in accessible savings account
            - For unexpected costs only
            
            **Saving Strategies:**
            - Automate savings transfers
            - Start small (even $10/week helps)
            - Use high-yield savings accounts
            - Set specific savings goals
            """,
            "key_points": ["Build emergency fund", "Automate savings", "Set clear goals", "Start small"]
        }
    },
    "intermediate": {
        "Investment Basics": {
            "content": """
            ### Introduction to Investing
            Investing means putting money into assets that can grow in value over time.
            
            **Common Investment Types:**
            - Stocks: Ownership in companies
            - Bonds: Loans to companies/governments
            - Mutual Funds: Diversified portfolios
            - ETFs: Exchange-traded funds
            
            **Key Concepts:**
            - Diversification reduces risk
            - Time in market beats timing the market
            - Higher returns = higher risk
            - Start early for compound growth
            """,
            "key_points": ["Diversify investments", "Think long-term", "Understand risk tolerance", "Start investing early"]
        },
        "Debt Management": {
            "content": """
            ### Managing Debt Wisely
            Not all debt is bad, but managing it properly is crucial.
            
            **Good vs Bad Debt:**
            - Good: Student loans, mortgages (builds assets)
            - Bad: High-interest credit cards, payday loans
            
            **Debt Payoff Strategies:**
            - Avalanche: Pay highest interest first
            - Snowball: Pay smallest balance first
            - Consolidation: Combine debts for lower rate
            
            **Avoiding Debt Traps:**
            - Read terms carefully
            - Avoid minimum payments only
            - Don't ignore debt
            """,
            "key_points": ["Prioritize high-interest debt", "Choose payoff strategy", "Avoid new debt", "Understand terms"]
        },
        "Tax Fundamentals": {
            "content": """
            ### Understanding Taxes
            Taxes fund government services and understanding them helps you keep more money.
            
            **Types of Taxes:**
            - Income tax: On earnings
            - Sales tax: On purchases
            - Property tax: On real estate
            
            **Tax-Advantaged Accounts:**
            - 401(k): Retirement savings (pre-tax)
            - IRA: Individual retirement account
            - HSA: Health savings account
            
            **Deductions & Credits:**
            - Standard vs itemized deductions
            - Tax credits reduce tax owed
            - Keep receipts for deductible expenses
            """,
            "key_points": ["Understand tax brackets", "Use tax-advantaged accounts", "Track deductions", "File on time"]
        }
    },
    "advanced": {
        "Retirement Planning": {
            "content": """
            ### Planning for Retirement
            Start early to harness the power of compound interest.
            
            **Retirement Accounts:**
            - 401(k): Employer-sponsored, often with matching
            - Traditional IRA: Tax-deductible contributions
            - Roth IRA: Tax-free withdrawals in retirement
            
            **How Much to Save:**
            - Rule of thumb: 15% of income
            - Factor in Social Security
            - Consider lifestyle goals
            - Account for inflation
            
            **Investment Strategy:**
            - Age-appropriate asset allocation
            - More aggressive when young
            - More conservative near retirement
            """,
            "key_points": ["Max employer match", "Choose right account type", "Save 15% of income", "Adjust allocation with age"]
        },
        "Real Estate & Mortgages": {
            "content": """
            ### Homeownership Basics
            Buying a home is a major financial decision requiring careful planning.
            
            **Mortgage Types:**
            - Fixed-rate: Same rate throughout
            - Adjustable-rate (ARM): Rate changes over time
            - FHA: Lower down payment options
            
            **Home Buying Process:**
            - Save for down payment (20% ideal)
            - Get pre-approved for mortgage
            - Factor in closing costs
            - Budget for maintenance and repairs
            
            **Investment Property:**
            - Rental income potential
            - Tax benefits
            - Property management costs
            - Market research essential
            """,
            "key_points": ["Save 20% down payment", "Understand mortgage types", "Budget beyond mortgage", "Research market"]
        },
        "Advanced Investing": {
            "content": """
            ### Advanced Investment Strategies
            Build wealth through sophisticated investment approaches.
            
            **Portfolio Management:**
            - Asset allocation strategies
            - Rebalancing regularly
            - Tax-loss harvesting
            - Dollar-cost averaging
            
            **Alternative Investments:**
            - Real estate investment trusts (REITs)
            - Commodities
            - Cryptocurrency (high risk)
            - Private equity
            
            **Risk Management:**
            - Diversification across sectors
            - Hedging strategies
            - Stop-loss orders
            - Regular portfolio review
            """,
            "key_points": ["Diversify portfolio", "Rebalance regularly", "Understand alternatives", "Manage risk actively"]
        }
    }
}

# Initialize page in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
st.sidebar.title("📚 Learning Hub")
page = st.sidebar.radio("Navigate", ["Home", "Lessons", "Quizzes", "AI Tutor", "Budget Planner", "Progress"], 
                        key="nav_radio")

# User level selector
st.sidebar.markdown("---")
st.sidebar.subheader("Your Level")
st.session_state.user_level = st.sidebar.selectbox(
    "Select your knowledge level:",
    ["beginner", "intermediate", "advanced"],
    index=["beginner", "intermediate", "advanced"].index(st.session_state.user_level)
)

# HOME PAGE
if page == "Home":
    st.title("📚 Financial Literacy Learning Hub")
    st.markdown("### Welcome to your personal finance education center!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📖 Lessons")
        st.write("Learn financial concepts at your own pace with structured lessons.")
        st.markdown("👉 *Use the sidebar to navigate to Lessons*")
    
    with col2:
        st.markdown("#### ✅ Quizzes")
        st.write("Test your knowledge with AI-generated quizzes tailored to your level.")
        st.markdown("👉 *Use the sidebar to navigate to Quizzes*")
    
    with col3:
        st.markdown("#### 🤖 AI Tutor")
        st.write("Ask questions and get personalized financial advice from our AI tutor.")
        st.markdown("👉 *Use the sidebar to navigate to AI Tutor*")
    
    st.markdown("---")
    st.markdown("### Your Learning Path")
    
    levels_info = {
        "beginner": "🌱 Learn the fundamentals of budgeting, saving, and credit",
        "intermediate": "🌿 Explore investing, debt management, and taxes",
        "advanced": "🌳 Master retirement planning, real estate, and advanced strategies"
    }
    
    st.info(f"**Current Level: {st.session_state.user_level.title()}**\n\n{levels_info[st.session_state.user_level]}")

# LESSONS PAGE
elif page == "Lessons":
    st.title("📖 Financial Lessons")
    st.markdown(f"**Your Level: {st.session_state.user_level.title()}**")
    
    lessons = LESSONS[st.session_state.user_level]
    
    tabs = st.tabs(list(lessons.keys()))
    
    for i, (lesson_name, lesson_data) in enumerate(lessons.items()):
        with tabs[i]:
            st.markdown(lesson_data["content"])
            
            st.markdown("---")
            st.markdown("#### 🔑 Key Takeaways")
            for point in lesson_data["key_points"]:
                st.markdown(f"- {point}")
            
            st.markdown("---")
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button(f"Generate Quiz on {lesson_name}", key=f"quiz_{lesson_name}"):
                    with st.spinner("Creating personalized quiz..."):
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[
                                    {
                                        "role": "system",
                                        "content": "You are a financial literacy educator. Generate a 5-question multiple choice quiz based on the lesson content. Return ONLY valid JSON in this exact format: {\"questions\": [{\"question\": \"text\", \"options\": [\"A) text\", \"B) text\", \"C) text\", \"D) text\"], \"correct\": \"A\", \"explanation\": \"text\"}]}. Do not include any other text."
                                    },
                                    {
                                        "role": "user",
                                        "content": f"Create a quiz for {st.session_state.user_level} level on: {lesson_name}\n\nLesson content:\n{lesson_data['content']}"
                                    }
                                ],
                                temperature=0.7
                            )
                            
                            quiz_text = response.choices[0].message.content.strip()
                            st.session_state.current_quiz = json.loads(quiz_text)
                            st.session_state.quiz_answers = {}
                            st.success("Quiz generated! Scroll down to take it.")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error generating quiz: {e}")
            
            with col2:
                if st.button("Ask AI About This", key=f"ask_{lesson_name}"):
                    # Switch to AI Tutor page via sidebar
                    st.info("💡 Navigate to 'AI Tutor' in the sidebar to ask questions about this topic!")

# QUIZZES PAGE
elif page == "Quizzes":
    st.title("✅ Test Your Knowledge")
    
    if st.session_state.current_quiz is None:
        st.info("Select a topic and generate a quiz to get started!")
        
        topic = st.selectbox("Choose a topic:", list(LESSONS[st.session_state.user_level].keys()))
        
        if st.button("Generate Quiz"):
            with st.spinner("Creating your personalized quiz..."):
                try:
                    lesson_content = LESSONS[st.session_state.user_level][topic]["content"]
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a financial literacy educator. Generate a 5-question multiple choice quiz. Return ONLY valid JSON in this exact format: {\"questions\": [{\"question\": \"text\", \"options\": [\"A) text\", \"B) text\", \"C) text\", \"D) text\"], \"correct\": \"A\", \"explanation\": \"text\"}]}. Do not include any other text or markdown."
                            },
                            {
                                "role": "user",
                                "content": f"Create a {st.session_state.user_level} level quiz on: {topic}\n\n{lesson_content}"
                            }
                        ],
                        temperature=0.7
                    )
                    
                    quiz_text = response.choices[0].message.content.strip()
                    st.session_state.current_quiz = json.loads(quiz_text)
                    st.session_state.quiz_answers = {}
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating quiz: {e}")
    else:
        quiz = st.session_state.current_quiz
        st.markdown(f"**Questions: {len(quiz['questions'])}**")
        
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"### Question {i+1}")
            st.write(q["question"])
            
            answer = st.radio(
                "Select your answer:",
                q["options"],
                key=f"q_{i}",
                index=None
            )
            
            if answer:
                st.session_state.quiz_answers[i] = answer[0]
            
            st.markdown("---")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Submit Quiz"):
                if len(st.session_state.quiz_answers) < len(quiz["questions"]):
                    st.warning("Please answer all questions before submitting!")
                else:
                    correct = 0
                    st.markdown("### 📊 Results")
                    
                    for i, q in enumerate(quiz["questions"]):
                        user_answer = st.session_state.quiz_answers.get(i)
                        correct_answer = q["correct"]
                        
                        if user_answer == correct_answer:
                            correct += 1
                            st.success(f"✅ Question {i+1}: Correct!")
                        else:
                            st.error(f"❌ Question {i+1}: Incorrect")
                            st.info(f"**Correct answer:** {correct_answer})\n\n{q['explanation']}")
                    
                    score = (correct / len(quiz["questions"])) * 100
                    st.markdown(f"### Final Score: {score:.0f}%")
                    
                    if score >= 80:
                        st.balloons()
                        st.success("Excellent work! You've mastered this topic!")
                    elif score >= 60:
                        st.info("Good job! Review the explanations to improve further.")
                    else:
                        st.warning("Keep studying! Review the lesson and try again.")
        
        with col2:
            if st.button("New Quiz"):
                st.session_state.current_quiz = None
                st.session_state.quiz_answers = {}
                st.rerun()

# AI TUTOR PAGE
elif page == "AI Tutor":
    st.title("🤖 AI Financial Tutor")
    st.markdown("Ask me anything about personal finance! I'm here to help you learn.")
    
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    user_question = st.chat_input("Ask a financial question...")
    
    if user_question:
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        
        with st.chat_message("user"):
            st.write(user_question)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": f"You are a friendly financial literacy tutor for {st.session_state.user_level} level learners. Explain concepts clearly, use examples, and encourage good financial habits. Avoid using dollar signs or LaTeX formatting. Keep responses conversational and educational."
                            },
                            *st.session_state.chat_history
                        ],
                        temperature=0.7
                    )
                    
                    answer = response.choices[0].message.content
                    st.write(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")
    
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# BUDGET PLANNER PAGE
elif page == "Budget Planner":
    st.title("💰 Personalized Budget Planner")
    st.markdown("Create a custom budget based on your income and financial goals.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        monthly_income = st.number_input("Monthly Income (after taxes):", min_value=0, value=3000, step=100)
        savings_goal = st.number_input("Monthly Savings Goal:", min_value=0, value=600, step=50)
    
    with col2:
        debt_payment = st.number_input("Monthly Debt Payments:", min_value=0, value=0, step=50)
        financial_goal = st.text_input("Main Financial Goal:", placeholder="e.g., Save for emergency fund, pay off credit card")
    
    st.markdown("### Current Expenses")
    rent = st.number_input("Rent/Mortgage:", min_value=0, value=1000, step=50)
    utilities = st.number_input("Utilities:", min_value=0, value=150, step=25)
    groceries = st.number_input("Groceries:", min_value=0, value=400, step=25)
    transportation = st.number_input("Transportation:", min_value=0, value=200, step=25)
    entertainment = st.number_input("Entertainment:", min_value=0, value=200, step=25)
    other = st.number_input("Other Expenses:", min_value=0, value=150, step=25)
    
    if st.button("Generate Budget Plan"):
        total_expenses = rent + utilities + groceries + transportation + entertainment + other + debt_payment + savings_goal
        
        with st.spinner("Creating your personalized budget plan..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a financial advisor helping users create realistic budgets. Analyze their income and expenses, provide specific recommendations for reducing costs, suggest ways to reach their goals, and identify areas of concern. Be encouraging but realistic. Do not use dollar signs or LaTeX."
                        },
                        {
                            "role": "user",
                            "content": f"""
                            Create a budget analysis for a {st.session_state.user_level} level user:
                            
                            Monthly Income: {monthly_income}
                            Savings Goal: {savings_goal}
                            Financial Goal: {financial_goal}
                            
                            Current Expenses:
                            - Rent/Mortgage: {rent}
                            - Utilities: {utilities}
                            - Groceries: {groceries}
                            - Transportation: {transportation}
                            - Entertainment: {entertainment}
                            - Other: {other}
                            - Debt Payments: {debt_payment}
                            
                            Total Expenses: {total_expenses}
                            Remaining: {monthly_income - total_expenses}
                            
                            Provide a detailed analysis with specific recommendations.
                            """
                        }
                    ],
                    temperature=0.7
                )
                
                st.markdown("### 📊 Your Personalized Budget Analysis")
                st.write(response.choices[0].message.content)
                
                # Visual breakdown
                st.markdown("### Expense Breakdown")
                expense_data = {
                    "Housing": rent,
                    "Utilities": utilities,
                    "Groceries": groceries,
                    "Transportation": transportation,
                    "Entertainment": entertainment,
                    "Savings": savings_goal,
                    "Debt": debt_payment,
                    "Other": other
                }
                
                for category, amount in expense_data.items():
                    if amount > 0:
                        percentage = (amount / monthly_income) * 100
                        st.metric(category, f"${amount}", f"{percentage:.1f}% of income")
                
            except Exception as e:
                st.error(f"Error generating budget plan: {e}")

# PROGRESS PAGE
elif page == "Progress":
    st.title("📈 Your Learning Progress")
    
    st.markdown(f"### Current Level: {st.session_state.user_level.title()}")
    
    # Show completed lessons
    st.markdown("### 📚 Lessons Available")
    for lesson in LESSONS[st.session_state.user_level].keys():
        st.markdown(f"- {lesson}")
    
    # Quiz scores
    st.markdown("### 🏆 Quiz Performance")
    if st.session_state.quiz_score:
        for topic, score in st.session_state.quiz_score.items():
            st.progress(score / 100, text=f"{topic}: {score}%")
    else:
        st.info("Take quizzes to track your progress!")
    
    # Chat history summary
    st.markdown("### 💬 AI Tutor Sessions")
    st.write(f"Total questions asked: {len([m for m in st.session_state.chat_history if m['role'] == 'user'])}")
    
    # Recommendations
    st.markdown("### 🎯 Next Steps")
    levels = ["beginner", "intermediate", "advanced"]
    current_index = levels.index(st.session_state.user_level)
    
    if current_index < len(levels) - 1:
        next_level = levels[current_index + 1]
        st.info(f"Keep learning to unlock {next_level.title()} level content!")
    else:
        st.success("You've reached the advanced level! Keep practicing and stay updated on financial trends.")
    
    if st.button("Reset All Progress"):
        st.session_state.quiz_score = {}
        st.session_state.chat_history = []
        st.session_state.current_quiz = None
        st.success("Progress reset!")
        st.rerun()
