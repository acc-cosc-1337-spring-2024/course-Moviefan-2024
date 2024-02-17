# Import the necessary functions from the decisions.py file
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    # Define the menu options
    menu = """
    Homework 3 Menu
    1-Factorial
    2-Sum odd numbers
    3-Exit
    """

    # Main loop for the menu
    while True:
        print(menu)
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            num = int(input("Enter a number: "))
            # Validate the number
            while num <= 0 or num >= 10:
                print("Please enter a number greater than 0 and less than 10.")
                num = int(input("Enter a number: "))
            # Call the factorial function and print the result
            print("Factorial:", get_factorial(num))

        elif choice == '2':
            num = int(input("Enter a number: "))
            # Validate the number
            while num <= 0 or num >= 100:
                print("Please enter a number greater than 0 and less than 100.")
                num = int(input("Enter a number: "))
            # Call the sum_odd_numbers function and print the result
            print("Sum of odd numbers:", sum_odd_numbers(num))

        elif choice == '3':
            # Ask the user if they want to continue or exit
            exit_choice = input("Do you want to exit? (yes/no): ").lower()
            if exit_choice == 'yes':
                print("Exiting...")
                break
            else:
                continue

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
