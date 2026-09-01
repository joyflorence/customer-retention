# Customer Retention & Business Performance Analysis

## Project Overview

This project analyses customer churn and retention patterns using the Telco Customer Churn dataset.

The goal is to understand customer behaviour, identify factors associated with customer churn, segment customers based on their value and engagement, analyse revenue performance, and generate actionable business recommendations to improve customer retention.

The project follows an end-to-end data analysis workflow, combining data cleaning, exploratory data analysis (EDA), churn analysis, customer segmentation, revenue analysis, and an interactive Streamlit dashboard.

---

## Business Problem

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

## Dashboard

An interactive dashboard was developed using **Streamlit** and **Plotly** to present key customer retention and business performance metrics.

### Key Performance Indicators

The dashboard includes:

- Total Customers
- Customer Retention Rate
- Customer Churn Rate
- Total Revenue

### Dashboard Analysis

The interactive dashboard provides insights into:

- Customer Retention vs Churn
- Revenue by Customer Segment
- Customer Distribution by Lifecycle
- Churn Rate by Customer Segment
- Churn Rate by Contract Type
- Churn Rate by Payment Method

### Dashboard Filters

Users can interact with the dashboard using filters for:

- Gender
- Contract Type
- Internet Service
- Customer Segment

---

## Dataset

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

## Tools and Technologies

### Data Analysis

- **Python**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualisation
- **KaggleHub** – Dataset access
- **Jupyter Notebook / VS Code** – Data analysis environment

### Dashboard Development

- **Streamlit** – Interactive dashboard development
- **Plotly** – Interactive data visualisation

---

## Project Workflow

The project followed the following analytical process:

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

## Data Cleaning and Preparation

The dataset was prepared through the following steps:

- Checked dataset structure and data types.
- Identified missing values.
- Identified invalid blank values.
- Converted `TotalCharges` into a numerical data type.
- Investigated potential outliers in numerical variables.
- Prepared the dataset for exploratory analysis and dashboard development.

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer characteristics and relationships between customer behaviour and churn.

The analysis included:

- Distribution of customer demographics.
- Analysis of customer tenure.
- Distribution of monthly and total charges.
- Categorical variable analysis.
- Numerical variable analysis.
- Customer churn comparisons.

---

## Customer Churn Analysis

Customer churn was analysed to understand customer retention performance and identify groups with higher churn.

Key metrics analysed include:

- Total number of customers.
- Number of churned customers.
- Number of retained customers.
- Customer churn rate.
- Customer retention rate.

Churn was further explored across different customer characteristics, including:

- Contract type.
- Customer tenure.
- Payment method.
- Internet service.
- Customer segments.

---

## Customer Segmentation

Customers were segmented based on different aspects of customer behaviour and value.

Segmentation factors included:

- Customer tenure.
- Customer spending.
- Customer value.
- Number of subscribed services.
- Customer churn behaviour.

Customer profiles were created to help identify groups with different business characteristics, including:

- High-Value Loyal Customers
- High-Value Churned Customers
- New Customer Churned
- Low Engagement Customers
- Standard Customers

---

## Revenue Analysis

Revenue performance was analysed across customer segments to understand the financial contribution of different customer groups.

The analysis explored:

- Total revenue by customer segment.
- Customer value.
- Revenue contribution across customer groups.
- The relationship between customer retention and business value.

This helps identify valuable customer segments that may require greater attention and retention efforts.

---

## Business Insights and Recommendations

The analysis was used to generate business-focused recommendations aimed at improving customer retention.

Potential strategies include:

### High-Value Loyal Customers

- Develop loyalty programmes.
- Provide personalised offers.
- Offer priority customer support.

### New Customers at Risk of Churn

- Improve customer onboarding.
- Increase early customer engagement.
- Provide introductory incentives.

### Low Engagement Customers

- Develop personalised service recommendations.
- Promote relevant service bundles.
- Improve customer engagement.

### High-Value Customers at Risk of Churn

- Identify potential churn risks earlier.
- Develop proactive retention strategies.
- Provide targeted offers to protect valuable customers.

---

## Project Structure

```text
customer-retention/
│
├── app.py
├── requirements.txt
├── telco_customer_dashboard_data.csv
├── customer churn.ipynb
└── README.md
```

---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd customer-retention
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## Requirements

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

## Key Skills Demonstrated

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
- Streamlit
- Plotly

---

## Future Improvements

Potential future improvements to this project include:

- Developing a machine learning model to predict customer churn.
- Adding predictive customer risk scores.
- Performing feature importance analysis.
- Developing more advanced customer segmentation.
- Adding automated business insights to the dashboard.
- Connecting the dashboard to a live database.

---

## Author

**Joy Florence**

Aspiring Data Analyst | Business Analyst

Skills: Python | SQL | Excel | Power BI | Streamlit | Data Analysis