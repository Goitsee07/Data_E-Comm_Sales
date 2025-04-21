
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("RFM Insights")

# Load data
df = pd.read_csv("../data/cleaned/cleaned_orders.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

# RFM Calculation
snapshot_date = df['order_date'].max() + pd.Timedelta(days=1)
rfm = df.groupby('customer_id').agg({
    'order_date': lambda x: (snapshot_date - x.max()).days,
    'order_id': 'count',
    'sales': 'sum'
}).rename(columns={
    'order_date': 'Recency',
    'order_id': 'Frequency',
    'sales': 'MonetaryValue'
})

rfm['R'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1]).astype(int)
rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)
rfm['M'] = pd.qcut(rfm['MonetaryValue'], 4, labels=[1, 2, 3, 4]).astype(int)

rfm['RFM_Score'] = rfm[['R', 'F', 'M']].sum(axis=1)
rfm['Segment'] = pd.cut(rfm['RFM_Score'], bins=[2, 5, 8, 11, 13],
                        labels=['At Risk', 'Need Attention', 'Loyal', 'Champions'])

# Display Segment Distribution
st.subheader("Customer Segments")
segment_counts = rfm['Segment'].value_counts().sort_values(ascending=False)

st.bar_chart(segment_counts)

# RFM Table
st.subheader("RFM Table (Top 10)")
st.dataframe(rfm.sort_values(by='RFM_Score', ascending=False).head(10))
