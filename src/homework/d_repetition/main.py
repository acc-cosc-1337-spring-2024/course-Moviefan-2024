# src/homework/d_repetition/main.py

from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            num = int(input("Enter a number: "))
            while not (0 < num < 10):
                print("Please enter a number greater than 0 and less than 10.")
                num = int(input("Enter a number: "))
            print("Factorial:", get_factorial(num))

        elif choice == '2':
            num = int(input("Enter a number: "))
            while not (0 < num < 100):
                print("Please enter a number greater than 0 and less than 100.")
                num = int(input("Enter a number: "))
            print("Sum of odd numbers:", sum_odd_numbers(num))

        elif choice == '3':
            exit_choice = input("Do you want to continue? (yes/no): ").lower()
            if exit_choice == 'no':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()
