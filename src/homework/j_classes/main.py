from class_a import Die

def main():
    die = Die()
    while True:
        input("Press Enter to roll the die...")
        die.roll()
        print(die)
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
