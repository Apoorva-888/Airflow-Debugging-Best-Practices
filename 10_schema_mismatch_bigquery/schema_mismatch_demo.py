"""
Schema Mismatch Demo – BigQuery
--------------------------------
This script simulates loading CSV data into a BigQuery table
with a mismatched schema. It will fail intentionally to
demonstrate the error.
"""

from google.cloud import bigquery
from google.api_core.exceptions import BadRequest

# Set your variables
PROJECT_ID = "your-gcp-project-id"
DATASET_ID = "demo_dataset"
TABLE_ID = "demo_table"
FILE_PATH = "data/sample_input_data.csv"

# Create BigQuery client
client = bigquery.Client(project=PROJECT_ID)

# Configure the job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    schema=[
        bigquery.SchemaField("id", "INTEGER"),  # Expected integer, CSV has string
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("score", "FLOAT")
    ]
)

try:
    print("🚀 Starting BigQuery load job...")
    with open(FILE_PATH, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}",
            job_config=job_config
        )
    load_job.result()  # Wait for job to complete
    print("✅ Load job completed successfully!")

except BadRequest as e:
    print("❌ Load job failed due to schema mismatch.")
    print("Error details:")
    for err in e.errors:
        print(f"- {err['message']}")
