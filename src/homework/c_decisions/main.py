# File: src/homework/c_decisions/main.py

from decisions import get_options_ratio, get_faculty_rating

def main():
    # Prompt the user for options and total
    options = float(input("Enter the number of options: "))
    total = float(input("Enter the total number: "))

    # Calculate the ratio of options to total
    ratio = get_options_ratio(options, total)

    # Get the faculty rating based on the ratio
    faculty_rating = get_faculty_rating(ratio)

    # Display the faculty rating
    print("Faculty Rating:", faculty_rating)

if __name__ == "__main__":
    main()
