# Airflow Debugging & Testing Best Practices
This repository contains practical examples, reproducible scenarios, and troubleshooting tips based on the **Astronomer Webinar: “Best Practices for Debugging and Testing Airflow Pipelines”**, along with additional real-world cases from production experience.
---
## 🛠 Use Cases Covered
### 1. **No DAGs Found**
- **Symptoms:** Airflow UI shows no DAGs despite them being in the `dags/` folder.
- **Root Cause:** Misconfigured `dags_folder` path, wrong file extension, or missing Python imports.
- **Resolution:** Verify `airflow.cfg`, ensure `.py` extensions, and check DAG syntax.
---
### 2. **DAGs Paused by Default**
- **Symptoms:** DAGs appear but are not running automatically.
- **Root Cause:** DAGs are created in a paused state (`is_paused_upon_creation=True`).
- **Resolution:** Unpause in UI or set `is_paused_upon_creation=False`.
---
### 3. **Missing Pools**
- **Symptoms:** Tasks stuck in "queued" state indefinitely.
- **Root Cause:** Tasks assigned to non-existent pools.
- **Resolution:** Create the pool via UI/CLI or remove `pool` parameter.
---
### 4. **DAG Parsing Failures**
- **Symptoms:** DAG not listed, parsing error in scheduler logs.
- **Root Cause:** Syntax errors, missing imports, or circular dependencies in DAG definition.
- **Resolution:** Run `airflow dags list` or check `scheduler.log` to identify and fix the code.
---
### 5. **Start Date & Scheduling Issues**
- **Symptoms:** DAG not triggering or triggering unexpectedly.
- **Root Cause:** `start_date` in the future, wrong timezone handling, or misuse of `catchup`.
- **Resolution:** Use timezone-aware datetimes, verify `catchup` parameter, adjust schedule.
---
### 6. **Task Dependency Deadlocks**
- **Symptoms:** DAG execution stuck because of circular dependencies.
- **Root Cause:** Incorrect use of `.set_upstream()` / `.set_downstream()` or bitshift operators.
- **Resolution:** Review DAG structure visually via Airflow Graph View and remove cycles.
---
### 7. **Environment Variable Misconfiguration**
- **Symptoms:** DAG works locally but fails in deployment.
- **Root Cause:** Missing or misconfigured environment variables.
- **Resolution:** Define variables in `airflow variables`, `.env` files, or Kubernetes secrets.
---
### 8. **Large XCom Size Causing Failures**
- **Symptoms:** Task fails with database write errors due to oversized XCom payloads.
- **Root Cause:** Returning large datasets instead of storing in external storage.
- **Resolution:** Store large data in S3/GCS and push only reference paths to XCom.
---
### 9. **Connection & Credential Issues**
- **Symptoms:** External system integrations fail despite correct credentials.
- **Root Cause:** Incorrect Airflow connection setup or missing `extra` parameters.
- **Resolution:** Use `airflow connections add` or UI to configure connections with correct JSON extras.
---
### 10. **Parallelism & Resource Limits**
- **Symptoms:** DAGs slow or queued even when workers are idle.
- **Root Cause:** Low `parallelism`, `max_active_runs_per_dag`, or executor settings.
- **Resolution:** Tune Airflow configs, adjust task concurrency, and monitor resource usage.
---
## 📚 Credits & Resources
**Credits**  
- **Webinar Host:** [Astronomer.io](https://www.astronomer.io/)  
- **Speaker:** Astronomer Airflow Experts Team  
- **Repo Author:** [Your Name]  
--
**Resources**  
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)  
- [Astronomer Airflow Guides](https://www.astronomer.io/guides/)  
- [Astronomer: Best Practices for Debugging and Testing Airflow Pipelines](https://www.astronomer.io/events/webinars/best-practices-debugging-testing-airflow/)  
- [Apache Airflow Official Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)  
- [Airflow Configuration Reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html)  
 

