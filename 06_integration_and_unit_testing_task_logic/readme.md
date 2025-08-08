# Simple Data Engineering Pipeline
This is a minimal Python project demonstrating how to:
- Write simple **task logic** for a data engineering job.
- Run a **pipeline** that uses this logic.
- Test the logic with **unit tests**.
- Test the pipeline end-to-end with **integration tests**.
## Install dependencies
```pip install -r requirements.txt```
## Running the Pipeline
Run the pipeline script:
```bash
python my_pipeline.py
```
##  Running Tests
```bash
pytest tests/test_task_logic.py
pytest tests/test_integration_task.py
```
## Example
Sample Data Flow:
- task_logic.py: Reads a small dataset, filters rows, transforms data.
- my_pipeline.py: Calls the task logic and logs each step.
- Unit tests: Check that each function in task_logic.py works as expected.
- Integration tests: Check that the full pipeline runs correctly and produces the expected result.
## 🛠 Tech Stack
Python 3.9+
pytest for testing
Logging for tracking pipeline progress
## 📚 Notes
- This project is intentionally simplified to focus on:
- Structuring a Python project for data engineering tasks.
- Writing both unit and integration tests.
- Demonstrating best practices for logging and testing.


