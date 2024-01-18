'''
Write a program to find the sum of all elements in a list.
'''

# classic and direct approach traversing the list with a loop and sum variable
def sum_list_iterative(input_list):
    sum = 0
    for num in input_list:
        sum += num
    return sum

# using recursive approach, 
# but this approach is bad since we are creating a new list for each recursive call
# and we are not using the stack efficiently
def sum_list_recursive(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        return input_list[0] + sum_list_recursive(input_list[1:])

# using python built-in sum() function
def sum_list_builtin(input_list):
    return sum(input_list)

# using functional approach with built-in reduce() function
def sum_list_reduce(input_list):
    from functools import reduce
    return reduce(lambda x, y: x + y, input_list)

# using map function
def sum_list_map(input_list):
    return sum(map(int, input_list))

input1 = [1,2,3,4,5]
input2 = [1,2,3,4,5,6,7,8,9,10]

print(f"\nthe sume of {input1} is: ")
print("iterative: ", sum_list_iterative(input1))
print("recursive: ", sum_list_recursive(input1))
print("built-in sum: ", sum_list_builtin(input1))
print("functional reduce: ", sum_list_reduce(input1))
print("functional sum: ", sum_list_map(input1))

print(f"\nthe sume of {input2} is: ")
print("iterative: ", sum_list_iterative(input2))
print("recursive: ", sum_list_recursive(input2))
print("built-in sum: ", sum_list_builtin(input2))
print("functional reduce: ", sum_list_reduce(input2))
print("functional sum: ", sum_list_map(input2))


