# 🔌 Plugin Coverage – Custom Airflow Operator Testing
This module contains a custom Airflow operator (`S3ToLocalOperator`) that downloads a file from an S3 bucket to the local filesystem.
It also includes a suite of unit tests that mock external AWS interactions using `unittest.mock`.
---
## 📦 Operator
**`S3ToLocalOperator`**
- Downloads a file from S3 using `boto3`
- Parameters:
  - `bucket_name`: Name of the S3 bucket
  - `s3_key`: Key/path of the file in S3
  - `local_path`: Destination path on the local file system
  - `aws_conn_id`: (optional) for future integration with Airflow's `S3Hook`
---
## 🧪 Tests
Located in: `test_operators/test_s3_to_local_operator.py`
- ✅ Operator initialization
- ✅ Successful execution (mocked)
- ✅ Failure handling
---
## 🏃‍♂️ Run Tests
```bash
pytest plugin_coverage/
```
