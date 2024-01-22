'''
Write a program to check if a number is even or odd.
'''
# assumptions:
# - number is a integer (whole number, not decimal)
# - number is a 32-bit number
# - 0 by mathmetical definition is even

# if we are getting input from user, it is a string
# we can just check the last digit of the string
# even numbers end in 0, 2, 4, 6, 8
def odd_or_even_last_digit(num):
    if num[-1] in ['0', '2', '4', '6', '8']:
        return "even"
    else:
        return "odd"

from random import randint
# the widely accepted approach is to use the modulo/modulus operator
# even numbers are divisible by 2, with remainder 0
# odd numbers are not divisible by 2, they have a remainder 1
def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# if the last bit of the binary representation of the number is 0, it is even
# if the last bit of the binary representation of the number is 1, it is odd
def odd_or_even_bitwise(num):
    
    # we use bitwise AND operator to check the last bit
    if (num & 0x1) == 1:
        return "odd"
    else:
        return "even"

for i in range(5):
    randnum = randint(-1*(pow(2,31)-1), pow(2,31)-1)
    print(f"{randnum} is: {odd_or_even(randnum)}")
    print(f"{randnum} is: {odd_or_even_bitwise(randnum)}")

input_num = input("Enter a number to check if it is odd or even: ")
print(f"{input_num} is: {odd_or_even_last_digit((input_num))}")