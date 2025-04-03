# Sales Data Analysis

This project analyzes sales data stored in a JSON file (`sales.json`). It filters, groups, and calculates statistics on sales data to provide insights into sales performance by location.

## Features

1. **Filter Sales**:
   - Filters sales made in the last quarter of the year (October, November, December).
   - Selects only sales with an amount greater than $500.

2. **Group by Location**:
   - Groups the filtered sales by the buyer's location.

3. **Calculate Averages**:
   - Calculates the average sales amount for each location.

4. **Sort Locations**:
   - Sorts locations by their average sales amount in descending order.

5. **Display Results**:
   - Prints the sorted locations along with their average sales amounts.

## How It Works

The script reads sales data from a JSON file (`sales.json`) and processes it using Python's list comprehensions, dictionaries, and lambda functions. The results are displayed in the terminal.

### Example JSON Format
The `sales.json` file should be structured as follows:
```
[
    {
        "product": "Smartphone",
        "date": "2025-04-01",
        "amount": 599.99,
        "location": "Madrid"
    },
    {
        "product": "Laptop",
        "date": "2025-11-28",
        "amount": 1200.50,
        "location": "Barcelona"
    },
    ...
]

```

## Example output
```
Location: Madrid, Average Sales Amount: $699.99
Location: Barcelona, Average Sales Amount: $650.00
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
