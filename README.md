# Healthcare Data Engineering Pipeline

## About
This is a personal data engineering project where I built a pipeline using synthetic healthcare data. It works with three datasets: providers, members, and claims.

## What I built
- **Bronze:** Loaded the raw CSV files into Databricks and stored them as Delta tables.
- **Silver:** Cleaned the data by handling duplicate claims, converting data types, standardizing regions, and identifying invalid claim amounts and member/provider references.
- **Gold:** Created summary tables showing claim counts and total claim amounts by region and claim status.
- **Data Quality Checks:** Added automated checks for duplicate claim IDs, invalid amounts, null IDs, and invalid member/provider references.
- **Workflow:** Configured Databricks Workflows to run the Bronze, Silver, Gold, and data quality notebooks in sequence.

## Tools used
Python, PySpark, SQL, Azure Databricks, Delta tables, Git, and GitHub.

## Data
I generated small synthetic datasets for this project. No real patient data or employer data is used.
