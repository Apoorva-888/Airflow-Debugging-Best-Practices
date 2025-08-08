# Troubleshooting – How to Measure Failure Duration

## Method 1 – Query Airflow Metadata DB
1. Connect to the Airflow metadata database.
2. Run `query_failure_duration.sql`.
3. Check the `first_failure_time` and `last_failure_time` columns.
4. Subtract to get the failure duration.

## Method 2 – Use Airflow REST API
1. Enable the Airflow REST API in `airflow.cfg`.
2. Run `failure_duration_check.py`.
3. The script will print the total duration of failures.

## Method 3 – Check Airflow UI (Manual)
1. Go to **Graph View**.
2. Click the failed task.
3. Review past runs and manually note the first and last failure times.

**Recommendation:** Use Method 1 or 2 for automation in monitoring systems.
