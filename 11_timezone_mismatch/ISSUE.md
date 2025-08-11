# Issue – Timezone Mismatch Causing Missed Runs

**Date Reported:** 2025-08-11  
**Environment:** Airflow 2.7.0 on Kubernetes (UTC default)  
**Reporter:** Data Engineering Team

## ❗ Problem
Scheduled job supposed to run daily at 08:00 IST is instead running at 02:30 IST.

## 🕵 Observations
1. Airflow's `default_timezone` was `UTC`.
2. Cron expression `0 8 * * *` was interpreted in UTC, not IST.
3. Pipeline dependency assumed local India time.

## 📜 Evidence
See `sample_logs.txt` for timestamps showing the mismatch.

## 💡 Potential Solutions
- Configure Airflow:  
  ```python
  default_timezone = pendulum.timezone("Asia/Kolkata")
```
Use pendulum to convert UTC to IST.
Adjust cron expression to 30 2 * * * UTC if UTC timezone must remain.
