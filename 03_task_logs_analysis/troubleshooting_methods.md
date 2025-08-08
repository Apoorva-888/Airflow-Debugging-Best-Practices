# Troubleshooting Using Airflow Logs

### Step 1 – Fetch Logs
- Use Airflow UI → Task Instance → View Log
- Or use `fetch_task_logs.py` to automate retrieval.

### Step 2 – Clean Logs
- Remove timestamps and ANSI color codes for easier searching.
- Normalize multi-line error messages.

### Step 3 – Look for Common Errors
- Python exceptions → check for `Traceback` lines.
- Memory issues → search for `OutOfMemoryError` or `Killed`.
- Network issues → search for `Connection refused` or `TimeoutError`.

### Step 4 – Identify Root Cause
- Match patterns against known Airflow / system issues.
- If the same error repeats → fix code or configuration.
- If different errors occur → check upstream dependencies.

### Step 5 – Validate Fix
- Rerun DAG after changes.
- Ensure logs are clean (no warnings or repeated errors).

---
**Pro Tip:** Automate parsing using `parse_logs_patterns.py` to quickly find recurring issues.
