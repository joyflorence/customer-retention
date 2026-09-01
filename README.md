# Customer Retention & Business Performance Analysis

An end-to-end customer retention and business performance analysis using Python and Streamlit.

The project explores customer churn, retention, customer behaviour, segmentation, and revenue performance to identify opportunities for improving customer retention and supporting data-driven business decisions.

---

## 📊 Project Highlights

- 📈 Analysed over **7,000 customer records**.
- 📉 Calculated overall customer churn and retention rates.
- 👥 Created customer segments based on customer behaviour, value, tenure, and engagement.
- 💰 Analysed revenue contribution across customer segments.
- 🔍 Identified customer characteristics associated with higher churn.
- 📊 Built an interactive dashboard using Streamlit and Plotly.
- 🎯 Developed business-focused customer retention recommendations.

---

## 🎯 Business Problem

Customer churn can significantly affect a company's revenue and long-term growth. Understanding why customers leave and identifying customer groups that require attention can help businesses develop more effective retention strategies.

This project aims to answer questions such as:

- What percentage of customers churn?
- What percentage of customers are retained?
- Which customer characteristics are associated with churn?
- How does customer tenure relate to churn?
- Do monthly charges influence customer churn?
- Which contract types experience higher churn?
- Which customer segments generate the most revenue?
- Which customer groups should be prioritised for retention strategies?

---

## 📂 Dataset

The dataset used in this project is the **Telco Customer Churn Dataset**.

It contains customer-level information including:

- Customer demographics
- Account information
- Services subscribed to
- Contract type
- Payment method
- Monthly charges
- Total charges
- Customer churn status

### Key Variables

| Variable | Description |
|---|---|
| `customerID` | Unique customer identifier |
| `gender` | Customer gender |
| `SeniorCitizen` | Indicates whether the customer is a senior citizen |
| `Partner` | Indicates whether the customer has a partner |
| `Dependents` | Indicates whether the customer has dependents |
| `tenure` | Number of months the customer has stayed with the company |
| `PhoneService` | Whether the customer has phone service |
| `InternetService` | Type of internet service |
| `Contract` | Customer contract type |
| `PaymentMethod` | Customer payment method |
| `MonthlyCharges` | Amount charged to the customer per month |
| `TotalCharges` | Total amount charged to the customer |
| `Churn` | Indicates whether the customer left the company |

---

# 🛠️ Tools and Technologies

## Data Analysis

- **Python**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualisation
- **KaggleHub** – Dataset access
- **Jupyter Notebook / VS Code** – Data analysis environment

## Dashboard Development

- **Streamlit** – Interactive dashboard development
- **Plotly** – Interactive data visualisation

---

# 🔄 Analysis Methodology

The project followed a structured business analysis approach:

### 1. Data Understanding

Examined the dataset structure, variables, data types, and overall data quality.

### 2. Data Cleaning

Identified and handled:

- Invalid blank values.
- Data type inconsistencies.
- Numerical conversion issues.
- Potential outliers.

### 3. Exploratory Data Analysis

Explored:

- Customer demographics.
- Customer tenure.
- Monthly charges.
- Total charges.
- Customer services.
- Customer churn behaviour.

### 4. Churn Analysis

Calculated and analysed:

- Total customers.
- Churned customers.
- Retained customers.
- Customer churn rate.
- Customer retention rate.

### 5. Customer Segmentation

Customers were grouped based on:

- Customer tenure.
- Spending behaviour.
- Customer value.
- Service usage.
- Customer churn behaviour.

### 6. Revenue Analysis

Revenue performance was analysed across customer segments to understand:

- Total revenue contribution.
- Customer value.
- Revenue distribution.
- High-value customer groups.

### 7. Business Recommendations

Customer retention strategies were developed based on the patterns identified during the analysis.

### 8. Dashboard Development

An interactive Streamlit dashboard was developed to communicate key business metrics and insights.

---

# 📊 Project Workflow

```text
Data Collection
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Missing and Invalid Value Detection
      ↓
Data Type Conversion
      ↓
Outlier Detection and Investigation
      ↓
Exploratory Data Analysis
      ↓
Churn Analysis
      ↓
Customer Segmentation
      ↓
Revenue Analysis
      ↓
Business Insights and Recommendations
      ↓
Streamlit Dashboard Development
```

---

# 📈 Dashboard

An interactive dashboard was developed using **Streamlit** and **Plotly** to present customer retention and business performance insights.

## Key Performance Indicators

The dashboard includes:

- Total Customers
- Customer Retention Rate
- Customer Churn Rate
- Total Revenue

## Dashboard Analysis

The dashboard provides insights into:

