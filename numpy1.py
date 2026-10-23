import numpy as np

def sep_even_odd(numbers):
    numbers = np.array(numbers)
    evens = numbers[numbers%2 == 0]
    odds = numbers[numbers%2 != 0]
    return evens,odds


numbers = input("Enter numbers separated by spaces: ")    
print(numbers)