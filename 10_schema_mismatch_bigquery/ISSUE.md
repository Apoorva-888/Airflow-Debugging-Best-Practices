# ❌ Issue – Schema Mismatch in BigQuery Load

## Problem
When loading CSV data into a BigQuery table, the **source file schema** does not match the **destination table schema**.

### Example
- **Expected Schema**:
  - id (INTEGER)
  - name (STRING)
  - score (FLOAT)
- **Source CSV**:
  - id (STRING)
  - name (STRING)
  - score (STRING)

## Error Message
```400 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/demo-project/jobs?uploadType=resumable:
Provided Schema does not match Table demo_dataset.demo_table. Field id has changed type from INTEGER to STRING
 ```

## Impact
- Load job fails
- Data pipeline breaks
- Downstream analytics delayed
