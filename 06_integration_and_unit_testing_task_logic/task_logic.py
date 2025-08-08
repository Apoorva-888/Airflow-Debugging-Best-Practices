# task_logic.py
# This file contains the main processing logic for our pipeline.

def clean_data(data):
    """
    Cleans the data by:
    - Stripping spaces
    - Converting text to lowercase
    """
    return [item.strip().lower() for item in data]

def transform_data(data):
    """
    Transforms the data by:
    - Adding a prefix 'processed_' to each string
    """
    return [f"processed_{item}" for item in data]
