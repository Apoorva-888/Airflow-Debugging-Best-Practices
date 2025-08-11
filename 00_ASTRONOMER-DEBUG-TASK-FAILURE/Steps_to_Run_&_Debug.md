## 🚀 Steps to Run & Debug
### 1️⃣ Clone this Repository
```bash
git clone https://github.com/yourusername/astro-debug-task-failure.git
cd astro-debug-task-failure
```
### 2️⃣ Start Astronomer Environment
```bash
astro dev start
```
This will spin up Airflow locally with the failing_dag.py included.
### 3️⃣ Trigger the Broken DAG
- Open Airflow UI → http://localhost:8080
- Locate failing_dag
- Trigger it manually
### 4️⃣ Observe Failure
- Task should fail intentionally
- Go to Logs → You’ll see the captured error (also saved in logs/sample_failure.log)
### 5️⃣ Enable Debug Logging (Optional but Recommended)
Edit docker-compose.override.yml:
```yaml
version: '3'
services:
  scheduler:
    environment:
      - AIRFLOW__CORE__LOGGING_LEVEL=DEBUG
  webserver:
    environment:
      - AIRFLOW__CORE__LOGGING_LEVEL=DEBUG
```
Then restart:
```bash
astro dev stop
astro dev start
```
### 6️⃣ Fix the DAG
- Replace failing_dag.py with fixed_dag.py (or rename in dags/)
- Restart Astronomer:
```bash
astro dev restart
```
- Trigger again → DAG should succeed

