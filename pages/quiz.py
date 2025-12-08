import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from openai import OpenAI
import os
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


st.title(" Financial Personality Quiz ")

st.write(
    "Take this quick 20-question quiz to find out your financial personality! "
    "Answer honestly, there are no right or wrong answers"
)

questions = [
    "When you get money (allowance, gifts, paycheck), what do you usually do first?",
    "If a new gadget drops, how likely are you to buy it?",
    "How often do you check how much money you have?",
    "If a friend forgets their wallet, what do you do?",
    "Do you feel guilty about spending money?",
    "How comfortable are you with trying new ways to make money?",
    "If you saved $200, what would you do with it?",
    "How fast do you spend gift money?",
    "What describes your attitude toward budgeting?",
    "How do you feel about borrowing money from friends?",
    "You hear about investing — what’s your reaction?",
    "If you see something you want at a pretty high price, what do you do?",
    "You’re at the mall with friends — what happens?",
    "How do you feel when your bank balance drops?",
    "You have a long-term goal (new phone, laptop). How committed are you?",
    "How likely are you to compare prices before buying?",
    "You see a charity you care about. What do you do?",
    "Would you rather: spend now or save for something bigger later?",
    "How organized are you with money overall?",
    "When you earn money, what motivates you the most?"
]

options = [
    ["Save it", "Spend a little", "Spend most of it", "Depends on my mood"],
    ["Not likely", "Maybe", "Pretty likely", "I need it NOW"],
    ["Daily", "Weekly", "Rarely", "Never"],
    ["Pay for them", "Split it", "Ignore it", "Tease them then maybe pay"],
    ["Always", "Never", "Sometimes", "Rarely"],
    ["Very comfortable", "Somewhat", "Not really", "Scared but curious"],
    ["Invest it", "Save more", "Spend half", "Spend all"],
    ["Slowly", "Moderately", "Fast", "Immediately"],
    ["Love it", "Try sometimes", "Don't like it", "Never tried"],
    ["Won’t borrow", "Borrow rarely", "Borrow often", "Always borrowing"],
    ["Excited", "Curious", "Confused", "Scared"],
    ["Wait for a sale", "Buy it now", "Don't buy", "Haggle"],
    ["I browse only", "Buy one small thing", "Buy something pricey", "Go wild"],
    ["Very stressed", "A little worried", "Meh", "Don’t care"],
    ["Very committed", "Somewhat", "Not really", "Forget about it"],
    ["Always compare", "Sometimes", "Rarely", "Never"],
    ["Donate", "Think about it", "Ignore", "Donate only if friends do"],
    ["Save", "Depends", "Spend", "Spend immediately"],
    ["Very organized", "Pretty good", "Not great", "Chaos"],
    ["Security", "Goals", "Fun", "Impulse"]
]

# Answer storage
if "responses" not in st.session_state:
    st.session_state.responses = {}

for i, q in enumerate(questions):
    st.write(f"### {i+1}. {q}")
    choice = st.radio(
        "",
        options[i],
        key=f"q_{i}"
    )
    st.session_state.responses[i] = choice
    st.divider()

if st.button("✨ Get My AI-Generated Financial Personality"):
    answers = list(st.session_state.responses.values())

    prompt = f"""
    The user is a teenager who completed a 20-question financial personality quiz.

    Here are their answers:
    {answers}

    Based on these, determine their financial personality.
    Choose one main type: Saver, Spender, Risk-Taker, Planner, or Giver.

    Then provide:
    - A friendly teen-appropriate explanation (5–7 sentences)
    - Strengths
    - Weak spots
    - 3 personalized tips they can apply right now

    Make it supportive and fun.
    """

    with st.spinner("Analyzing your results…"):
        completion = client.chat.completions.create(
            model="gpt-5.1",
            messages=[{"role": "user", "content": prompt}]
        )

    st.subheader("🎉 Your Financial Personality")
    st.write(completion.choices[0].message.content)
