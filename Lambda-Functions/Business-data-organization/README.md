# Employee Management System

This project provides functionality to manage a list of employees stored in a JSON file. The main features include sorting employees by performance and age, grouping them by country, and displaying the results in a structured format.

## Features

- **Sort Employees**: Employees are sorted based on their performance (from highest to lowest) and age (from lowest to highest).
- **Group by Country**: Employees are grouped by their respective countries for easier viewing and analysis.
- **Display Employees**: The sorted and grouped list of employees is displayed in the terminal.

### Example JSON Format
The `inventory.json` file should be structured as follows:
```json
[ 
    {
        "name": "Juan Perez",
        "age": 33,
        "country": "Spain",
        "performance": 90
    },
    {
        "name": "Ana Gomez",
        "age": 28,
        "country": "Mexico",
        "performance": 85
    },
    {
        "name": "Carlos Lopez",
        "age": 45,
        "country": "Argentina",
        "performance": 92
    },
    {
        "name": "Maria Rodriguez",
        "age": 37,
        "country": "Mexico",
        "performance": 88
    }
]
```

## Running the Program

To run the script, ensure you have Python installed, and that your working directory contains the `inventory.json` file.

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
