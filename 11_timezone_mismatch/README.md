# Scenario 11 – Timezone Mismatch Causing Missed Runs
This scenario demonstrates how timezone configuration mismatches between an orchestration tool (like Airflow) and the system/server timezone can cause scheduled jobs to run at incorrect times or be missed entirely.
## 📌 Problem Summary
- **Symptom:** Jobs not running at the expected time.
- **Root Cause:** Mismatch between:
  - System timezone
  - Scheduler timezone
  - Cron expression interpretation
- **Impact:** Data pipelines run too early, too late, or skip runs.
## 📂 Files in this Folder
- **ISSUE.md** → Detailed description of the problem.
- **troubleshooting.md** → Steps to diagnose and fix the issue.
- **sample_logs.txt** → Example logs showing timezone discrepancies.
- **timezone_issue_demo.py** → A Python example simulating the timezone problem.
## 🛠 Common Fixes
- Align scheduler timezone with business requirement (e.g., UTC vs local time).
- Verify cron expressions under intended timezone.
- Use explicit timezone conversion in datetime operations.
