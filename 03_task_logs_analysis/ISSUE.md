## Problem Statement
We need a repeatable process to:
1. Fetch logs for a specific DAG run / task instance.
2. Clean & normalize the log format.
3. Detect recurring error patterns or unusual behaviors.

## Root Cause Possibilities
- Syntax errors in task scripts.
- Incorrect configuration of connections or variables.
- Memory exhaustion or worker crashes.
- Upstream system downtime.

## Key Questions
- Is the failure consistent or intermittent?
- Do logs point to the same error message every time?
- Are there warnings that appear before the actual error?
