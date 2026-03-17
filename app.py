import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv("forage.csv")
data.columns = data.columns.str.strip()

companies = sorted(data["Company"].unique().tolist())

def chatbot(company, question):
    company_data = data[data["Company"].str.lower() == company.lower()]
    company_data = company_data.sort_values("Year")

    if len(company_data) == 0:
        return "Company not found."

    latest = company_data.iloc[-1]
    previous = company_data.iloc[-2] if len(company_data) > 1 else None

    question = question.lower()

    if question == "what is the total revenue?":
        return f"{company} total revenue in {latest['Year']} was ${latest['Total Revenue']} million."

    elif question == "how has net income changed over the last year?":
        if previous is None:
            return "Not enough data to compare last year."
        change = latest["Net Income"] - previous["Net Income"]
        if change > 0:
            return f"Net income increased by ${change} million compared to last year."
        else:
            return f"Net income decreased by ${abs(change)} million compared to last year."

    elif question == "what are total assets?":
        return f"{company} total assets in {latest['Year']} were ${latest['Total Assets']} million."

    elif question == "what is the operating cash flow?":
        return f"{company} operating cash flow in {latest['Year']} was ${latest['Cash Flow from Operating']} million."

    else:
        return "Sorry, I can only answer predefined questions."

st.set_page_config(page_title="FinChat", page_icon="💰", layout="wide")

st.title("💰 FinChat - Financial Chatbot ")

with st.sidebar:
    st.header("Select Companies")
    selected_companies = st.multiselect("Choose companies", companies, default=[companies[0]])

st.subheader("💬 Ask Financial Question")

question = st.selectbox("Select Question", [
    "What is the total revenue?",
    "How has net income changed over the last year?",
    "What are total assets?",
    "What is the operating cash flow?"
])

if st.button("Ask"):
    if selected_companies:
        for comp in selected_companies:
            response = chatbot(comp, question)
            st.success(f"**{comp}:** {response}")
    else:
        st.warning("Please select at least one company.")

if selected_companies:
    company_data = data[data["Company"].isin(selected_companies)].sort_values(["Company", "Year"])

    st.divider()
    st.subheader("📊 Financial Comparison")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(company_data, x="Year", y="Total Revenue",
                      color="Company", markers=True,
                      title="Revenue Comparison")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.line(company_data, x="Year", y="Net Income",
                       color="Company", markers=True,
                       title="Net Income Comparison")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Total Assets Comparison")
    fig3 = px.bar(company_data, x="Year", y="Total Assets",
                  color="Company", barmode="group",
                  title="Assets Comparison")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Operating Cash Flow Comparison")
    fig4 = px.line(company_data, x="Year", y="Cash Flow from Operating",
                   color="Company", markers=True,
                   title="Cash Flow Comparison")
    st.plotly_chart(fig4, use_container_width=True)