# Inventory Management System

This Python script is a basic **Inventory Management System** that interacts with a JSON file to manage products and their quantities. It allows the user to search for products, add or remove items, delete products, and display the current inventory. The system uses a JSON file (`inventory.json`) to store and update inventory data.

## Features

- **Search for a product**: Search for a product by its code in the inventory.
- **Add items**: Increase the quantity of an existing product or add a new product if it doesn't exist.
- **Remove items**: Decrease the quantity of an existing product.
- **Delete a product**: Remove a product from the inventory.
- **Show the inventory**: Display the current state of the inventory (product codes and quantities).

## How It Works

The inventory is stored in a JSON file named `inventory.json`. When the program starts, it reads the data from this file and stores it in memory. After every task (such as adding or removing items), the inventory is updated and saved back to the JSON file.

## Running the Program

To run the script, ensure you have Python installed, and that your working directory contains the `inventory.json` file.

### Example

Here’s an example of how to use the script:

What task do you want to do? 
1. Search product 
2. Add items 
3. Remove items 
4. Delete product 
5. Show the inventory 
2
What is the code of the product you want to add items?
101
What amount of items do you want to add? 
50

Product quantity with code 101 updated to 50 items.

### Note
This is a slightly more extensive implementation than what is requested in the PDF instructions. Although it is more extensive, it is still a basic implementation of an inventory management system, and many functionalities could be added. Any requests for additional features are welcome and appreciated

## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
