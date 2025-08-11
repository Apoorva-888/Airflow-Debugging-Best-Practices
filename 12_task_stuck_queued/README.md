# Scenario 12 – Task Stuck in Queued State

## Overview

This example demonstrates a common Apache Airflow issue where a task gets stuck in the **queued** state and never progresses to **running** or **success**.

The cause can be due to:
- No available workers in the Celery/KubernetesExecutor pool.
- Scheduler not picking up queued tasks due to misconfiguration.
- Resource constraints (e.g., pool size limits, concurrency caps).
- Deadlocked worker processes.

This repository contains:
- A minimal reproducible Airflow DAG (`queued_task_example.py`) that simulates a stuck queued task.
- Realistic sample logs.
- Documentation for the issue and troubleshooting.
- Example dummy dataset (`data/dummy_input.csv`).

---

## Folder Contents

| File/Folder                   | Purpose                                                      |
|--------------------------------|--------------------------------------------------------------|
| `README.md`                   | This document.                                               |
| `ISSUE.md`                    | Detailed issue description, environment, and reproduction steps. |
| `TROUBLESHOOTING.md`          | Common causes and solutions for queued task issues.          |
| `sample_logs.txt`             | Realistic task logs showing the queued state.                |
| `dags/queued_task_example.py` | Airflow DAG reproducing the problem.                         |
| `data/dummy_input.csv`        | Dummy CSV file for the DAG to process.                       |

---

## Quick Start

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/airflow-debug-scenarios.git
   cd airflow-debug-scenarios/12_task_stuck_queued
```
