### 📄 `issues.md`


# Known Issues with DAG Validation

- ❌ `AttributeError: 'module' object has no attribute 'dag'`  
  - ➤ DAG not defined as a top-level variable (`dag = DAG(...)` missing)

- ❌ `ImportError` or `SyntaxError`  
  - ➤ Syntax issues in your DAG file

- ❌ `AssertionError: Loaded object is not a DAG`  
  - ➤ DAG not instantiated or incorrectly referenced
