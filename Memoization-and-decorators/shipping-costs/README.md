# Shipping Costs Calculator with Memoization

This project demonstrates the use of Python's `functools.lru_cache` for memoization to optimize the calculation of shipping costs based on destination, distance, and weight.

## Features

1. **Shipping Cost Calculation**:
   - The `calculate_shipping_costs` function computes the total shipping cost using the formula:
     ```
     shipping_cost = 5 + distance * 0.1 + weight * 0.2
     ```
   - The function takes three parameters:
     - `destination`: The shipping destination (used for caching purposes).
     - `distance`: The distance to the destination in kilometers.
     - `weight`: The weight of the package in kilograms.

2. **Memoization**:
   - The function is decorated with `functools.lru_cache` to cache results for previously computed inputs, improving performance for repeated calls with the same parameters.

3. **Example Input**:
   - The script calculates the shipping cost for a predefined destination, distance, and weight.

## How It Works

- The `calculate_shipping_costs` function computes the shipping cost based on the provided parameters.
- The `functools.lru_cache` decorator caches the results of previous calculations, so if the function is called again with the same parameters, the cached result is returned instead of recalculating.

### Example Input and Output
The input parameters are defined as:
```
destination = "Barcelona"
distance = 250
weight = 8
```
Output:
```
Total shipping cost to Barcelona is 38.0 $
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
