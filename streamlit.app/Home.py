
import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("E-Commerce Customer Behavior Dashboard")

st.markdown("Welcome to the E-Commerce Dashboard. Use the sidebar to navigate between key insights:")

st.markdown("""
- **RFM Insights:** Understand customer value using Recency, Frequency, and Monetary scores.
- **Sales Forecasting:** See predicted revenue trends based on historical patterns.
- **Basket Analysis:** Discover what products are commonly bought together.
""")

# Load data
df = pd.read_csv("../data/cleaned/cleaned_orders.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

# KPIs
total_sales = df['sales'].sum()
total_customers = df['customer_id'].nunique()
total_orders = df['order_id'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Customers", total_customers)
col3.metric("Total Orders", total_orders)

# Monthly Sales
monthly_sales = df.groupby(df['order_date'].dt.to_period('M'))['sales'].sum()
monthly_sales.index = monthly_sales.index.astype(str)

st.subheader("Monthly Sales Trend")
st.line_chart(monthly_sales)
