# Troubleshooting – S3 Data Delay

## Symptoms
- DAG fails in the processing task.
- Error in logs: `FileNotFoundError` for `input_data.csv`.

## Root Cause
Data was not present in the S3 bucket at DAG runtime due to delay in upstream process.

## Debugging Steps
1. **Check logs**:
cat logs/sample_failure.log
2. **Check S3 manually**:
aws s3 ls s3://your-bucket/path/
3. **Verify upstream job completion**:
Ensure that the upstream job pushing data to S3 completed successfully.
5. **Check DAG code for sensors**:
If there’s no `S3KeySensor`, the DAG may be starting without waiting for the file.

## Resolution
- Add an `S3KeySensor` or `ExternalTaskSensor` to ensure data availability.
- Adjust `poke_interval` and `timeout` values as per SLA.
- Optionally, set `retries` for transient S3 delays.

## Prevention
- Implement data availability checks before processing.
- Set up monitoring/alerting for delayed S3 data uploads.

