# Week 2
# exercise 5
# Function to determine divisibility by 11, 
# takes the alternating sum of the digits in the number, 
# reads from left to right
#
# Xandy Duhe 

def divisible_by_11(number):

    # make num positive
    number = abs(number)
    
    # convert num to str to iterate through digits
    digits = str(number)
    
    # cal alternating sum of digits
    alternating_sum = 0
    for i, digit_char in enumerate(digits):
        digit = int(digit_char)
        if i % 2 == 0:

            # add digit for even index
            alternating_sum += digit  
        else:

            # subtract digit for odd index
            alternating_sum -= digit  
    
    # check if alternating sum is divisible by 11
    return alternating_sum % 11 == 0



try:
    # user enter a number
    number = int(input("Enter a number: "))
    
    # check if number is divisible by 11 
    if divisible_by_11(number):
        print("This number is divisible by 11.")
    else:
        print("This number is not divisible by 11.")
        
except ValueError:
    # case where user enters non-integer input
    print("Invalid input. Please enter a valid integer.")
