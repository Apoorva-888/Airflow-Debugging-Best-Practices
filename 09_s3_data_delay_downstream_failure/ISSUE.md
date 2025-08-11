## Title
S3 Data Delay Causing Downstream Task Failure in DAG

## Description
When the expected data file is not present in the S3 location at DAG runtime, the downstream processing task fails with a `FileNotFoundError`.

## Environment
- Airflow 2.7.3
- Python 3.10
- AWS S3 (simulated locally)

## Steps to Reproduce
1. Remove or rename `data/input_data.csv`.
2. Trigger `s3_data_delay_example` DAG.
3. Observe failure in downstream task.

## Expected Behavior
The DAG should either:
- Wait for the data before proceeding.
- Or gracefully skip downstream processing.

## Actual Behavior
DAG fails immediately with the following error:
