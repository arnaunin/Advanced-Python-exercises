# Logger Decorator

This project demonstrates the use of Python decorators to log information about a function's execution, including its runtime and any errors that occur during execution.

## Features

1. **Logger Decorator**:
   - Logs the following details about a function:
     - When the function is invoked.
     - If an error occurs during execution.
     - How long the function takes to execute.

2. **Fibonacci Function**:
   - Calculates the first 20 numbers in the Fibonacci series.
   - The function is wrapped with the `logger` decorator to log its execution details.

## How It Works

The `logger` decorator wraps a function and provides additional functionality:
- It records the start time before the function is executed.
- It catches and logs any exceptions raised by the function.
- It calculates and logs the total execution time of the function.

## Example Output
```
Invoking the function 'fibonacci'...
Function 'fibonacci' took 4.696846008300781e-05 seconds to run.
Functon results: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
