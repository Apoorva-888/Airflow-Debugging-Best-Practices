-- Query to find the first and last failure time of a task
SELECT
    dag_id,
    task_id,
    MIN(start_date) AS first_failure_time,
    MAX(end_date) AS last_failure_time,
    COUNT(*) AS failure_count
FROM
    task_instance
WHERE
    dag_id = 'your_dag_id'
    AND task_id = 'your_task_id'
    AND state = 'failed'
GROUP BY
    dag_id, task_id;
