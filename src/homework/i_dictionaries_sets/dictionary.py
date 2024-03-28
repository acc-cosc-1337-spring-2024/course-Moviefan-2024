# Function to add inventory items
def add_inventory(inventory, item, quantity):
    """
    Adds a specified quantity of an item to the inventory dictionary.

    Parameters:
    - inventory (dict): The inventory dictionary to which the item will be added.
    - item (str): The item to be added to the inventory.
    - quantity (int): The quantity of the item to be added.

    Returns:
    None
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
# Function to remove inventory items and return the remaining quantity
def remove_inventory_widget(inventory, item, quantity):
    """
    Removes a specified quantity of an item from the inventory dictionary
    and returns the remaining quantity of that item.

    Parameters:
    - inventory (dict): The inventory dictionary from which the item will be removed.
    - item (str): The item to be removed from the inventory.
    - quantity (int): The quantity of the item to be removed.

    Returns:
    int: The remaining quantity of the specified item after removal.
    """
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            return inventory[item]
        else:
            print(f"Not enough {item} in inventory!")
            return 0
    else:
        print(f"{item} not found in inventory!")
        return 0