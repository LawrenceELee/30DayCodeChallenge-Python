from random import randint
import sys
'''
Write a program to check if a number is positive, negative, or zero.
'''

# direct and straightforward approach/algorithm
def check_pos_neg_num(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# this approach uses bitwise operations and is not as straightforward, especially for python
# making the assumption that the number is a integer (whole number, not decimal)
# also assuming the number is a 32-bit number
def check_pos_neg_num_bitwise(num):
    # 0x######## is a hex number meaning it is base 16
    # it looks like binary 10000000000000000000000000000000
    # when a negative number is represented in binary, it is represented as the 2's complement
    if num & 0x80000000:
        return "negative"
    # if the starting number starts with 0, it is either positive or zero
    return "positive" if num != 0 else "zero"

# this approach is 'cheating' since I convert the number into a string and check for a minus sign at the beginning
# this is basically the "string" equivalent of 2's complement
def check_pos_neg_num_minus_sign(num):
    num_str = str(num)
    if num_str[0] == "-":
        return "negative"
    elif num_str[0] == "0":
        return "zero"
    else:
        return "positive"

for i in range(5):
    # generate a random number between negative 2 billion and positive 2 billion
    randnum = randint(-1*(pow(2,31)-1), pow(2,31)-1)
    
    # assert to test both my functions return the same result
    assert check_pos_neg_num(randnum) == check_pos_neg_num_bitwise(randnum)
    assert check_pos_neg_num(randnum) == check_pos_neg_num_minus_sign(randnum)  
    print(f"randnum: {randnum} is: {check_pos_neg_num(randnum)} {check_pos_neg_num_bitwise(randnum)} {check_pos_neg_num_minus_sign(randnum)}")

# test zero
randnum = 0
print(f"randnum: {randnum} is: {check_pos_neg_num(randnum)} {check_pos_neg_num_bitwise(randnum)} {check_pos_neg_num_minus_sign(randnum)}")

