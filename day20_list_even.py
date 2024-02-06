'''
Write a function that takes a list of numbers and returns a list with only the even numbers.
'''

'''
I am assuming "valid" input, i.e. the input list is a list of integers.
I don't do error checking. I am more focused on the algorithm and the different ways to implement it.

Remember from day09 exercise, oddness and evenness are properties of integers, not decimals.

Ideas/Approach/Algorithm:
1. use loop to iterate through the list - this is the most straight forward way approach
2. use list comprehension - this is the most pythonic way, underneath the hood, it is still a loop/iteration
3. use the built-in filter() function - this is the most functional programming way
4. use recursion - this is the most inefficient way, but it is a good exercise to practice recursion
'''

# define a function to check for even-ness which will be used in multiple places later
def is_even(n):
    return n % 2 == 0

def get_evens_iterative(input_list):
    # we have to a new array/list which uses O(n) extra space
    evens = []

    # we have to iterate through the entire list, which uses O(n) time
    for num in input_list:
        if is_even(num):
            evens.append(num)

    return evens

def get_evens_list_comprehension(input_list):
    # we have to iterate through the entire list, which uses O(n) time
    # I think underneath the hood, it iterates with a loop as well
    # the difference is the is more "pythonic" and "concise" b/c we write less code
    return [num for num in input_list if is_even(num)]

def get_evens_recursive(input_list):
    # base case
    if len(input_list) == 0:
        return []
    
    # recursive case, this is inefficient b/c it creates a new list when we slice [1:]
    # and each recursive call uses stack memory
    if is_even(input_list[0]):
        return [input_list[0]] + get_evens_recursive(input_list[1:])
    else:
        return get_evens_recursive(input_list[1:])

def get_evens_filter(input_list):
    # "functional programming" by using lambda function and filter function
    # a "lambda" function is an anonymous function that is defined on the fly
    return list(filter(lambda x: x % 2 == 0, input_list))

# these 2 functions do the same job as the above function
# if we need to use is_even() in multiple places, it is better to define it as a function than as an anonymous lambda function
#def is_even(n):
#    return n % 2 == 0
def get_evens_filter_without_lambda(input_list):
    return list(filter(is_even, input_list))


# test cases
input_nums = [n for n in range(-15, 15)]
print(f"input_nums: {input_nums}")
print(f"get_evens_iterative:                {get_evens_iterative(input_nums)}")
print(f"get_evens_list_comprehension:       {get_evens_list_comprehension(input_nums)}")
print(f"get_evens_recursive:                {get_evens_recursive(input_nums)}")
print(f"get_evens_filter:                   {get_evens_filter(input_nums)}")
print(f"get_evens_filter_without_lambda:    {get_evens_filter_without_lambda(input_nums)}")

assert get_evens_iterative(input_nums) == get_evens_list_comprehension(input_nums) == get_evens_recursive(input_nums) == get_evens_filter(input_nums) == get_evens_filter_without_lambda(input_nums) == [-14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14]