FinChat AI — Financial Analyst Chatbot
======================================

An AI-powered financial dashboard built with Streamlit, OpenAI GPT-4o-mini, and Plotly.

SETUP
-----
1. Install dependencies:
   pip install -r requirements.txt

2. Add your OpenAI API key to the .env file:
   OPENAI_API_KEY=your-key-here

3. Run the app:
   streamlit run app.py

FEATURES
--------
- Company selector in sidebar
- Live financial metrics with year-over-year delta
- Bar chart: Total Revenue by year
- Line chart: Net Income vs Operating Cash Flow
- Persistent chat history with GPT-4o-mini
- Multi-turn conversation with full context

DATA
----
forage.csv contains financial data for Microsoft, Tesla, and Apple (2023–2025).
Columns: Company, Year, Total Revenue, Net Income, Total Assets, Total Liabilities, Cash Flow from Operating

To add more companies, simply append rows to forage.csv.
