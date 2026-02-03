"""
Pre-module warm-up exercise 6

Scenario:
You are building an inventory system for a small shop.

Task:
Create a list called inventory.
Define at least one product as a dictionary with the keys:
    "name"   "price"   "stock_level"
Store the product dictionary inside the inventory list.
Use a for loop to display product details.

Requirements:
# All data is stored using dictionaries.
# Inventory is iterable.
# Output is clearly formatted and readable.
#Output Format:
#   Product: Milk | Price: £1.20 | Status: In Stock
"""
#Completed exercise 6 - with major additions.
#Transformed challenge into fully functional object based code
#Calls functions within functions for validation and to prevent WET code
#Utilizes json to store and load inventory data
#Added type hints

"""Imports"""
import json



def load_test_inventory() -> None:
    """
    This function loads the preset test inventory

    Arguments:
        None

    Returns:
        None - calls load inventory function, which returns the loaded inventory

    Raise:
        FileNotFoundError: If file cannot be found
        json.JSONDecodeError: If file is corrupted
    """

    test_inventory: list[dict[str, str | float | int]] = [
    {"name": "Milk","price": 1.20,"stock_level": 10},
    {"name": "Monster Energy","price": 2.25,"stock_level": 0},
    {"name": "Beef Mince","price": 5,"stock_level": 14},
    {"name": "Chocolate Bar","price": 2.99,"stock_level":5}]

    try:
        with open("inventory_exercise_6.json", "w") as f:
            json.dump(test_inventory, f, indent= 4)
        return load_inventory()

    except FileNotFoundError:
        raise FileNotFoundError("File could not be Found")

    except json.JSONDecodeError:
        raise ValueError("File failed to decode")



def save_inventory(new_inventory: list[dict]) -> None:
    """
    Saves inventory to json file

    Arguments:
        new_inventory - new inventory to save from

    Returns:
        None

    Raises:
        FileNotFoundError: If file cannot be found
        json.JSONDecodeError: If file is corrupted
    """
    try:
        with open("inventory_exercise_6.json", "w") as f:
            json.dump(new_inventory, f, indent= 4)
    
    except FileNotFoundError:
        raise FileNotFoundError("File could not be Found")

    except json.JSONDecodeError:
        raise ValueError("File failed to decode")



def load_inventory() -> list[dict]:
    """
    Loads inventory from json file and returns it

    Arguments:
        None - no argument needed as the data is taken from json

    Returns:
        loaded inventory as a list of dictionaries or error message

    Raises:
        FileNotFoundError: If file cannot be found
        json.JSONDecodeError: If file is corrupted
    """
    try:
        with open("inventory_exercise_6.json", "r") as f:
            inventory = json.load(f)
            return inventory

    except FileNotFoundError:
        raise ValueError("File could not be Found")

    except json.JSONDecodeError:
        raise ValueError("File failed to decode")


def validate_option_choice(choice: str) -> int:
    """
    Validates the menu option choice by changing the string to int

    Arguments:
        The users input choice

    Returns:
        The users choice as a integer

    Raises:
        ValueError: If choice is not in option range 1-5
    """
    if choice not in {"1","2","3","4","5"}:
        raise ValueError("Invalid option")
    return int(choice)


def menu_management(inventory: list[dict]) -> None:
    """
    Menu management for selecting options and saving new data

    Arguments:
        current inventory as a list of dictionaries

    Returns:
        None, if the user wants to exit the menu

    Raises:
        ValueError: If input option is invalid
    """
    while True:
        print("\nPlease select from the following options:\n1. Change stock" \
        "\n2. Change product price\n3. Add product\n4. Close menu\n5. Load test data")
        try:
            option: int = validate_option_choice((input().strip()))
            print()
            if option == 1:
                save_inventory(change_stock(inventory))
                load_inventory()
                break
            elif option == 2:
                save_inventory(change_product_price(inventory))
                load_inventory()
                break
            elif option == 3:
                save_inventory(add_product(inventory))
                load_inventory()
            elif option == 4:
                return None
            elif option == 5:
                load_test_inventory()
                CLI_menu(menu_state = 2)
            
        except ValueError as e:
            print(f"Error: {e}")


