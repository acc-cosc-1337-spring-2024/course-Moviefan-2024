def sum_odd_numbers(num):
    sum_odd = 0
    current_number = 1
    while current_number <= num:
        if current_number % 2 != 0:
            sum_odd += current_number
        current_number += 1
    return sum_odd
