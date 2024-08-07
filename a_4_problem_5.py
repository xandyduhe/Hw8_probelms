# Week 4
# Problem 5
# compute gcd(a,b) for a and b 
#
# Recursively 
#
# Xandy Duhe 


def greatest_common_divisor(a, b):
    '''compute gcd(a,b) for input integers a and b '''

    # if b =0 then skip obviously..
    while b != 0:
        # b becomes a modulo b 
        a, b = b, a % b
    return a

# input a and b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


gcd = greatest_common_divisor(a, b)
print(f"The greatest common divisor of {a} and {b} is {gcd}.")
