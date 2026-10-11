# Healthcare Data Engineering Pipeline

An end-to-end data engineering project built with **Azure Databricks, PySpark, and Delta Lake**, demonstrating incremental data ingestion, multi-layer transformations, data quality validation, and analytical data modelling using synthetic healthcare datasets.

## Project Overview

This project processes claims, members, and providers data through a structured Bronze–Silver–Gold architecture. Databricks Workflows orchestrate the pipeline, while incremental processing handles newly generated claim batches.

## Architecture

**Raw CSV → Bronze (Raw Ingestion) → Silver (Cleansing & Validation) → Gold (Analytics)**

## Key Features

### 1. Bronze Layer — Data Ingestion
- Ingested raw claims, members, and providers CSV datasets into Delta tables.
- Implemented batch-based incremental ingestion to process newly generated claim data.
- Preserved a raw-data layer for downstream transformations and validation.

### 2. Silver Layer — Data Transformation
- Applied PySpark transformations and data type conversions.
- Identified duplicate claim IDs and validated claim amounts.
- Standardized regional values and checked member/provider referential integrity.
- Processed incremental claims while preventing duplicate claim IDs in Silver.

### 3. Gold Layer — Analytical Modelling
- Built aggregated Delta tables for claim metrics by region and claim status.
- Calculated claim counts and total claim amounts to support downstream reporting.
- Refreshed analytical summaries from the latest Silver-layer data.

### 4. Data Quality & Validation
Implemented automated checks covering:
- Duplicate and blank claim IDs.
- Null identifiers and invalid claim amounts.
- Invalid member and provider references.

### 5. Workflow Orchestration
- Configured Databricks Workflows to execute ingestion, transformation, analytics, and validation notebooks in sequence.
- Tested the pipeline with multiple incremental batches and repeated workflow executions.

## Technology Stack

**Languages:** Python, SQL  
**Processing:** PySpark  
**Platform:** Azure Databricks  
**Storage:** Delta Lake, CSV  
**Orchestration:** Databricks Workflows  
**Version Control:** Git, GitHub

## Repository Structure

```text
healthcare-data-engineering-pipeline/
├── data/raw/
│   ├── claims.csv
│   ├── members.csv
│   └── providers.csv
├── notebooks/
│   ├── 01_explore_raw_data.ipynb
│   ├── 02_bronze_ingestion.ipynb
│   ├── 03_silver_transformation.ipynb
│   ├── 04_gold_analytics.ipynb
│   └── 05_data_quality_checks.ipynb
├── src/
├── .gitignore
└── README.md
```

### Data Quality & Validation

- Implemented automated checks for duplicate claim IDs, invalid claim amounts, missing identifiers, and invalid member/provider references.
- Validated transformed data before downstream analytical processing.

## Dataset

All datasets are synthetically generated for learning and demonstration. No real patient data or employer data is used.