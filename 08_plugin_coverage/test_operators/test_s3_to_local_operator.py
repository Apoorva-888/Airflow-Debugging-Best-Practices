"""
Explanation:
test_operator_initialization: ensures parameters are passed correctly.
test_operator_execute_success: uses unittest.mock.patch to mock boto3.client() and validate it’s called correctly.
test_operator_execute_failure: simulates a failed download and checks for exception handling.
"""
# plugin_coverage/test_operators/test_s3_to_local_operator.py

import pytest
from unittest.mock import patch, MagicMock
from airflow.models.dag import DAG
from datetime import datetime

from plugin_coverage.operators import S3ToLocalOperator

@pytest.fixture
def default_dag():
    """
    Provides a simple DAG object to attach the operator to during tests.
    """
    return DAG(dag_id='test_dag', start_date=datetime(2023, 1, 1))

def test_operator_initialization(default_dag):
    """
    Test that the operator initializes correctly with the given arguments.
    """
    op = S3ToLocalOperator(
        task_id='test_task',
        bucket_name='my-bucket',
        s3_key='data/test.csv',
        local_path='/tmp/test.csv',
        dag=default_dag
    )

    assert op.bucket_name == 'my-bucket'
    assert op.s3_key == 'data/test.csv'
    assert op.local_path == '/tmp/test.csv'

@patch('plugin_coverage.operators.s3_to_local_operator.boto3.client')
def test_operator_execute_success(mock_boto_client, default_dag):
    """
    Test that the operator calls boto3.download_file with the correct parameters.
    """
    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3

    op = S3ToLocalOperator(
        task_id='test_task',
        bucket_name='my-bucket',
        s3_key='data/test.csv',
        local_path='/tmp/test.csv',
        dag=default_dag
    )

    op.execute(context={})

    mock_s3.download_file.assert_called_once_with('my-bucket', 'data/test.csv', '/tmp/test.csv')

@patch('plugin_coverage.operators.s3_to_local_operator.boto3.client')
def test_operator_execute_failure(mock_boto_client, default_dag):
    """
    Test that the operator raises an exception when boto3.download_file fails.
    """
    mock_s3 = MagicMock()
    mock_s3.download_file.side_effect = Exception("Download failed")
    mock_boto_client.return_value = mock_s3

    op = S3ToLocalOperator(
        task_id='test_task',
        bucket_name='bad-bucket',
        s3_key='missing.csv',
        local_path='/tmp/missing.csv',
        dag=default_dag
    )

    with pytest.raises(Exception, match="Download failed"):
        op.execute(context={})
