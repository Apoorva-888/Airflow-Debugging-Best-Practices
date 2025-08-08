# tests/test_integration_task.py
# Integration test for the whole pipeline

from my_pipeline import run_pipeline

def test_pipeline():
    result = run_pipeline()
    expected = ["processed_apple", "processed_banana", "processed_cherry"]
    assert result == expected  # Pipeline should process all steps correctly
