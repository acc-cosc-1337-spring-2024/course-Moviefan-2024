# File: src/homework/c_decisions/decisions.py

def get_options_ratio(option, total):
    """
    Calculates the ratio of options to total.
    """
    return option / total

def get_faculty_rating(ratio):
    """
    Returns the faculty rating based on the given ratio.
    """
    if ratio >= 0.9:
        return 'Excellent'
    elif ratio > 0.8:
        return 'Very Good'
    elif ratio > 0.7:
        return 'Good'
    elif ratio > 0.6:
        return 'Needs Improvement'
    else:
        return 'Unacceptable'
