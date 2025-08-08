## Problem Statement
We need to find out how long a particular Airflow task has been failing without manually checking the UI for every run.

## Root Cause
Airflow UI does not directly show a "failure duration" metric, so we must compute it using either database queries or API calls.

## Symptoms
- Multiple consecutive task failures.
- Increased SLA misses.
- Downstream jobs delayed.

## Impact
Without knowing the exact duration of failure, prioritization of incident response becomes guesswork.
