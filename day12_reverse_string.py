'''
Write a program to reverse a given string.
'''

'''
Like all programming problems, there are multiple ways/approaches/algorithsm to solve this problem.

Ideas:
1. use the Python built-in reverse() function
    a. this is the shortest code and requires the least amount of effort, but is not accepted in technical interviews
    b. we also don't know the time and space complexities of this built-in function, unless we look at the source code
2. iterative approach: use a loop to traverse the string from the end to the beginning
    a. we can either swap in-place or use a extra temporary array
3. recursive approach: we recursively call reverse function until end of string then we concatenate the previous char to end
    a. this is least efficient because we are creating a new string for each recursive call
    b. this is to demonstrate that it can be done recursively, but it is not the best approach
'''

# built-in reverse() function
def reverse_builtin(input_str):
    # convert string to array/list, reverse the list, then convert back to string
    return ''.join(reversed(list(input_str)))

#iterative approach with in-place swap
def reverse_iterative(input_str):
    # convert string to array/list
    input_list = list(input_str)

    # use 2 index pointers, one at the beginning and one at the end
    start = 0
    end = len(input_list) - 1

    # swap elements in-place at start and end pointers, we don't use extra temp array/list
    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]

        # move pointers to the next indices
        start += 1
        end -= 1

    # convert list back to string
    return ''.join(input_list)

# recursive approach
def reverse_recursive(input_str):
    # base case
    if len(input_str) == 0:
        return ''

    # recursive case
    return reverse_recursive(input_str[1:]) + input_str[0]


input1 = "!abcefghijklmnopqrstuvwxyz."

assert reverse_builtin(input1) == reverse_iterative(input1) == reverse_recursive(input1)
print(reverse_builtin(input1))
print(reverse_iterative(input1))
print(reverse_recursive(input1))