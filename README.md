# customer-retention
# Telco Customer Churn & Retention Analysis

## Project Overview

This project analyses customer churn patterns using the Telco Customer Churn dataset. The goal is to understand customer behaviour, identify factors associated with customer churn, segment customers based on their value and engagement, and generate actionable business recommendations to improve customer retention.

The analysis combines data cleaning, exploratory data analysis (EDA), customer segmentation, churn analysis, and revenue analysis to provide meaningful insights into customer behaviour and business performance.

---

## Business Problem

Customer churn can significantly affect a company's revenue and long-term growth. Understanding why customers leave and identifying customer groups that require attention can help businesses develop more effective retention strategies.

This project aims to answer questions such as:

- What percentage of customers churn?
- Which customer characteristics are associated with churn?
- How does customer tenure relate to churn?
- Do monthly charges influence customer churn?
- Which contract types experience higher churn?
- Which customer segments generate the most revenue?
- Which customer groups should be prioritised for retention strategies?

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

The project was completed using:

- **Python**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualisation
- **KaggleHub** – Dataset access
- **Jupyter Notebook / VS Code** – Data analysis environment

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






