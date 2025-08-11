# Troubleshooting – Timezone Mismatch

# Step 1 – Verify Environment Timezone
Run:
```bash
date
timedatectl
```
Check if server/system time matches expected timezone.

### Step 2 – Check Application/Scheduler Timezone
In Airflow:
- airflow.cfg → default_timezone
- DAG definition timezone parameter

# Step 3 – Review Cron Interpretation
Example:
- IST job 0 8 * * *
- In UTC, this means 0 2 * * * (6 hours difference).

# Step 4 – Simulate Timezone Conversion
```
python
import pendulum
utc_time = pendulum.datetime(2025, 8, 11, 2, 0, tz="UTC")
ist_time = utc_time.in_timezone("Asia/Kolkata")
print(ist_time)
```

# Step 5 – Fix and Test
- Update timezone in scheduler config.
- Re-run DAG and confirm execution time.
- Document change for all environments.
