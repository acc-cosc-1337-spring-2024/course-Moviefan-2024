# Define the dictionaries
prog1 = {
    "Alice": True,
    "Bob": True,
    "Charlie": False,
    "David": True,
    "Eve": False
}

prog2 = {
    "Alice": True,
    "Bob": False,
    "Charlie": True,
    "David": False,
    "Frank": True
}

# Function to find students who took prog1 and prog2
def students_took_both(prog1, prog2):
    return [student for student in prog1 if prog1[student] and prog2.get(student, False)]

# Function to find students who took prog2 only
def students_took_prog2_only(prog1, prog2):
    return [student for student in prog2 if prog2[student] and not prog1.get(student, False)]

# Function to find students who took prog1 but not prog2
def students_took_prog1_not_prog2(prog1, prog2):
    return [student for student in prog1 if prog1[student] and not prog2.get(student, False)]

# Function to find students who took prog2 but not prog1
def students_took_prog2_not_prog1(prog1, prog2):
    return [student for student in prog2 if prog2[student] and not prog1.get(student, False)]

# Main function to display menu and handle user input
def main():
    while True:
        print("\nInventory Menu\n")
        print("1-Students who took prog1 and prog2")
        print("2-Students who took prog2 only")
        print("3-Students who took prog1 not prog2")
        print("4-Students who took prog2 not prog1")
        print("5-Exit\n")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("Students who took both prog1 and prog2:", students_took_both(prog1, prog2))
        elif choice == '2':
            print("Students who took prog2 only:", students_took_prog2_only(prog1, prog2))
        elif choice == '3':
            print("Students who took prog1 but not prog2:", students_took_prog1_not_prog2(prog1, prog2))
        elif choice == '4':
            print("Students who took prog2 but not prog1:", students_took_prog2_not_prog1(prog1, prog2))
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
