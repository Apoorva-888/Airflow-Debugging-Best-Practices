# plugin_coverage/operators/__init__.py
# Imports custom operator so it can be accessed at the package level if needed

from .s3_to_local_operator import S3ToLocalOperator

"""
Explanation:

This allows simplified imports:
Instead of from plugin_coverage.operators.s3_to_local_operator import S3ToLocalOperator,
you can use:  from plugin_coverage.operators import S3ToLocalOperator.
""'
