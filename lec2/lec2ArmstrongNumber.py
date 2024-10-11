# What is an Armstrong number? Write a Python function to check if a given number is an Armstrong number.

# An Armstrong number (also known as a Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example:

# 153 is an Armstrong number, because:

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153



def is_armstrong(number: int) -> bool:
 
    num_digits = len(str(number))
    
    original_number = number
    armstrong_sum = 0
   
    while original_number > 0:
        digit = original_number % 10 
        armstrong_sum += digit ** num_digits 
        original_number //= 10  
    
    return armstrong_sum == number
