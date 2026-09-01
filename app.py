import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Retention Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("telco_customer_dashboard_data.csv")
    return df


df = load_data()


# ============================================================
# DASHBOARD TITLE
# ============================================================

st.title("Customer Retention & Business Performance Dashboard")

st.markdown(
    """
    This interactive dashboard analyses customer churn, retention,
    customer segments, and revenue performance.
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Dashboard Filters")


# Gender Filter
gender = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].dropna().unique(),
    default=df["gender"].dropna().unique()
)


# Contract Filter
contract = st.sidebar.multiselect(
    "Contract",
    options=df["Contract"].dropna().unique(),
    default=df["Contract"].dropna().unique()
)


# Internet Service Filter
internet_service = st.sidebar.multiselect(
    "Internet Service",
    options=df["InternetService"].dropna().unique(),
    default=df["InternetService"].dropna().unique()
)


# Customer Segment Filter
customer_profile = st.sidebar.multiselect(
    "Customer Segment",
    options=df["CustomerProfile"].dropna().unique(),
    default=df["CustomerProfile"].dropna().unique()
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["Contract"].isin(contract)) &
    (df["InternetService"].isin(internet_service)) &
    (df["CustomerProfile"].isin(customer_profile))
]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_customers = filtered_df["customerID"].nunique()

churned_customers = (
    filtered_df["Churn"] == "Yes"
).sum()

retained_customers = (
    filtered_df["Churn"] == "No"
).sum()


# Prevent division by zero
if total_customers > 0:

    churn_rate = (
        churned_customers / total_customers
    ) * 100

    retention_rate = (
        retained_customers / total_customers
    ) * 100

else:

    churn_rate = 0
    retention_rate = 0


total_revenue = filtered_df["TotalCharges"].sum()


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)


col2.metric(
    "Retention Rate",
    f"{retention_rate:.1f}%"
)


col3.metric(
    "Churn Rate",
    f"{churn_rate:.1f}%"
)


col4.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)


# ============================================================
# FIRST ROW OF CHARTS
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# CUSTOMER RETENTION VS CHURN
# ------------------------------------------------------------

with col1:

    churn_distribution = (
        filtered_df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn_distribution.columns = [
        "Churn Status",
        "Customers"
    ]


    fig_churn = px.pie(
        churn_distribution,
        names="Churn Status",
        values="Customers",
        hole=0.5,
        title="Customer Retention vs Churn"
    )


    st.plotly_chart(
        fig_churn,
        width="stretch"
    )


# ------------------------------------------------------------
# REVENUE BY CUSTOMER SEGMENT
# ------------------------------------------------------------

with col2:

    revenue_by_segment = (
        filtered_df
        .groupby(
            "CustomerProfile",
            observed=True
        )["TotalCharges"]
        .sum()
        .reset_index()
        .sort_values(
            by="TotalCharges",
            ascending=False
        )
    )


    fig_revenue = px.bar(
        revenue_by_segment,
        x="CustomerProfile",
        y="TotalCharges",
        title="Revenue by Customer Segment"
    )


    fig_revenue.update_layout(
        xaxis_title="Customer Segment",
        yaxis_title="Total Revenue"
    )


    st.plotly_chart(
        fig_revenue,
        width="stretch"
    )


# ============================================================
# SECOND ROW OF CHARTS
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# CUSTOMER LIFECYCLE DISTRIBUTION
# ------------------------------------------------------------

with col1:

    tenure_distribution = (
        filtered_df["TenureSegment"]
        .value_counts()
        .reset_index()
    )

    tenure_distribution.columns = [
        "Tenure Segment",
        "Customers"
    ]


    fig_tenure = px.bar(
        tenure_distribution,
        x="Tenure Segment",
        y="Customers",
        title="Customer Distribution by Lifecycle"
    )


    fig_tenure.update_layout(
        xaxis_title="Customer Lifecycle",
        yaxis_title="Number of Customers"
    )


    st.plotly_chart(
        fig_tenure,
        width="stretch"
    )


# ------------------------------------------------------------
# CHURN RATE BY CUSTOMER SEGMENT
# ------------------------------------------------------------

with col2:

    churn_segment = (
        filtered_df
        .groupby(
            "CustomerProfile",
            observed=True
        )["Churn"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
        .reset_index()
    )


    churn_segment.columns = [
        "Customer Segment",
        "Churn Rate"
    ]


    churn_segment = churn_segment.sort_values(
        by="Churn Rate",
        ascending=False
    )


    fig_segment_churn = px.bar(
        churn_segment,
        x="Customer Segment",
        y="Churn Rate",
        title="Churn Rate by Customer Segment"
    )


    fig_segment_churn.update_layout(
        xaxis_title="Customer Segment",
        yaxis_title="Churn Rate (%)"
    )


    st.plotly_chart(
        fig_segment_churn,
        width="stretch"
    )


# ============================================================
# THIRD ROW OF CHARTS
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# CHURN RATE BY CONTRACT TYPE
# ------------------------------------------------------------

with col1:

    churn_contract = (
        filtered_df
        .groupby("Contract")["Churn"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
        .reset_index()
    )


    churn_contract.columns = [
        "Contract",
        "Churn Rate"
    ]


    churn_contract = churn_contract.sort_values(
        by="Churn Rate",
        ascending=False
    )


    fig_contract = px.bar(
        churn_contract,
        x="Contract",
        y="Churn Rate",
        title="Churn Rate by Contract Type"
    )


    fig_contract.update_layout(
        xaxis_title="Contract Type",
        yaxis_title="Churn Rate (%)"
    )


    st.plotly_chart(
        fig_contract,
        width="stretch"
    )


# ------------------------------------------------------------
# CHURN RATE BY PAYMENT METHOD
# ------------------------------------------------------------

with col2:

    churn_payment = (
        filtered_df
        .groupby("PaymentMethod")["Churn"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
        .reset_index()
    )


    churn_payment.columns = [
        "Payment Method",
        "Churn Rate"
    ]


    churn_payment = churn_payment.sort_values(
        by="Churn Rate",
        ascending=False
    )


    fig_payment = px.bar(
        churn_payment,
        x="Payment Method",
        y="Churn Rate",
        title="Churn Rate by Payment Method"
    )


    fig_payment.update_layout(
        xaxis_title="Payment Method",
        yaxis_title="Churn Rate (%)"
    )


    st.plotly_chart(
        fig_payment,
        width="stretch"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    **Customer Retention & Business Performance Analysis**

    Built using Python, Pandas, Plotly, and Streamlit.
    """
)