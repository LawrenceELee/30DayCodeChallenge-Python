'''
Write a function to calculate the factorial of a number.
'''

'''
questions:
++ what is the largest number python can store?
'''
import timeit
import math
import sys
sys.setrecursionlimit(10**6)

def factorial_iterative(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    
    return n * factorial_recursive(n-1)

def factorial_builtin(n):
    return math.factorial(n)

input_num = 5
print(f"factorial_iterative({input_num}) = {factorial_iterative(input_num)}")
print(f"factorial_recursive({input_num}) = {factorial_recursive(input_num)}")
print(f"factorial_builtin({input_num}) = {factorial_builtin(input_num)}")
assert factorial_iterative(input_num) == factorial_recursive(input_num) == factorial_builtin(input_num)

input_num = 20
print(f"factorial_iterative({input_num}) = {factorial_iterative(input_num)}")
print(f"factorial_recursive({input_num}) = {factorial_recursive(input_num)}")
print(f"factorial_builtin({input_num})   = {factorial_builtin(input_num)}")
assert factorial_iterative(input_num) == factorial_recursive(input_num) == factorial_builtin(input_num)

input_num = 50
print(f"factorial_iterative({input_num}) = {factorial_iterative(input_num)}")
print(f"factorial_recursive({input_num}) = {factorial_recursive(input_num)}")
print(f"factorial_builtin({input_num})   = {factorial_builtin(input_num)}")
assert factorial_iterative(input_num) == factorial_recursive(input_num) == factorial_builtin(input_num)

input_num = 100
#print(f"factorial_iterative({input_num}) = {factorial_iterative(input_num)}")
#print(f"factorial_recursive({input_num}) = {factorial_recursive(input_num)}")
#print(f"factorial_builtin({input_num})   = {factorial_builtin(input_num)}")
assert factorial_iterative(input_num) == factorial_recursive(input_num) == factorial_builtin(input_num)

input_num = 1000
#print(f"factorial_iterative({input_num}) = {factorial_iterative(input_num)}")
#print(f"factorial_recursive({input_num}) = {factorial_recursive(input_num)}")
#print(f"factorial_builtin({input_num})   = {factorial_builtin(input_num)}")
assert factorial_iterative(input_num) == factorial_recursive(input_num) == factorial_builtin(input_num)

def wrapper_factorial_iterative():
    return factorial_iterative(1000)

def wrapper_factorial_recursive():
    return factorial_recursive(1000)

def wrapper_factorial_builtin():
    return factorial_builtin(1000)

def measure_performance():
    ''' Measure the performance '''
    NUMBER_OF_RUNS = 1000
    execution_time_iteration = round(timeit.timeit(wrapper_factorial_iterative, number=NUMBER_OF_RUNS), 10)
    average_time_iteration = execution_time_iteration / NUMBER_OF_RUNS
    execution_time_recursion = round(timeit.timeit(wrapper_factorial_recursive, number=NUMBER_OF_RUNS), 10)
    average_time_recursion = execution_time_recursion / NUMBER_OF_RUNS
    execution_time_builtin = round(timeit.timeit(wrapper_factorial_builtin, number=NUMBER_OF_RUNS), 10)
    average_time_builtin = execution_time_builtin / NUMBER_OF_RUNS

    print(f"\nRunning code {NUMBER_OF_RUNS} times.")
    print(f"Total execution time using iteration: {execution_time_iteration} seconds")
    print(f"Total execution time using recursion: {execution_time_recursion} seconds")
    print(f"Total execution time using builtin:   {execution_time_builtin} seconds")
    print(f"Average time per execution (iteration): {average_time_iteration: .10f} seconds")
    print(f"Average time per execution (recursion): {average_time_recursion: .10f} seconds")
    print(f"Average time per execution (builtin):   {average_time_builtin: .10f} seconds")

measure_performance()