def get_hamming_distance(dna1, dna2):
    """
    Calculate the Hamming distance between two DNA sequences.

    Parameters:
    - dna1 (str): First DNA sequence.
    - dna2 (str): Second DNA sequence.

    Returns:
    - distance (int): Hamming distance between the two DNA sequences.
    """
    if len(dna1) != len(dna2):
        raise ValueError("DNA sequences must be of equal length")
    
    distance = 0
    for char1, char2 in zip(dna1, dna2):
        if char1 != char2:
            distance += 1

    return distance


def get_dna_complement(dna):
    """
    Return the complement of a DNA sequence.

    Parameters:
    - dna (str): DNA sequence.

    Returns:
    - complement (str): Complement of the DNA sequence.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_dna = ''.join(complement[base] for base in dna)
    return complemented_dna
