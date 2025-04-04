# Verify Log-In with Decorators

This project demonstrates the use of Python decorators to verify user credentials before granting access to specific functionality.

## Features

1. **Log-In Verification Decorator**:
   - The `verify_log_in` decorator checks if the provided username and password match the credentials stored in a `users.json` file.
   - If the credentials are valid, the decorated function is executed.
   - If the credentials are invalid, an error message is displayed, and the function is not executed.

2. **User Information Function**:
   - `user_information(user)`: Displays personal information about the logged-in user, such as their full name and email address.
   - This function is protected by the `verify_log_in` decorator.

3. **User Data**:
   - User credentials and personal information are stored in a `users.json` file.

## How It Works

- The `verify_log_in` decorator checks the provided username and password against the data in `users.json`.
- If the credentials are valid, the decorator passes the user's data to the decorated function.
- If the credentials are invalid, an error message is displayed, and the function is not executed.

### Example `users.json` File
The `users.json` file should be structured as follows:
```
{
    "user1": {
        "password": "password123",
        "full_name": "John Doe",
        "email": "johndoe@example.com"
    },
    "user2": {
        "password": "securepass456",
        "full_name": "Jane Smith",
        "email": "janesmith@example.com"
    },
    ...
}

```

## Example output
If the credentials are valid:
```
Successful login for the user 'user1'
User personal information:
Full name: John Smith
Email adress: john@example.com
```
If the creddentials are invalid:
```
Login failed. Verify your username and password
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
