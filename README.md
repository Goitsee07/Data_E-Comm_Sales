# E-commerce Sales Data Analysis & Dashboard

This project analyzes an e-commerce dataset to uncover insights about sales performance, customer behavior, product success, and marketing campaign effectiveness. It includes both an interactive **Streamlit web app** and a **PDF report** version for comprehensive portfolio presentation.

## Table of Contents
- [Project Overview](#project-overview)
- [Business Questions](#business-questions)
- [Data Cleaning](#data-cleaning)
- [Streamlit App](#streamlit-app)
- [PDF Report](#pdf-report)
- [Power BI Dashboard (Optional)](#power-bi-dashboard-optional)
- [Technologies Used](#technologies-used)
- [Key Insights](#key-insights)

---

## Project Overview

This project explores customer and sales data from an e-commerce platform between January and June 2024. The goal is to support data-driven decisions in sales, marketing, and product development.

## Business Questions

- How have monthly sales trended over the past 6 months?
- Who are our most valuable customers?
- Which products are top performers?
- What campaigns drive the most revenue?

## Data Cleaning

Data was cleaned using SQL (simulated for this portfolio). Key steps:
```sql
-- Remove nulls
SELECT * FROM sales_data WHERE order_id IS NOT NULL AND product_id IS NOT NULL;

-- Extract month from order date
SELECT order_date, EXTRACT(MONTH FROM order_date) AS month FROM sales_data;

-- Join customer types
SELECT s.*, c.customer_type FROM sales_data s JOIN customers c ON s.customer_id = c.id;


---

Streamlit App

A live interactive web dashboard built using Streamlit.

Features:

Filterable visual analytics for sales, customers, products, and marketing.

Market Basket Analysis (Apriori).

Forecasting (time series with statsmodels).


Launch the App:

> Streamlit Web App




---

PDF Report

For offline portfolio viewing, a fully visual PDF report is available.

Highlights:

Monthly sales trends

Customer segmentation (LTV, new vs returning)

Top product analysis

Marketing campaign performance

SQL snippets and recommendations


Download: Full Report (PDF)


---

Power BI Dashboard (Optional)

If you prefer working with Power BI:

Folder: /powerbi_dashboard/
Includes:

monthly_sales.csv

customer_insights.csv

product_performance.csv

marketing_effectiveness.csv


These files are ready for direct import into Power BI Desktop for creating visuals similar to the Streamlit app.


---

Technologies Used

Python (Pandas, Seaborn, Matplotlib)

Streamlit for web dashboard

Power BI / Looker Studio (optional visual layer)

SQL for data querying

FPDF for report generation



---

Key Insights

March and May had the highest sales volume.

Returning customers generate 60%+ of revenue.

Tier 1 customers show higher lifetime value.

Spring Sale and Email marketing campaigns performed best.

Product A and B lead in total sales.



---

Author

GitHub: Goitsee07 Portfolio Project by a Data Analyst focused on user behavior and digital marketing analytics.

---


