"""
timezone_issue_demo.py
A simple Python example showing how timezone mismatches cause unexpected execution times.
"""

import pendulum
from datetime import datetime, timedelta

# Simulate the scheduler being in UTC
scheduler_timezone = "UTC"
business_timezone = "Asia/Kolkata"

# Business requirement: run job daily at 08:00 IST
job_time_ist = pendulum.time(8, 0, 0)  # 8 AM IST

# Current UTC time (simulating server clock)
now_utc = pendulum.now(tz=scheduler_timezone)
print(f"[INFO] Current UTC Time: {now_utc}")

# Convert UTC time to IST
now_ist = now_utc.in_timezone(business_timezone)
print(f"[INFO] Current IST Time: {now_ist}")

# Calculate next run in UTC based on IST requirement
next_run_ist = pendulum.datetime(
    now_ist.year, now_ist.month, now_ist.day,
    job_time_ist.hour, job_time_ist.minute,
    tz=business_timezone
)

# If job time has already passed today in IST, schedule for tomorrow
if now_ist > next_run_ist:
    next_run_ist = next_run_ist.add(days=1)

# Convert IST run time to UTC (scheduler interprets in UTC)
next_run_utc = next_run_ist.in_timezone(scheduler_timezone)

print(f"[EXPECTED] Next Run Time in IST: {next_run_ist}")
print(f"[ACTUAL] Scheduler (UTC) will run at: {next_run_utc}")

"""
This will show that without timezone alignment, a job meant for 08:00 IST
runs at a completely different UTC time, potentially leading to missed runs.
"""