def change_stock(inventory: list[dict]) -> list[dict]:
    """
    Changes stock and returns updated inventory

    Arguments:
        Current inventory as a list of dictionaries

    Returns:
        Updated inventory as a list of dictionaries

    Raises:
        ValueError: If input is invalid
    """
    while True:
        i = 1
        for x in inventory:
            print(f"{i}. Product: {x["name"]:<15}| Stock: {x["stock_level"]}")
            i += 1
        try:
            product_choice: str = int(input(
                f"Please select product number 1-{len(inventory)}").strip())
            
            if product_choice < 1 or product_choice > len(inventory):
                raise ValueError
            print(f"Current stock: {inventory[(product_choice - 1)]["stock_level"]}")

            new_stock = int(input("Enter new stock level:"))
            if new_stock < 0:
                raise ValueError
            inventory[(product_choice - 1)]["stock_level"] = new_stock
            break
            
        except ValueError as e:
            print(f"Invalid input, Try again\n")

    return inventory



def change_product_price(inventory: list[dict]) -> list[dict]:
    """
    Changes product price and returns new inventory

    Arguments:
        Current inventory as a list of dictionaries

    Returns:
        Updated inventory as a list of dictionaries

    Raises:
        ValueError: If input is invalid
    """
    while True:
        i = 1
        for x in inventory:
            print(f"{i}. Product: {x["name"]:<15}| Price: {x["price"]}")
            i += 1
        try:
            product_choice: str = int(input(
                f"Please select product number 1-{len(inventory)}").strip())
            
            if product_choice < 1 or product_choice > len(inventory):
                raise ValueError
            print(f"Current price: {inventory[(product_choice - 1)]["price"]:.2f}")

            new_price = float(input("Enter new price £:"))
            if new_price < 0:
                raise ValueError
            inventory[(product_choice - 1)]["price"] = new_price
            break
            
        except ValueError as e:
            print(f"Invalid input, Try again\n")

    return inventory


def add_product(inventory: list[dict]) -> list[dict]:
    """
    Adds new product to inventory with inputted: name, price, stock

    Arguments:
        Current inventory as a list of dictionaries

    Returns:
        Updated inventory as a list of dictionaries

    Raises:
        ValueError: If input is invalid
    """
    while True:
        product_name = input("New product name: ").strip()
        if product_name:
            break

    while True:
        try:
            product_price: float = float(input("Product price: ").strip())
            if product_price < 0:
                raise ValueError
            break
        
        except ValueError:
            print("Invalid price, Try again")

    while True:
        try:
            product_stock: int = int(input("Please enter stock amount: ").strip())
            break
        
        except ValueError:
            print("Invalid price, try again")

    new_product: list[dict] = {"name": product_name, "price": product_price,
                    "stock_level": product_stock}
    
    inventory.append(new_product)
    return inventory


def CLI_menu(menu_state: int) -> None:
    """
    Script for displaying inventory in CLI

    Arguments:
        Menu state to detect when test inventory is wanted,
        overrides current inventory!

    Returns:
        None, because it displays the menu inside the function

    Raises:
        ValueError: If inventory fails to load
    """
    while True:
        if menu_state == 1:
            try:
                loaded_inventory = load_inventory()
                print("Inventory loaded successfully\n")
            except ValueError as e:
                print(f"Error: {e}\n")
                try:
                    loaded_inventory = load_test_inventory()
                    print("Test Inventory Loaded\n")
                except ValueError as e:
                    print(f"Error: {e}\n")
        elif menu_state == 2:
            try:
                loaded_inventory = load_test_inventory()
                print("Test Inventory Loaded\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        
        for x in loaded_inventory:
            if x["stock_level"] > 1:
                status = "In Stock"
            else:
                status = "Out of Stock"
            print(f"Product: {x["name"]:<15}| Price: {x["price"]:<5.2f}| Status: {status}")
        input("Press enter for menu")
        menu_management(loaded_inventory)

        continue_menu = input(("Press enter to return to inventory,"
        " or any other key to exit").strip())
        if continue_menu:
            break
        
if __name__ == "__main__":
    CLI_menu(menu_state = 1)
