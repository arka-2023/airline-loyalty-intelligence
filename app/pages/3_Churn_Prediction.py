import streamlit as st
import pandas as pd

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv(
    "data/customer_intelligence_dataset.csv"
)

# ---------------------------------------------------
# Page Header
# ---------------------------------------------------

st.title("🔮 Churn Prediction")

st.markdown(
    """
    Search a loyalty member and view churn risk.
    """
)

# ---------------------------------------------------
# Customer Search
# ---------------------------------------------------

customer_id = st.number_input(
    "Enter Loyalty Number",
    min_value=int(df["Loyalty Number"].min()),
    max_value=int(df["Loyalty Number"].max()),
    value=int(df["Loyalty Number"].iloc[0]),
    step=1
)

# ---------------------------------------------------
# Analyze Button
# ---------------------------------------------------

if st.button("Analyze Customer"):

    customer = df[
        df["Loyalty Number"] == customer_id
    ]

    if customer.empty:

        st.error(
            "Customer not found."
        )

    else:

        row = customer.iloc[0]

        col1, col2 = st.columns(2)

        # ---------------------------------------
        # Left Side
        # ---------------------------------------

        with col1:

            st.metric(
                "Segment",
                row["Segment"]
            )

            st.metric(
                "CLV",
                f"${row['CLV']:,.0f}"
            )

        # ---------------------------------------
        # Right Side
        # ---------------------------------------

        with col2:

            risk = row["Churn_Probability"]

            st.metric(
                "Churn Probability",
                f"{risk:.2%}"
            )

            st.metric(
                "Priority Level",
                row["Priority_Level"]
            )

        # ---------------------------------------
        # Risk Indicator
        # ---------------------------------------

        st.subheader("Risk Assessment")

        if risk < 0.20:

            st.success(
                f"🟢 LOW RISK ({risk:.2%})"
            )

        elif risk < 0.50:

            st.warning(
                f"🟡 MEDIUM RISK ({risk:.2%})"
            )

        else:

            st.error(
                f"🔴 HIGH RISK ({risk:.2%})"
            )

        # ---------------------------------------
        # Recommended Action
        # ---------------------------------------

        st.subheader(
            "Recommended Action"
        )

        action = row["Recommended_Action"]

        if row["Priority_Level"] == "High":

            st.error(action)

        elif row["Priority_Level"] == "Medium":

            st.warning(action)

        else:

            st.success(action)

        # ---------------------------------------
        # Customer Snapshot
        # ---------------------------------------

        st.subheader(
            "Customer Snapshot"
        )

        snapshot = pd.DataFrame(
            {
                "Metric": [
                    "Total Flights",
                    "Distance",
                    "Points Accumulated",
                    "Points Redeemed",
                    "Recency (Months)",
                    "CLV"
                ],
                "Value": [
                    row["Total Flights"],
                    row["Distance"],
                    row["Points Accumulated"],
                    row["Points Redeemed"],
                    row["Recency_Months"],
                    round(row["CLV"], 2)
                ]
            }
        )

        st.dataframe(
            snapshot,
            use_container_width=True,
            hide_index=True
        )

        # ---------------------------------------
        # Customer Profile
        # ---------------------------------------

        st.subheader(
            "Customer Profile"
        )

        profile = pd.DataFrame(
            {
                "Attribute": [
                    "Gender",
                    "Education",
                    "Marital Status",
                    "Loyalty Card",
                    "Enrollment Type",
                    "Province"
                ],
                "Value": [
                    row["Gender"],
                    row["Education"],
                    row["Marital Status"],
                    row["Loyalty Card"],
                    row["Enrollment Type"],
                    row["Province"]
                ]
            }
        )

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True
        )
