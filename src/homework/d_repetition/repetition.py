# src/homework/d_repetition/repetition.py

def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

