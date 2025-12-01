import streamlit as st
from openai import OpenAI

st.title("💰 Personalized Budget Planner")
st.markdown("### Create a custom budget based on your income and financial goals")

# Initialize OpenAI client
if "OPENAI_API_KEY" not in st.secrets:
    st.error("Missing `OPENAI_API_KEY` in Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Get user level if available
user_level = st.session_state.get("user_level", "beginner")

st.info(f"💡 Budget recommendations tailored for **{user_level.title()}** level")

# Income section
st.markdown("## 💵 Income")
col1, col2 = st.columns(2)

with col1:
    monthly_income = st.number_input(
        "Monthly Income (after taxes):",
        min_value=0,
        value=3000,
        step=100,
        help="Enter your take-home pay after taxes"
    )

with col2:
    additional_income = st.number_input(
        "Additional Income (side gigs, etc.):",
        min_value=0,
        value=0,
        step=50
    )

total_income = monthly_income + additional_income
st.metric("Total Monthly Income", f"${total_income:,.2f}")

st.markdown("---")

# Fixed expenses
st.markdown("## 🏠 Fixed Expenses (Needs)")
st.caption("Essential expenses that stay relatively the same each month")

exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    rent = st.number_input("Rent/Mortgage:", min_value=0, value=1000, step=50)
    utilities = st.number_input("Utilities (electric, water, gas):", min_value=0, value=150, step=25)
    insurance = st.number_input("Insurance (health, car, etc.):", min_value=0, value=200, step=25)
    groceries = st.number_input("Groceries:", min_value=0, value=400, step=25)

with exp_col2:
    transportation = st.number_input("Transportation (gas, public transit):", min_value=0, value=200, step=25)
    phone_internet = st.number_input("Phone & Internet:", min_value=0, value=100, step=25)
    debt_payment = st.number_input("Minimum Debt Payments:", min_value=0, value=0, step=50)
    other_fixed = st.number_input("Other Fixed Expenses:", min_value=0, value=100, step=25)

total_needs = rent + utilities + insurance + groceries + transportation + phone_internet + debt_payment + other_fixed

st.markdown("---")

# Variable expenses
st.markdown("## 🎉 Variable Expenses (Wants)")
st.caption("Non-essential spending that can vary month to month")

want_col1, want_col2 = st.columns(2)

with want_col1:
    dining_out = st.number_input("Dining Out & Takeout:", min_value=0, value=200, step=25)
    entertainment = st.number_input("Entertainment (streaming, movies, etc.):", min_value=0, value=100, step=25)
    shopping = st.number_input("Shopping (clothes, etc.):", min_value=0, value=150, step=25)

with want_col2:
    hobbies = st.number_input("Hobbies & Recreation:", min_value=0, value=100, step=25)
    subscriptions = st.number_input("Subscriptions:", min_value=0, value=50, step=10)
    other_wants = st.number_input("Other Wants:", min_value=0, value=100, step=25)

total_wants = dining_out + entertainment + shopping + hobbies + subscriptions + other_wants

st.markdown("---")

# Savings and goals
st.markdown("## 💎 Savings & Financial Goals")

save_col1, save_col2 = st.columns(2)

with save_col1:
    emergency_fund = st.number_input("Emergency Fund Contribution:", min_value=0, value=200, step=50)
    retirement = st.number_input("Retirement Savings:", min_value=0, value=200, step=50)
    other_savings = st.number_input("Other Savings Goals:", min_value=0, value=200, step=50)

with save_col2:
    financial_goal = st.text_input(
        "Main Financial Goal:",
        placeholder="e.g., Save for house down payment, pay off credit card, build emergency fund"
    )
    goal_timeline = st.selectbox(
        "Goal Timeline:",
        ["Within 6 months", "6-12 months", "1-2 years", "3-5 years", "5+ years"]
    )

total_savings = emergency_fund + retirement + other_savings

st.markdown("---")

# Calculate totals
total_expenses = total_needs + total_wants + total_savings
remaining = total_income - total_expenses

# Display summary
st.markdown("## 📊 Budget Summary")

summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

with summary_col1:
    st.metric("Total Income", f"${total_income:,.2f}")

with summary_col2:
    needs_pct = (total_needs / total_income * 100) if total_income > 0 else 0
    st.metric("Needs", f"${total_needs:,.2f}", f"{needs_pct:.1f}%")

with summary_col3:
    wants_pct = (total_wants / total_income * 100) if total_income > 0 else 0
    st.metric("Wants", f"${total_wants:,.2f}", f"{wants_pct:.1f}%")

with summary_col4:
    savings_pct = (total_savings / total_income * 100) if total_income > 0 else 0
    st.metric("Savings", f"${total_savings:,.2f}", f"{savings_pct:.1f}%")

st.markdown("---")

# Remaining balance
if remaining >= 0:
    st.success(f"### ✅ Remaining: ${remaining:,.2f}")
else:
    st.error(f"### ⚠️ Over Budget: ${remaining:,.2f}")

# 50/30/20 comparison
st.markdown("### 📐 50/30/20 Rule Comparison")
st.caption("Ideal: 50% Needs, 30% Wants, 20% Savings")

rule_col1, rule_col2, rule_col3 = st.columns(3)

with rule_col1:
    st.metric("Your Needs", f"{needs_pct:.1f}%", f"{needs_pct - 50:.1f}% vs ideal")

with rule_col2:
    st.metric("Your Wants", f"{wants_pct:.1f}%", f"{wants_pct - 30:.1f}% vs ideal")

with rule_col3:
    st.metric("Your Savings", f"{savings_pct:.1f}%", f"{savings_pct - 20:.1f}% vs ideal")

st.markdown("---")

# Generate AI analysis
if st.button("🤖 Get AI Budget Analysis", type="primary", use_container_width=True):
    if total_income == 0:
        st.warning("Please enter your income to get an analysis!")
    else:
        with st.spinner("Analyzing your budget..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are a financial advisor helping a {user_level} level user create a realistic budget. Analyze their income and expenses, provide specific recommendations for reducing costs, suggest ways to reach their goals, and identify areas of concern. Be encouraging but realistic. Provide actionable advice. Do not use dollar signs in explanations or LaTeX formatting."
                        },
                        {
                            "role": "user",
                            "content": f"""
                            Create a detailed budget analysis:
                            
                            INCOME:
                            - Monthly Income: {monthly_income}
                            - Additional Income: {additional_income}
                            - Total: {total_income}
                            
                            NEEDS (Fixed Expenses):
                            - Housing: {rent}
                            - Utilities: {utilities}
                            - Insurance: {insurance}
                            - Groceries: {groceries}
                            - Transportation: {transportation}
                            - Phone/Internet: {phone_internet}
                            - Debt Payments: {debt_payment}
                            - Other: {other_fixed}
                            - Total Needs: {total_needs} ({needs_pct:.1f}%)
                            
                            WANTS (Variable Expenses):
                            - Dining Out: {dining_out}
                            - Entertainment: {entertainment}
                            - Shopping: {shopping}
                            - Hobbies: {hobbies}
                            - Subscriptions: {subscriptions}
                            - Other: {other_wants}
                            - Total Wants: {total_wants} ({wants_pct:.1f}%)
                            
                            SAVINGS:
                            - Emergency Fund: {emergency_fund}
                            - Retirement: {retirement}
                            - Other Savings: {other_savings}
                            - Total Savings: {total_savings} ({savings_pct:.1f}%)
                            
                            FINANCIAL GOAL: {financial_goal if financial_goal else 'Not specified'}
                            TIMELINE: {goal_timeline}
                            
                            BUDGET STATUS: {"Over budget by " + str(abs(remaining)) if remaining < 0 else "Under budget with " + str(remaining) + " remaining"}
                            
                            Provide:
                            1. Overall budget health assessment
                            2. Comparison to 50/30/20 rule
                            3. Specific areas to improve (with dollar amounts where relevant)
                            4. Tips to reach their financial goal
                            5. Action steps they can take this month
                            """
                        }
                    ],
                    temperature=0.7
                )
                
                st.markdown("## 🎯 Your Personalized Budget Analysis")
                st.markdown(response.choices[0].message.content)
                
                # Additional tips based on level
                st.markdown("---")
                st.markdown("### 💡 Quick Tips for Your Level")
                
                if user_level == "beginner":
                    st.info("""
                    **Beginner Tips:**
                    - Start tracking every expense for one month
                    - Build a 500-1000 emergency fund first
                    - Focus on paying off high-interest debt
                    - Automate your savings to make it easier
                    """)
                elif user_level == "intermediate":
                    st.info("""
                    **Intermediate Tips:**
                    - Review and optimize subscriptions quarterly
                    - Increase retirement contributions by 1-2%
                    - Look into tax-advantaged savings accounts
                    - Set up sinking funds for irregular expenses
                    """)
                else:
                    st.info("""
                    **Advanced Tips:**
                    - Maximize tax-advantaged account contributions
                    - Review asset allocation quarterly
                    - Consider tax-loss harvesting strategies
                    - Explore additional income streams
                    """)
                
            except Exception as e:
                st.error(f"Error generating analysis: {e}")

