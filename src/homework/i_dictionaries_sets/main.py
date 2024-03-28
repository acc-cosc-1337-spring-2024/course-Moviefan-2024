def display_menu():
    print("Inventory Menu\n")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def add_or_update_item(inventory):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{item} updated. Current quantity: {inventory[item]}")

def delete_item(inventory):
    item = input("Enter item name to delete: ")
    if item in inventory:
        del inventory[item]
        print(f"{item} deleted from inventory.")
    else:
        print(f"{item} not found in inventory.")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            add_or_update_item(inventory)
        elif choice == '2':
            delete_item(inventory)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")