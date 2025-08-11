# Astro Debug – Task Failure Simulation & Fix
This repository demonstrates how to **intentionally trigger** and then **fix** an Airflow task failure using Astronomer’s local development setup.

## 📌 Objective
- Learn how to **simulate** a broken DAG
- Explore **debugging techniques** for Airflow tasks
- Understand **how to fix** common issues
- Capture logs for future reference

## 📂 Project Structure
astro-debug-task-failure/
│
├── dags/
│ ├── failing_dag.py # Intentionally broken DAG
│ ├── fixed_dag.py # Corrected version
│
├── logs/
│ ├── sample_failure.log # Captured output of the failure
│
├── docker-compose.override.yml # Enable DEBUG-level logging
├── README.md # Step-by-step instructions + screenshots
└── packages.txt # Extra deps if needed

## 🛠 Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed & running  
- [Astronomer CLI](https://www.astronomer.io/docs/astro/cli/install-cli) installed  
- Basic Python knowledge  
- Airflow concepts (DAG, Task, Operator, Logs)  

