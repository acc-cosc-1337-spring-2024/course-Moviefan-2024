def get_hamming_distance(s1, s2):
    # Calculate the Hamming distance between two strings
    distance = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            distance += 1
    return distance

def get_dna_complement(dna):
    # Return the complement of a DNA sequence
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_dna = ''.join(complement[base] for base in dna)
    return complemented_dna

while True:
    print("1-Hamming Distance")
    print("2-DNA Complement")
    print("3-Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")
        hamming_distance = get_hamming_distance(string1, string2)
        print("Hamming distance:", hamming_distance)
    elif choice == '2':
        dna_string = input("Enter the DNA string: ")
        dna_complement = get_dna_complement(dna_string)
        print("DNA complement:", dna_complement)
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

