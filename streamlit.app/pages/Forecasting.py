
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.title("Sales Forecasting")

# Load data
df = pd.read_csv("data/cleaned/cleaned_orders.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

# Prepare monthly sales
monthly_sales = df.set_index('order_date').resample('M')['sales'].sum()

# Fit ARIMA model
model = ARIMA(monthly_sales, order=(1, 1, 1))
fitted = model.fit()
forecast = fitted.forecast(steps=6)

# Display chart
st.subheader("Monthly Sales & Forecast (Next 6 Months)")
fig, ax = plt.subplots(figsize=(10, 5))
monthly_sales.plot(ax=ax, label="Historical Sales")
forecast.plot(ax=ax, style='--', label="Forecast")
ax.set_ylabel("Sales")
ax.legend()
st.pyplot(fig)
