# Schema Mismatch in Data Warehouse Load (BigQuery)

## 📌 Overview
This scenario simulates a schema mismatch issue when loading data into **BigQuery**.  
It’s common when source data fields, types, or column order do not match the expected **BigQuery table schema**.

## 🛠 What’s Included
- `schema_mismatch_demo.py` → A Python script that tries to load CSV data to BigQuery but fails due to schema mismatch.
- `sample_input_data.csv` → Example input data causing schema mismatch.
- `bigquery_expected_schema.json` → BigQuery table schema definition.
- `sample_logs.txt` → Sample error logs from BigQuery load job.
- `ISSUE.md` → Detailed explanation of the issue.
- `troubleshooting.md` → Steps to debug and fix.

## ⚙ Prerequisites
- Python 3.x
- Google Cloud SDK (`gcloud`)
- BigQuery Python Client (`pip install google-cloud-bigquery`)

## ▶ How to Run
```bash
# Authenticate GCP
gcloud auth application-default login

# Run the script
python schema_mismatch_demo.py
