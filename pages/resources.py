import streamlit as st

st.title("📖 Financial Resources")
st.markdown("### Curated resources to continue your financial education")

# Government Resources
st.markdown("## 🏛️ Official Government Resources")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Consumer Financial Protection Bureau (CFPB)
    **Website:** [consumerfinance.gov](https://www.consumerfinance.gov)
    
    Free resources on:
    - Credit reports and scores
    - Student loans
    - Mortgages
    - Debt collection
    - Banking
    """)
    
    st.markdown("""
    ### IRS Free File
    **Website:** [irs.gov/freefile](https://www.irs.gov/filing/free-file-do-your-federal-taxes-for-free)
    
    - File federal taxes for free
    - Guided tax preparation
    - Available if you earn under a certain amount
    """)

with col2:
    st.markdown("""
    ### MyMoney.gov
    **Website:** [mymoney.gov](https://www.mymoney.gov)
    
    Financial literacy resources from the U.S. government:
    - Budgeting tools
    - Saving strategies
    - Investment basics
    - Retirement planning
    """)
    
    st.markdown("""
    ### Social Security Administration
    **Website:** [ssa.gov](https://www.ssa.gov)
    
    - Retirement benefit estimates
    - Medicare information
    - Plan for retirement
    - Check your earnings record
    """)

st.markdown("---")

# Educational Websites
st.markdown("## 🎓 Educational Websites & Tools")

ed_col1, ed_col2 = st.columns(2)

with ed_col1:
    st.markdown("""
    ### Khan Academy - Finance
    **Website:** [khanacademy.org/economics-finance-domain](https://www.khanacademy.org/economics-finance-domain)
    
    Free courses on:
    - Personal finance
    - Stocks and bonds
    - Economics
    - Video lessons
    """)
    
    st.markdown("""
    ### Investopedia
    **Website:** [investopedia.com](https://www.investopedia.com)
    
    - Financial dictionary
    - Investment tutorials
    - Market news
    - Calculators and tools
    """)
    
    st.markdown("""
    ### NerdWallet
    **Website:** [nerdwallet.com](https://www.nerdwallet.com)
    
    - Compare financial products
    - Credit card reviews
    - Banking tools
    - Investment guides
    """)

with ed_col2:
    st.markdown("""
    ### Mint (Budgeting App)
    **Website:** [mint.com](https://www.mint.com)
    
    - Free budget tracking
    - Bill reminders
    - Credit score monitoring
    - Spending insights
    """)
    
    st.markdown("""
    ### Annual Credit Report
    **Website:** [annualcreditreport.com](https://www.annualcreditreport.com)
    
    - Free credit reports
    - From all 3 bureaus
    - Check once per year
    - Official source
    """)
    
    st.markdown("""
    ### Financial Calculators
    - **Compound Interest:** [calculator.net/investment-calculator.html](https://www.calculator.net/investment-calculator.html)
    - **Debt Payoff:** [undebt.it](https://undebt.it)
    - **Retirement:** [bankrate.com/retirement/calculators/](https://www.bankrate.com/retirement/calculators/)
    """)

st.markdown("---")

# Books and Podcasts
st.markdown("## 📚 Recommended Books")

book_col1, book_col2 = st.columns(2)

with book_col1:
    st.markdown("""
    ### For Beginners
    - **"The Total Money Makeover"** by Dave Ramsey
    - **"Your Money or Your Life"** by Vicki Robin
    - **"I Will Teach You to Be Rich"** by Ramit Sethi
    - **"The Simple Path to Wealth"** by JL Collins
    """)

with book_col2:
    st.markdown("""
    ### For Advanced Learners
    - **"The Intelligent Investor"** by Benjamin Graham
    - **"A Random Walk Down Wall Street"** by Burton Malkiel
    - **"The Bogleheads' Guide to Investing"** by Taylor Larimore
    - **"Rich Dad Poor Dad"** by Robert Kiyosaki
    """)

st.markdown("---")

st.markdown("## 🎙️ Financial Podcasts")

podcast_col1, podcast_col2 = st.columns(2)

with podcast_col1:
    st.markdown("""
    - **Planet Money** - NPR's economics podcast
    - **The Dave Ramsey Show** - Debt-free living advice
    - **ChooseFI** - Financial independence
    - **Afford Anything** - Real estate & investing
    """)

with podcast_col2:
    st.markdown("""
    - **BiggerPockets Money** - Personal finance interviews
    - **Motley Fool Money** - Stock market insights
    - **Clark Howard Show** - Consumer advice
    - **So Money** - Financial success stories
    """)

st.markdown("---")

# Community Resources
st.markdown("## 👥 Online Communities")

st.markdown("""
**Reddit Communities:**
- r/personalfinance - General personal finance advice
- r/financialindependence - FIRE movement
- r/povertyfinance - Help for tight budgets
- r/investing - Investment discussions
- r/Bogleheads - Low-cost index investing

**Important:** Always verify financial advice from online communities with official sources!
""")

st.markdown("---")

# Emergency Resources
st.markdown("## 🚨 Emergency Financial Help")

emergency_col1, emergency_col2 = st.columns(2)

with emergency_col1:
    st.markdown("""
    ### If You're Struggling
    - **211:** Call or text for local assistance
    - **Feeding America:** Find food banks near you
    - **Modest Needs:** Emergency financial assistance
    - **LIHEAP:** Help with utility bills
    """)

with emergency_col2:
    st.markdown("""
    ### Housing Help
    - **HUD:** Housing counseling services
    - **Eviction Lab:** Know your rights
    - **NACA:** Homeownership assistance
    - **SNAP:** Food assistance program
    """)

st.markdown("---")

# Disclaimer
st.info("""
💡 **Note:** These resources are provided for educational purposes. We are not affiliated with any of these 
organizations. Always verify information and consider consulting with a licensed financial advisor for 
personalized advice.
""")

st.success("💪 Keep learning and building your financial knowledge! Remember, small steps lead to big changes.")
