import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# Load Data
# ----------------------------

df = pd.read_csv(
    "data/customer_intelligence_dataset.csv"
)

st.title("📊 Executive Overview")

st.markdown(
    "Business KPIs and portfolio health indicators."
)

# ----------------------------
# KPI Calculations
# ----------------------------

total_customers = len(df)

churn_rate = round(
    df['Churn'].mean() * 100,
    2
)

avg_clv = round(
    df['CLV'].mean(),
    2
)

high_priority = (
    df[df['Priority_Level'] == 'High']
    .shape[0]
)

st.success(
    f"""
    🚨 {high_priority:,} customers require immediate retention attention.
    
    Current churn rate is {churn_rate}%.
    
    Dormant Members represent the highest-risk segment.
    """
)

# ----------------------------
# KPI Cards
# ----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churn Rate",
    f"{churn_rate}%"
)

col3.metric(
    "Average CLV",
    f"${avg_clv:,.0f}"
)

col4.metric(
    "High Priority",
    f"{high_priority:,}"
)

st.divider()

# ----------------------------
# Segment Distribution
# ----------------------------

segment_counts = (
    df['Segment']
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    'Segment',
    'Customers'
]

fig_segment = px.bar(
    segment_counts,
    x='Segment',
    y='Customers',
    color='Segment',
    title='Customer Segment Distribution'
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)

# ----------------------------
# Priority Distribution
# ----------------------------

priority_counts = (
    df['Priority_Level']
    .value_counts()
    .reset_index()
)

priority_counts.columns = [
    'Priority',
    'Count'
]

fig_priority = px.pie(
    priority_counts,
    names='Priority',
    values='Count',
    title='Retention Priority Distribution'
)

st.plotly_chart(
    fig_priority,
    use_container_width=True
)

# ----------------------------
# Executive Insights
# ----------------------------

st.subheader("Executive Insights")

st.info(
    """
    • Customer behavior is a stronger predictor of churn than CLV.

    • Dormant Members represent the highest retention risk.

    • Champions remain highly engaged and should be protected.

    • Growth-oriented retention campaigns should target high-priority customers.
    """
)
