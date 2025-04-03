# Name Transformation and Filtering

This project processes a list of names stored in a JSON file (`names.json`). It transforms the names into a new format and filters them based on specific criteria.

## Features

1. **Transform Names**:
   - Converts names from the format `LastName, FirstName` to `FirstName LastName`.

2. **Filter Names**:
   - Filters the transformed names to include only those that:
     - Contain at least two vowels.
     - Are longer than 10 characters.

3. **Display Results**:
   - Prints the filtered names to the terminal.

## How It Works

The script reads a list of names from a JSON file (`names.json`) and processes them using Python's `map` and `filter` functions with lambda expressions. The results are displayed in the terminal.

### Example JSON Format
The `names.json` file should be structured as follows:
```
[
    "García, Alejandro", 
    "Fernández, Beatriz", 
    "Rodríguez, Carlos", 
    "López, Diana"
]
...
```

## Example output
```
['Alejandro García', 'Beatriz Fernández']
```

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
