'''
Create a program to find the largest among three numbers.
'''
import random

def max3_builtin(a, b, c):
    '''
    Don't know the time complexity of the max() function, until we look at the source code.
    '''
    return max(a, b, c)

def max3_if_chain(a, b, c):
    '''
    Doing direct comparison is O(1) time complexity.
    and O(1) space complexity because we use 3 variables.
    But the code is longer and if we have more than 3 numbers, it will be even longer.
    The other code is easier to maintain if we need to add more numbers.
    '''
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def max3_using_sort(a, b, c):
    '''
    The fastest sorting algorithm is O(n log n) time complexity,
    so this solution is O(n log n) time complexity.
    '''
    # after the numbers are sorted, the max is the last element which is at index -1
    return sorted([a, b, c])[-1]

for _ in range(5):
    x, y, z = [random.randint(-100, 100) for _ in range(3)]
    print(f"max3_builtin({x, y, z})       =  {max3_builtin(x, y, z)}")
    print(f"max3_if_chain({x, y, z})      =  {max3_if_chain(x, y, z)}")
    print(f"max3_using_sort({x, y, z})    =  {max3_using_sort(x, y, z)}")
    assert max3_builtin(x, y, z) == max3_if_chain(x, y, z) == max3_using_sort(x, y, z)