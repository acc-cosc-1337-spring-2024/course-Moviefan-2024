# In main.py

def add_or_update_item(inventory):
    widget_name = input("Enter widget name: ")
    quantity = int(input("Enter quantity: "))
    if widget_name in inventory:
        inventory[widget_name] += quantity
        print("Item updated successfully.")
    else:
        inventory[widget_name] = quantity
        print("Item added successfully.")

def delete_item(inventory):
    widget_name = input("Enter widget name to delete: ")
    if widget_name in inventory:
        del inventory[widget_name]
        print("Item deleted successfully.")
    else:
        print("Item not found.")

def display_menu():
    print("\nInventory Menu\n")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_or_update_item(inventory)
        elif choice == "2":
            delete_item(inventory)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")