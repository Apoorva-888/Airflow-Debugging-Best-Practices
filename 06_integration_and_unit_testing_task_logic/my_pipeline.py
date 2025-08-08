# my_pipeline.py
# This is the main script to run the pipeline.

from task_logic import clean_data, transform_data

def run_pipeline():
    # Step 1: Raw input data
    raw_data = ["  Apple", "BANANA ", " Cherry  "]

    # Step 2: Clean the data
    cleaned = clean_data(raw_data)

    # Step 3: Transform the data
    transformed = transform_data(cleaned)

    # Step 4: Print results (in real case, you might save to database/S3)
    print("Final Processed Data:", transformed)
    return transformed

if __name__ == "__main__":
    run_pipeline()
