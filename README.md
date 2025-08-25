# Airflow Debugging & Testing Best Practices
A practical guide and set of examples for debugging and testing Apache Airflow pipelines.This repository contains reproducible scenarios, real-world troubleshooting cases, and best practices distilled from the Astronomer Webinar **"Best Practices for Debugging and Testing Airflow Pipelines"** plus additional production experiences.

## 📌 Overview
Working with Airflow in production inevitably involves dealing with failing DAGs, import errors, misconfigured tasks, and tricky runtime bugs.  
This project aims to:
- Provide **ready-to-run examples** for different Airflow debugging scenarios.
- Demonstrate **testing workflows** for DAGs and tasks.
- Share **best practices** for building maintainable Airflow pipelines.
- Offer **troubleshooting guides** and logs for faster resolution.

## 🛠 Use Cases Covered
- **01_task_failure_local_remote**  
  Demonstrates diagnosing and resolving task failures when running locally versus in a remote Airflow environment.

- **02_task_failure_duration**  
  Shows how to debug tasks that fail due to excessive execution time or timeout settings.

- **03_task_logs_analysis**  
  Focuses on collecting, reviewing, and interpreting Airflow logs to identify root causes of failures.

- **04_api_permission_issues**  
  Highlights troubleshooting steps for tasks failing due to insufficient API permissions or authentication errors.

- **05_Unit_Testing_DAG_Configuration_&_Parsing**  
  Covers how to write and run unit tests to validate DAG parsing and configuration correctness.

- **06_integration_and_unit_testing_task_logic**  
  Explains strategies for combining integration tests with unit tests to verify task logic end-to-end.

- **07_dag_validation**  
  Provides examples of programmatically validating DAG structure, dependencies, and metadata before deployment.

- **08_plugin_coverage**  
  Demonstrates how to test and ensure coverage for custom Airflow plugins.

- **09_s3_data_delay_downstream_failure**  
  Shows how to handle and debug downstream task failures caused by delayed data arrival in S3.

- **10_schema_mismatch_bigquery**  
  Explains detecting and fixing schema mismatches when loading data into BigQuery.

- **11_timezone_mismatch**  
  Highlights issues arising from timezone differences in scheduling, execution, and data processing.

- **12_task_stuck_queued**  
  Provides guidance on diagnosing and resolving tasks that remain indefinitely in the `queued` state.

## 🙌 Credits

This project was inspired by and builds upon knowledge shared by experts at Astronomer:
- **Kenten Danas** – Senior Manager, Developer Relations, Astronomer  
- **Jake Roach** – Associate Sales Engineer, Astronomer  
- **Chris Munn** – Associate Sales Engineer, Astronomer
-  Webinar Host: [Astronomer.io](https://www.astronomer.io/)  
-  Speaker: Astronomer Airflow Experts Team  

## Resources
 [Apache Airflow Documentation](https://airflow.apache.org/docs/)  
 [Astronomer Airflow Guides](https://www.astronomer.io/guides/)  
 [Astronomer: Best Practices for Debugging and Testing Airflow Pipelines](https://www.astronomer.io/events/webinars/best-practices-debugging-testing-airflow/)  
 [Apache Airflow Official Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)  
 [Airflow Configuration Reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html)  

## 🛠️ Languages & Tools
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Queries-orange?logo=databricks&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.x-darkblue?logo=apacheairflow&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Scripts-black?logo=gnu-bash&logoColor=white)

 

