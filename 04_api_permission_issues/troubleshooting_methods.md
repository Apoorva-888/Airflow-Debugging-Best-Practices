# Troubleshooting 403 Forbidden in Airflow Tasks

### Step 1 – Confirm the API URL and Endpoint
- Ensure the endpoint is correct and not restricted to certain IP ranges.

### Step 2 – Validate Credentials
- Retrieve Airflow connection credentials (`airflow connections get my_conn_id`).
- Verify the token locally with `curl` or `Postman`.

### Step 3 – Check Token Expiry
- If JWT or OAuth, decode and confirm expiration time.
- Refresh the token if needed.

### Step 4 – Review External System Permissions
- Confirm the service account has correct roles/permissions for the API resource.

### Step 5 – Test From Airflow Worker
- SSH into the worker container and run the request manually to confirm network & credentials.

---
**Pro Tip:** Store API tokens in Airflow connections, not hard-coded in DAGs.
