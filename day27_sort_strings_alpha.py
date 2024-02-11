'''
Create a program that sorts a list of strings alphabetically.
'''

'''
Assumptions:
1. the input types are all the same, in this case, they are all strings
2. when sorting strings, case matters, so "A" comes before "a"
3. length of the strings matter, so "a" comes before "aa"
'''

'''
Ideas:
1. use the built-in sort() method
2  use the built-in sorted() function
3. use the built-in sort() method with a custom key function
4. use the built-in sorted() function with a custom key function
'''

# the sort() function will modify the original list
def sort_using_builtin_sort(input_list):
    input_list.sort()
    # we return the input_list b/c it modifies the list in-place
    # sort() doesn't return anything, so it returns None
    return input_list

# sorted() is different than sort() since sorted returns a new list
def sort_using_builtin_sorted(input_list):
    # the sorted() function will return a new list
    # the original list will not be modified
    return sorted(input_list)

'''
def sort_using_builtin_sort_custom_key(input_list):
    # we use the built-in sort() method with a custom key function
    input_list.sort(key=lambda x: x.lower())
    return input_list
'''

import random, string

# test cases
input_strings = [char for char in string.ascii_letters]
print(f"input_strings: \n{input_strings}\n")

unsorted_strings = input_strings.copy()
random.shuffle(unsorted_strings)
print(f"unsorted_strings: \n{unsorted_strings}\n")

random.shuffle(unsorted_strings)
print(f"sort_using_builtin_sort: \n{sort_using_builtin_sort(unsorted_strings)}\n")

random.shuffle(unsorted_strings)
print(f"sort_using_builtin_sorted: \n{sort_using_builtin_sorted(unsorted_strings)}\n")

# assert input_strings == sort_using_builtin_sorted(unsorted_strings) == sort_using_builtin_sort(unsorted_strings)