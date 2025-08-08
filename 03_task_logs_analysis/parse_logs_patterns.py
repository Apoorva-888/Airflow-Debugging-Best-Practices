"""
Parse Airflow logs for error patterns and save a summary.
"""

import re
import json

input_file = "sample_logs/raw_airflow_log.txt"
output_clean_file = "sample_logs/cleaned_log.txt"
output_summary_file = "sample_logs/error_summary.json"

error_patterns = {
    "python_exception": r"Traceback \(most recent call last\):",
    "oom_killed": r"OutOfMemoryError|Killed",
    "connection_error": r"(Connection refused|TimeoutError|OperationalError)",
    "airflow_fail": r"Task failed with exception",
}

def clean_logs():
    with open(input_file, "r") as f:
        lines = f.readlines()
    # Remove ANSI color codes & timestamps for easier reading
    cleaned = [re.sub(r"\x1B\[[0-9;]*[mK]", "", line) for line in lines]
    cleaned = [re.sub(r"^\[\d{4}-\d{2}-\d{2}.*?\]", "", line) for line in cleaned]
    with open(output_clean_file, "w") as f:
        f.writelines(cleaned)

def detect_patterns():
    with open(output_clean_file, "r") as f:
        content = f.read()
    summary = {}
    for key, pattern in error_patterns.items():
        matches = re.findall(pattern, content)
        summary[key] = len(matches)
    with open(output_summary_file, "w") as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    clean_logs()
    detect_patterns()
    print("✅ Log parsing complete. Outputs in sample_logs/")
