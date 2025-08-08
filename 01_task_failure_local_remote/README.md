# Use Case 1 – Task Failure (Local or Remote) in Apache Airflow
This guide documents how to troubleshoot Airflow task failures occurring either on a **local development environment** or a **remote production/deployment environment**.
## Objective
- Identify root causes of Airflow task failures.
- Learn structured debugging techniques.
- Provide reproducible test cases and logs.
## Context
In Airflow, a DAG task can fail due to:
- **Local Issues** (e.g., missing dependencies, misconfigured environment, wrong Python version)
- **Remote Issues** (e.g., infrastructure failure, Airflow worker crash, missing credentials in prod)
## Files in this Folder
- `ISSUE.md` → Problem statement & root cause.
- `task_failure_local.py` → DAG simulating a local task failure.
- `task_failure_remote.py` → DAG simulating a remote task failure.
- `troubleshooting_methods.md` → Step-by-step debugging strategies.
- `logs/` → Real sample logs from local & remote failures.
## Quick Start
1. Clone repo & set up Airflow locally.
2. Place DAGs in your Airflow `dags/` folder.
3. Trigger each DAG to reproduce the issue.
4. Compare your logs to the provided samples.
