import json

# Open the json file in read mode
with open("inventory.json", "r") as inventory_json:
    # Load the inventory list to store it in a variable
    inventory = json.load(inventory_json)


# Function that will search for the product in the inventory
def search_product(inventory, code):

    lenght = len(inventory)
    medium = lenght // 2

    # Base case 1 -- The inventory has only 1 product and the codes do not match
    if lenght == 1 and code != inventory[0]['code']:
        return -1
    
    # Base case 2 -- The product that we are looking for is in the middle if the list
    if code == inventory[medium]['code']:
        return inventory[medium]['quantity']
    
    # Recursive case
    else:

        if code > inventory[medium]['code']:
            # Search in the left half of the list
            return search_product(inventory[:medium], code)

        elif code < inventory[medium]['code']:
            # Search in the right hald of the list
            return search_product(inventory[medium:], code)

# Function that will add items to the existing product or will create a new product if it does not exist
def add_items(inventory, code, amount):
    # To check if the product is in the list we will use the search_product function
    quantity = search_product(inventory, code)
    # Index where the product is stored
    index = None

    # If the product does not exist it will be added to the list
    if quantity == -1:
        new_code = inventory[0]['code']+1
        inventory.insert(0, {'code':new_code, 'quantity':amount})
        print(f"There is no product with the given code so the product will be added to the inventory with the code {new_code}")

        
    # If the product exists it's amount will be updated
    else:
        index = inventory.index({'code': code, 'quantity': quantity})
        inventory[index]['quantity'] += amount # Updateing the new quantity
        print(f"Product quantity with code {code} updated to {quantity+amount} items")
    

# Function that will decrease the quantity of a product
def remove_items(inventory, code, amount):
    # To check if the product is in the list we will use the search_product function
    quantity = search_product(inventory, code)
    # Index where the product is stored
    index = None

    # If the product does not exist
    if quantity == -1:
        print("There is no product with the given code")

    else:
        index = inventory.index({'code': code, 'quantity': quantity})
        inventory[index]['quantity'] -= amount # Updateing the new quantity
        print(f"Product quantity with code {code} updated to {quantity-amount} items")
    

# Function that will delete items
def delete_product(inventory, code):
    # To check if the product is in the list we will use thw search_product function
    quantity = search_product(inventory, code)
    # Index where the product is stored
    index = None

    # If the product does not exist
    if quantity == -1:
        print("There is no product with the given code")

    else:
        index = inventory.index({'code': code, 'quantity': quantity})
        inventory.remove(inventory[index])

# Function that will show you the inventory
def show_inventory():
    print("INVENTORY:")
    for i in range(len(inventory)):
        print(f"Code: {inventory[i]['code']}, Quantity: {inventory[i]['quantity']}")

keep = True

while keep:

    function = int(input("What task do you want to do? \n1. Search product \n2. Add items \n3. Remove items \n4. Delete product5 \n5. Show the inventory \n"))

    while function not in range(1,6):
        print("ERROR: no task available")
        function = int(input("What task do you want to do? \n1. Search product \n2. Add items \n3. Remove items \n4. Delete product \n5. Show the inventory \n"))

    # Search product
    if function == 1:
        code = int(input("What code do you want to look for? \n"))
        quantity = search_product(inventory, code)

        if quantity == -1:
            print("There is no product with the given code")
        else:
            print(f"The product with code {code} has a quantity of {quantity} units")

    # Add items
    elif function == 2:
        code = int(input("What is the code of the product you want to add items? \n"))
        amount = int(input("What amount of items do you want to add? \n"))

        add_items(inventory, code, amount)

    # Remove items
    elif function == 3:
        code = int(input("What is the code of the product you want to remove items? \n"))
        amount = int(input("What amount of items do you want to remove? \n"))

        remove_items(inventory, code, amount)

    # Delete items
    elif function == 4:
        code = int(input("What is the code of the product you want to remove? \n"))
        quantity = search_product(inventory, code)

        if quantity == -1:
            print("There is no product with the given code")
        
        else:
            delete_product(inventory, code)
            print(f"The product with the code {code} has been deleted from the inventory")

    # Show inventory
    elif function == 5:
        show_inventory()

    while keep:
        keep_asking = input("Do you want to do another task? Y/N \n")
        keep_asking = keep_asking.upper()

        if keep_asking == "Y":
            break
        elif keep_asking == "N":
            keep = False
        else:
            print("ERROR: no valid answer")

# Updating the changes in the JSON file
with open("inventory.json", 'w') as new_inventory:
    json.dump(inventory, new_inventory, indent=4)
