import streamlit as st

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "customer_intelligence_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.set_page_config(
    page_title="Airline Loyalty Intelligence",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Airline Loyalty Intelligence Platform")

st.markdown("""
### Unlocking Behavioral Intelligence in Airline Loyalty Programs

This platform helps marketing teams:

- Identify customers likely to churn
- Understand customer segments
- Prioritize retention efforts
- Recommend targeted interventions

---

### Dashboard Modules

#### Executive Overview
Business KPIs and portfolio health.

#### Customer Segmentation
Behavioral segmentation of loyalty members.

#### Churn Prediction
Identify customers at risk of disengagement.

#### Retention Intelligence
Actionable recommendations for customer retention.

---

### Key Finding

Customer behavior is a stronger predictor of churn than Customer Lifetime Value (CLV) alone.

Behavioral indicators such as:

- Recency
- Flight frequency
- Travel distance
- Loyalty engagement

provide more actionable retention insights than historical value metrics.
""")
