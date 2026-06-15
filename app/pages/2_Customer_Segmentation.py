import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "customer_intelligence_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.title("👥 Customer Segmentation")

st.markdown(
    """
    Behavioral segmentation of airline loyalty members.
    """
)

# ---------------------------------
# Segment Counts
# ---------------------------------

segment_counts = (
    df['Segment']
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    'Segment',
    'Customers'
]

fig1 = px.pie(
    segment_counts,
    names='Segment',
    values='Customers',
    title='Segment Distribution'
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ---------------------------------
# Segment Statistics
# ---------------------------------

segment_stats = (
    df.groupby('Segment')
    [
        [
            'CLV',
            'Churn_Probability',
            'Recency_Months',
            'Total Flights'
        ]
    ]
    .mean()
    .round(2)
)

st.subheader(
    "Segment Characteristics"
)

st.dataframe(
    segment_stats,
    use_container_width=True
)

segment_risk = (
    df.groupby('Segment')['Churn_Probability']
      .mean()
      .reset_index()
)

fig_risk = px.bar(
    segment_risk,
    x='Segment',
    y='Churn_Probability',
    color='Segment',
    title='Average Churn Risk by Segment'
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)
# ---------------------------------
# Segment Insights
# ---------------------------------

st.subheader(
    "Segment Definitions"
)

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
        🏆 Champions

        Highest-value and most engaged customers.

        Frequent flyers with very low churn risk.
        """
    )

    st.info(
        """
        ✈️ Active Travelers

        Regular travelers with moderate engagement.

        Potential future champions.
        """
    )

with col2:

    st.warning(
        """
        ⚠️ Dormant Members

        Inactive members with high churn risk.

        Require immediate intervention.
        """
    )

    st.success(
        """
        🎯 Loyalty Enthusiasts

        Highly engaged loyalty members.

        Strong retention potential.
        """
    )
