# Access Control with Decorators

This project demonstrates the use of Python decorators to implement access control based on the environment in which the code is executed.

## Features

1. **Access Control Decorator**:
   - The `verify_access_environment` decorator restricts access to certain functions unless the environment is set to `production`.
   - If the environment is not `production`, access to the function is denied, and a message is displayed.

2. **Document Management Functions**:
   - `upload_document(document)`: Simulates uploading a document.
   - `delete_document(document)`: Simulates deleting a document.
   - Both functions are wrapped with the `verify_access_environment` decorator to enforce access control.

3. **Environment Check**:
   - The `get_environment()` function determines the current environment. In this example, it is hardcoded to return `'production'`.

## How It Works

- The `verify_access_environment` decorator checks the current environment before allowing access to the decorated function.
- If the environment is `'production'`, the function executes normally.
- If the environment is not `'production'`, access is denied, and the function is not executed.

## Example Output
When running the script with the environment set to `'production'`, the output might look like this:
```
Access was allowed in the production environment
Document deleted
```
When running the script with the environment not set to `'production'`, the output might look like this:
```
Access is restricted to production environments
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
