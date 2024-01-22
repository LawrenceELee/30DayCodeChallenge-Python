'''
Write a program to print the multiplication table of a given number.

Ideas:
1. Iterative: use a loop to generate the multiplication table
    a. this is the most straightforward approach to think of.
2. Functional: use functional style and built-in map() to generate a list of numbers
    a. this code is shorter, but requires knowledge of map() and lambda functions
3. Recursive: use recursion to generate the multiplication table
    a. least efficient b/c of recursive call stacks
4. using Python generators/iterators
'''

# straightforward approach: use a loop to calculate and print the multiplication table
def print_mul_table(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num*i}")

def print_mul_table_map(num):
    # use functional style and built-in map() to generate a list of numbers
    mul_table = list(map(lambda x: x*num, range(1, 13)))
    print(mul_table)

def print_mul_table_recursive(num, i=1):
    # base case
    if i > 12:
        return

    # recursive case
    print(f"{num} x {i} = {num*i}")
    print_mul_table_recursive(num, i+1)

def print_mul_table_generator(num):
    # use Python generators/iterators?
    mul_table = [x*num for x in range(1, 13)]
    print(mul_table)

input1 = 5
print_mul_table(input1)
print_mul_table_map(input1)
print_mul_table_recursive(input1)
print_mul_table_generator(input1)

input_num = int(input("Enter a number to print its multiplication table: "))
print_mul_table(input_num)
print_mul_table_map(input_num)
print_mul_table_recursive(input_num)
print_mul_table_generator(input_num)