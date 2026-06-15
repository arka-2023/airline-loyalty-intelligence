import streamlit as st
import pandas as pd
import numpy as np

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/customer_intelligence_dataset.csv"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("🎯 Retention Intelligence")

st.markdown(
    """
    AI-powered retention recommendations for customers at risk of churn.
    """
)

# =====================================================
# BUSINESS VALUE CALCULATIONS
# =====================================================

# Estimated campaign cost

df["Retention_Cost"] = np.select(
    [
        df["Segment"] == "Dormant Members",
        df["Segment"] == "Active Travelers",
        df["Segment"] == "Champions",
        df["Segment"] == "Loyalty Enthusiasts"
    ],
    [
        50,
        120,
        200,
        80
    ],
    default=100
)

# Revenue potentially lost if customer churns

df["Expected_Revenue_Saved"] = (
    df["CLV"]
    * df["Churn_Probability"]
)

# ROI estimate

df["ROI"] = (
    df["Expected_Revenue_Saved"]
    /
    df["Retention_Cost"]
)

# =====================================================
# KPI SECTION
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "High Priority Customers",
        int(
            (
                df["Priority_Level"] == "High"
            ).sum()
        )
    )

with col2:

    st.metric(
        "Potential Revenue Saved",
        f"${df['Expected_Revenue_Saved'].sum():,.0f}"
    )

with col3:

    st.metric(
        "Average ROI",
        f"{df['ROI'].mean():.1f}x"
    )

st.divider()

# =====================================================
# TOP RETENTION TARGETS
# =====================================================

st.subheader(
    "Top Retention Targets"
)

top_targets = (
    df.sort_values(
        "Retention_Priority",
        ascending=False
    )
)

display_cols = [
    "Loyalty Number",
    "Segment",
    "CLV",
    "Churn_Probability",
    "Priority_Level",
    "Expected_Revenue_Saved",
    "ROI",
    "Recommended_Action"
]

st.dataframe(
    top_targets[
        display_cols
    ].head(25),
    use_container_width=True
)

# =====================================================
# SEGMENT RETENTION ANALYSIS
# =====================================================

st.subheader(
    "Segment Retention Analysis"
)

segment_summary = (
    df.groupby("Segment")
    [
        [
            "CLV",
            "Churn_Probability",
            "Expected_Revenue_Saved",
            "ROI"
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    segment_summary,
    use_container_width=True
)

# =====================================================
# RETENTION CAMPAIGN PLAYBOOK
# =====================================================

st.subheader(
    "Recommended Campaign Playbook"
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        """
### 🏆 Champions

• VIP Recognition Program

• Exclusive Airport Lounge Access

• Early Access Promotions

• Premium Upgrade Offers
"""
    )

    st.info(
        """
### ✈️ Active Travelers

• Premium Cabin Upgrade

• Double Mileage Campaign

• Corporate Travel Benefits

• Route Expansion Offers
"""
    )

with col2:

    st.warning(
        """
### ⚠️ Dormant Members

• Win-back Campaign

• Bonus Miles Offer

• Re-engagement Emails

• Limited-Time Discounts
"""
    )

    st.success(
        """
### 🎯 Loyalty Enthusiasts

• Reward Redemption Campaign

• Loyalty Challenges

• Personalized Offers

• Status Upgrade Opportunities
"""
    )

# =====================================================
# HIGH RISK CUSTOMERS
# =====================================================

st.subheader(
    "High Risk Customers"
)

high_risk = df[
    df["Priority_Level"] == "High"
]

st.dataframe(
    high_risk[
        [
            "Loyalty Number",
            "Segment",
            "CLV",
            "Churn_Probability",
            "Expected_Revenue_Saved",
            "Recommended_Action"
        ]
    ],
    use_container_width=True
)

# =====================================================
# DOWNLOAD BUTTON
# =====================================================

st.download_button(
    label="📥 Download Retention List",
    data=high_risk.to_csv(index=False),
    file_name="retention_targets.csv",
    mime="text/csv"
)
