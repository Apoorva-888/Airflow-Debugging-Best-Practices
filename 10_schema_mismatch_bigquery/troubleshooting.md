# 🛠 Troubleshooting – Schema Mismatch in BigQuery

# Step 1 – Check Schema in BigQuery
```sql
SELECT column_name, data_type
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'demo_table';
```

# Step 2 – Inspect Input File
```bash
head -n 5 data/sample_input_data.csv
```
# Step 3 – Compare Schemas
Ensure data types match
Ensure column names match exactly (case-sensitive)
Ensure column order matches (if using schema auto-detect OFF)

# Step 4 – Possible Fixes
Update Source File to match schema before load.
Update BigQuery Table Schema (if change is intended).
Use schema auto-detection (only for compatible changes).
Transform data before loading (e.g., cast types using Dataflow, Pandas, or PySpark).