- Customer Retention vs Churn
- Revenue by Customer Segment
- Customer Distribution by Lifecycle
- Churn Rate by Customer Segment
- Churn Rate by Contract Type
- Churn Rate by Payment Method

## Dashboard Filters

Users can interact with the dashboard using filters for:

- Gender
- Contract Type
- Internet Service
- Customer Segment

---

# 🖥️ Dashboard Preview

- checkout dashboard from the link

# 🔍 Key Findings

The analysis identified several important patterns in customer behaviour and retention.

- The overall customer churn rate was **26.6%**.
- The customer retention rate was **73.4%**.
- Customers with **MOM** experienced the highest churn rate of **42.7%**.
- Customers in the **high-value loyal** segment generated the highest total revenue.
- Customers with **[Shorter]tenure** experienced higher churn.
- **Payment Method of Electronic check** was associated with a higher churn rate.
- **High-value churned customer segment** represented an important high-value group that should be prioritised for retention efforts.

These findings highlight opportunities for targeted customer retention strategies and improved customer engagement.


---

# 💡 Business Recommendations

| Business Finding | Recommended Action | Expected Business Impact |
|---|---|---|
| High churn among new customers | Improve onboarding and early customer engagement | Improve early customer retention |
| High-value customers are at risk of churn | Develop personalised retention offers | Protect valuable revenue |
| High churn among month-to-month customers | Encourage customers to move to longer-term contracts | Improve customer loyalty and retention |
| Low engagement customers | Recommend relevant services and personalised bundles | Increase engagement and customer value |
| Certain payment methods are associated with higher churn | Investigate customer payment experience and offer alternative payment options | Reduce potential friction and churn |

---

# 💼 Business Impact

This analysis provides a structured approach for understanding customer churn and identifying customer groups that may require targeted retention strategies.

The insights can help a business:

- Identify customer groups with higher churn risk.
- Prioritise valuable customers for retention efforts.
- Understand how customer contracts relate to retention.
- Identify revenue contribution across customer segments.
- Improve customer engagement strategies.
- Support data-driven decision-making.
- Develop targeted retention campaigns.

The project demonstrates how customer data can be transformed into actionable insights that support customer retention and business performance.

---

# 👥 Customer Segmentation

Customers were segmented based on different aspects of customer behaviour and value.

Segmentation factors included:

- Customer tenure.
- Customer spending.
- Customer value.
- Number of subscribed services.
- Customer churn behaviour.

Customer profiles included:

- High-Value Loyal Customers
- High-Value Churned Customers
- New Customer Churned
- Low Engagement Customers
- Standard Customers

These customer profiles help identify groups with different behaviours, business value, and retention needs.

---

# 💰 Revenue Analysis

Revenue performance was analysed across customer segments to understand the financial contribution of different customer groups.

The analysis explored:

- Total revenue by customer segment.
- Customer value.
- Revenue contribution across customer groups.
- The relationship between customer retention and business value.

This helps identify valuable customer groups that may require greater retention attention.

---

# ⚠️ Limitations and Assumptions

This analysis has several limitations:

- The dataset represents a snapshot of customer information rather than a time-series dataset.
- Traditional monthly or yearly churn trends could not be analysed because a date variable was not available.
- The analysis identifies associations with churn but does not establish causation.
- Revenue calculations are based on the available `TotalCharges` variable and may not represent the company's complete financial performance.
- Customer segments were created using business rules and available dataset variables.
- The dataset represents a specific customer population and findings may not directly generalise to other businesses or industries.

---

# 📁 Project Structure

```text
customer-retention/
│
├── app.py
├── requirements.txt
├── telco_customer_dashboard_data.csv
├── customer_retention_analysis.ipynb
├── README.md
└── 
```

---

# 🚀 Running the Project Locally

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the Project Folder

```bash
cd customer-retention
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
pandas
plotly
numpy
matplotlib
kagglehub
```

---

# 🧠 Key Skills Demonstrated

- Data Cleaning
- Data Preparation
- Exploratory Data Analysis
- Customer Churn Analysis
- Customer Retention Analysis
- Customer Segmentation
- Revenue Analysis
- Business Analysis
- Data Visualisation
- Interactive Dashboard Development
- Python
- Pandas
- Streamlit
- Plotly

---

# 🔮 Future Improvements

Potential future improvements include:

- Developing a machine learning model to predict customer churn.
- Adding predictive customer risk scores.
- Performing feature importance analysis.
- Developing more advanced customer segmentation.
- Adding automated business insights to the dashboard.
- Connecting the dashboard to a live database.

---

# 👤 Author

**Joy Florence**

Aspiring Data Analyst | Business Analyst

**Skills:** Python | SQL | Excel | Power BI | Streamlit | Data Analysis