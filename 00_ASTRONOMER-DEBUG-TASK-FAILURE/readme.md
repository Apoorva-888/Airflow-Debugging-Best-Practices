# Astro Debug – Task Failure Simulation & Fix
This repository demonstrates how to **intentionally trigger** and then **fix** an Airflow task failure using Astronomer’s local development setup.

## 📌 Objective
- Learn how to **simulate** a broken DAG
- Explore **debugging techniques** for Airflow tasks
- Understand **how to fix** common issues
- Capture logs for future reference

### 📂 Project Structure
Folder / File               | Description
----------------------------|-----------------------------------------------------
dags                        | Folder containing Airflow DAG files
failing_dag.py              | Intentionally broken DAG to simulate failure
fixed_dag.py                | Corrected DAG version with error handling
logs                        | Folder storing sample logs from DAG runs
sample_failure.log          | Captured output of the failure
Steps_to_Run_&_Debug.md     | Step-by-step instructions to run and debug locally
docker-compose.override.yaml| Override to enable DEBUG logging in Airflow
packages.txt                | Lists extra Python dependencies (e.g., requests)
README.md                   | Project overview and instructions


### 🛠 Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed & running  
- [Astronomer CLI](https://www.astronomer.io/docs/astro/cli/install-cli) installed  
- Basic Python knowledge  
- Airflow concepts (DAG, Task, Operator, Logs)  

