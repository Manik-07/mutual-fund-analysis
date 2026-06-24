# Mutual Fund Analytics Project

## Overview

This project analyzes mutual fund data using Python, Pandas, SQL, and SQLite. The goal is to clean, validate, store, and analyze mutual fund datasets to generate meaningful business insights related to fund performance, investor behavior, NAV trends, and AUM growth.

## Project Objectives

* Clean and validate raw mutual fund datasets
* Design a star schema database using SQLite
* Load processed data into a relational database
* Perform analytical SQL queries
* Generate business insights from mutual fund performance and investor transactions
* Prepare the foundation for dashboarding and visualization

## Tools & Technologies

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* SQL
* Git & GitHub
* Jupyter Notebook

## Project Structure

```text
mutual-fund-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│   └── data_dictionary.md
│
├── bluestock_mf.db
└── README.md
```

## Day 1 Deliverables

* Project setup and folder structure
* Environment configuration
* Dependency installation
* Initial dataset exploration
* GitHub repository setup

## Day 2 Deliverables

* Cleaned NAV History dataset
* Cleaned Investor Transactions dataset
* Cleaned Scheme Performance dataset
* SQLite Star Schema Design
* Database creation and loading
* Row count validation
* 10 Analytical SQL Queries
* Data Dictionary documentation

## Key Analytical Queries

* Top 5 Funds by AUM
* Average NAV per Month
* SIP Transaction Analysis
* Transactions by State
* Expense Ratio Analysis
* Fund Performance Comparison

## Database Schema

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance

## Results

* Successfully cleaned and validated datasets
* Loaded data into SQLite database
* Verified row count consistency
* Generated analytical SQL queries for business insights

## Future Enhancements

* Exploratory Data Analysis (EDA)
* Interactive Dashboard (Power BI / Tableau)
* Investor Segmentation
* Fund Performance Visualization
* Predictive Analytics

## Author

**Manik Soodan**

B.Tech Computer Science Engineering
Data Analytics & AI/ML Enthusiast
