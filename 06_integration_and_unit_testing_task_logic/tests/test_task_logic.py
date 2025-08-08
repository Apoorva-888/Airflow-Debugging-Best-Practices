# tests/test_task_logic.py
# Unit tests for individual functions in task_logic.py

from task_logic import clean_data, transform_data

def test_clean_data():
    data = ["  Apple", "BANANA "]
    result = clean_data(data)
    assert result == ["apple", "banana"]  # Expected cleaned output

def test_transform_data():
    data = ["apple", "banana"]
    result = transform_data(data)
    assert result == ["processed_apple", "processed_banana"]