# Export option
st.markdown("---")
st.markdown("### 💾 Save Your Budget")

budget_summary = f"""
# My Budget Plan

## Income
- Monthly Income: ${monthly_income:,.2f}
- Additional Income: ${additional_income:,.2f}
- **Total Income: ${total_income:,.2f}**

## Expenses

### Needs ({needs_pct:.1f}% of income)
- Rent/Mortgage: ${rent:,.2f}
- Utilities: ${utilities:,.2f}
- Insurance: ${insurance:,.2f}
- Groceries: ${groceries:,.2f}
- Transportation: ${transportation:,.2f}
- Phone & Internet: ${phone_internet:,.2f}
- Debt Payments: ${debt_payment:,.2f}
- Other: ${other_fixed:,.2f}
- **Total Needs: ${total_needs:,.2f}**

### Wants ({wants_pct:.1f}% of income)
- Dining Out: ${dining_out:,.2f}
- Entertainment: ${entertainment:,.2f}
- Shopping: ${shopping:,.2f}
- Hobbies: ${hobbies:,.2f}
- Subscriptions: ${subscriptions:,.2f}
- Other: ${other_wants:,.2f}
- **Total Wants: ${total_wants:,.2f}**

### Savings ({savings_pct:.1f}% of income)
- Emergency Fund: ${emergency_fund:,.2f}
- Retirement: ${retirement:,.2f}
- Other Savings: ${other_savings:,.2f}
- **Total Savings: ${total_savings:,.2f}**

## Summary
- Total Expenses: ${total_expenses:,.2f}
- Remaining: ${remaining:,.2f}
- Financial Goal: {financial_goal if financial_goal else 'Not specified'}
- Timeline: {goal_timeline}
"""

st.download_button(
    label="📄 Download Budget as Text File",
    data=budget_summary,
    file_name="my_budget_plan.txt",
    mime="text/plain",
    use_container_width=True
)
