'''
Create a program that uses a lambda function to square each element in a list.
'''
# we can define a function with out the "def" keyword
# then we can use the "lambda" keyword to define an anonymous function
# and use the "equals" sign to bind the anonymous function to a variable/name
square_function = lambda x: x**2
def square_lambda_named_with_map(input_list):
    return list( map(square_function, input_list) )

# if there are no plans to reuse the lambda function, we can define it on the fly
# it doesn't need to be bound to a variable/name
def square_lambda_unamed_with_map(input_list):
    return list( map(lambda x: x**2, input_list) )

# incorrect usage of lambda and list comprehension
# [lambda x: x*x for x in range(10)]
# you’re creating a ***list of lambda functions***, not a list of numbers.
# Each lambda function computes the square of its input.
# the correct way to use lambda and list comprehension is to use the map function, like above
# or use parentheses to call the lambda function 
def square_lambda_with_list_comprehension(input_list):
    return [ (lambda x: x**2)(x) for x in input_list]

# or simply put the body of the function in the list comprehension
def square_with_list_comprehension(input_list):
    return [x**2 for x in input_list]

# test cases
input_nums = [n for n in range(-10, 11)]
print(f"input_nums:                            {input_nums}")
print(f"square_lambda_named_with_map:          {square_lambda_named_with_map(input_nums)}")
print(f"square_list:                           {square_lambda_unamed_with_map(input_nums)}")
print(f"square_lambda_with_list_comprehension: {square_lambda_with_list_comprehension(input_nums)}")
print(f"square_with_list_comprehension:        {square_with_list_comprehension(input_nums)}")