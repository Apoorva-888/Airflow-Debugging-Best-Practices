# Scenario 1 – S3 Data Delay Causing Downstream Failure

## Overview
This scenario simulates an **S3 data delay** that causes a downstream Airflow DAG task to fail.  
It demonstrates:
- How S3 unavailability or late-arriving data impacts DAG execution.
- How to capture failure logs for debugging.
- Steps to troubleshoot and resolve.

## How to Reproduce
1. Run the `s3_data_delay_example.py` DAG in Airflow.
2. The first task checks for data in an S3 bucket (simulated locally).
3. The downstream task tries to process data but fails if data is missing.

## Folder Contents
- `dags/s3_data_delay_example.py` → DAG simulating data dependency failure.
- `logs/sample_failure.log` → Realistic failure logs from Airflow.
- `ISSUE.md` → Root cause and description of the problem.
- `troubleshooting.md` → Step-by-step debugging and resolution.
- `data/input_data.csv` → Dummy dataset (optional).

## Airflow Version
Tested on:
- Apache Airflow 2.7+
- Python 3.10+

## Notes
You can simulate the delay by removing `data/input_data.csv` before running the DAG.
