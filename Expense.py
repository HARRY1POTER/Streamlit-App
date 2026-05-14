import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.title("💰 Personal Expense Tracker")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Date", "Category", "Amount", "Note"])

# Sidebar input
st.sidebar.header("➕ Add Expense")

with st.sidebar.form("expense_form", clear_on_submit=True):

    date = st.date_input("Date", datetime.date.today())

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        format="%.2f"
    )

    note = st.text_input("Note")

    submitted = st.form_submit_button("Add Expense")

    if submitted:

        if amount == 0:
            st.warning("Amount must be greater than 0")

        else:
            new_data = pd.DataFrame(
                [[date, category, amount, note]],
                columns=["Date", "Category", "Amount", "Note"]
            )

            st.session_state.data = pd.concat(
                [st.session_state.data, new_data],
                ignore_index=True
            )

            st.success("Expense Added!")

df = st.session_state.data

# Show data
st.subheader("📋 Expense History")
st.dataframe(df, use_container_width=True)

# Summary
if not df.empty:
    total = df["Amount"].sum()
    st.metric("💸 Total Spending", f"₹ {total:.2f}")

    # Category-wise spending
    st.subheader("📊 Spending by Category")
    category_data = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_data)

    # Daily trend
    st.subheader("📈 Daily Spending Trend")
    df["Date"] = pd.to_datetime(df["Date"])
    daily_data = df.groupby("Date")["Amount"].sum()
    st.line_chart(daily_data)

    # Filter option
    st.subheader("🔍 Filter by Category")
    selected_category = st.selectbox(
        "Choose category", ["All"] + list(df["Category"].unique()))

    if selected_category != "All":
        filtered_df = df[df["Category"] == selected_category]
        st.dataframe(filtered_df, use_container_width=True)

# Download option
st.subheader("⬇️ Export Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "expenses.csv", "text/csv")