
import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Market Basket Analysis")

# Load data
df = pd.read_csv("data/cleaned/cleaned_orders.csv")
basket_df = df[['order_id', 'product_name']].dropna()

# Basket matrix
basket = (basket_df
          .groupby(['order_id', 'product_name'])['product_name']
          .count().unstack().fillna(0)
          .applymap(lambda x: 1 if x > 0 else 0))

# Generate itemsets and rules
frequent_items = apriori(basket, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)
rules = rules.sort_values(by="lift", ascending=False)

# Display frequent itemsets
st.subheader("Top Frequent Itemsets")
st.dataframe(frequent_items.sort_values(by="support", ascending=False).head(10))

# Display association rules
st.subheader("Top Association Rules")
rules_display = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].copy()
rules_display['antecedents'] = rules_display['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_display['consequents'] = rules_display['consequents'].apply(lambda x: ', '.join(list(x)))

st.dataframe(rules_display.head(10))
