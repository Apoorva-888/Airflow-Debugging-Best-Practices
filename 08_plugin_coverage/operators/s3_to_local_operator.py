# plugin_coverage/operators/s3_to_local_operator.py

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import boto3
import os

class S3ToLocalOperator(BaseOperator):
    """
    Custom Airflow operator to download a file from an S3 bucket to a local file path.

    Parameters:
    - bucket_name: str - S3 bucket name
    - s3_key: str - S3 object key (path to the file in the bucket)
    - local_path: str - Destination path on the local file system
    - aws_conn_id: str - Optional AWS connection ID (not used in this basic version)
    """

    @apply_defaults
    def __init__(self, bucket_name, s3_key, local_path, aws_conn_id=None, **kwargs):
        super().__init__(**kwargs)
        self.bucket_name = bucket_name
        self.s3_key = s3_key
        self.local_path = local_path
        self.aws_conn_id = aws_conn_id  # Optional: for future integration with Airflow's S3Hook

    def execute(self, context):
        """
        Executes the download from S3 using boto3.

        This version uses default credentials from environment or IAM role.
        """
        self.log.info(f"Starting S3 download: bucket={self.bucket_name}, key={self.s3_key}")

        try:
            # Ensure the local directory exists
            os.makedirs(os.path.dirname(self.local_path), exist_ok=True)

            # Use boto3 to download the file
            s3 = boto3.client('s3')
            s3.download_file(self.bucket_name, self.s3_key, self.local_path)

            self.log.info(f"Successfully downloaded to: {self.local_path}")
        except Exception as e:
            self.log.error(f"Failed to download file from S3: {e}")
            raise
