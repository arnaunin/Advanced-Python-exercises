# Subarray Optimization with Memoization

This project demonstrates the use of Python's `functools.lru_cache` for memoization to optimize the calculation of the maximum sum of a contiguous subarray using Kadane's algorithm.

## Features

1. **Maximum Subarray Sum**:
   - The `max_sub_array_sum` function calculates the maximum sum of a contiguous subarray and returns both the sum and the subarray itself.
   - Implements Kadane's algorithm for efficient computation.

2. **Memoization**:
   - The function is decorated with `functools.lru_cache` to cache results for previously computed inputs, improving performance for repeated calls with the same input.

3. **Example Input**:
   - The script processes a predefined array of integers and prints the results.

## How It Works

- The function iterates through the array, maintaining the current sum of the subarray and the maximum sum encountered so far.
- If adding the current number to the subarray decreases the sum, the subarray is reset to start from the current number.
- The function uses memoization to cache results for repeated calls with the same input, reducing redundant computations.

### Example Input and Output
The input array is defined as:
```
array = tuple([1, -2, 3, 10, -4, 7, 2, -5, -2])
```
Output:
```
Maximum sum of contiguous subarray: 18
Contiguous subarray with maximum sum: [1, -2, 10, -4, 7, 2]
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
