'''
Create a program that removes the nth element from a list.
'''

'''
different ways to remove the nth element from a list:
1. use the built-in del statement (imperative way)
2. use the built-in pop() method
3. use the built-in remove() method
4. use slicing (pythonic way)
5. use a list comprehension (pythonic way)
6. use the built-in filter() function (functional way)
7. use shifting and overwriting in-place (imperative way)
'''

def remove_using_builtin_del(input_list, n):
    # the del statement will modify the original list
    del input_list[n]
    # we return the input_list b/c it modifies the list in-place
    # del doesn't return anything, so it this function returns None implicitly

def remove_using_builtin_pop(input_list, n):
    # the pop() method will return the removed element
    # the original list will be modified
    input_list.pop(n)
    #return input_list.pop(n) #if we want the element that was removed, pop will return it

def remove_using_builtin_remove(input_list, n):
    # the original list will be modified
    input_list.remove(n)        # remove() returns None

def remove_using_slicing(input_list, n):
    # slicing will return a new list
    # the original list will not be modified
    return input_list[:n] + input_list[n+1:]

# iterate over original list and create a new list with the nth element removed
# instead of list comprehension, we could use a for loop and if statement
def remove_using_list_comprehension(input_list, n):
    # list comprehension will return a new list, we iterate and skip over nth element
    # the original list will not be modified
    return [input_list[i] for i in range(len(input_list)) if i != n]

def remove_using_for_loop(input_list, n):
    # iterate over the original list and create a new list with the nth element removed
    new_list = []
    for i in range(len(input_list)):
        if i != n:
            new_list.append(input_list[i])
    return new_list

def remove_using_filter(input_list, n):
    # the filter() function will return a new list
    # the original list will not be modified
    return list(filter(lambda x: x != n, input_list))

def remove_using_shifting_overwriting_inplace(input_list, n):
    # the original list will be modified
    for i in range(n, len(input_list)-1):
        input_list[i] = input_list[i+1]
    # remove the last element that is a duplicate after copying over
    input_list.pop()
    #return input_list


# test cases
import string
import random

input_list = list(string.ascii_lowercase)
print(f"input_list:               \n{input_list}")
print()

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
remove_using_builtin_del(input_list, random_idx)
print(f"remove_using_builtin_del: \n{input_list}")
print()
assert random_letter not in input_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
remove_using_builtin_pop(input_list, random_idx)
print(f"remove_using_builtin_pop: \n{input_list}")
print()
assert random_letter not in input_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
remove_using_builtin_remove(input_list, input_list[random_idx])
print(f"remove_using_builtin_remove: \n{input_list}")
print()
assert random_letter not in input_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
# note that the original list is not modified, the returned list is modified
new_list = remove_using_slicing(input_list, random_idx)
print(f"remove_using_slicing:     \n{new_list}")
print()
assert random_letter not in new_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
# note that the original list is not modified, the returned list is modified
new_list = remove_using_list_comprehension(input_list, random_idx)
print(f"remove_using_list_comp:   \n{new_list}")          
print()
assert random_letter not in new_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
# note that the original list is not modified, the returned list is modified
new_list = remove_using_for_loop(input_list, random_idx)
print(f"remove_using_for_loop:    \n{new_list}")
print()
assert random_letter not in new_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
# note that the original list is not modified, the returned list is modified
new_list = remove_using_filter(input_list, input_list[random_idx])
print(f"remove_using_filter:      \n{new_list}")
print()
assert random_letter not in new_list

random_idx = random.randint(0, len(input_list)-1)
random_letter = input_list[random_idx]
print(f"removing n = {random_idx}, letter: {random_letter}")
remove_using_shifting_overwriting_inplace(input_list, random_idx)
print(f"remove_using_overwriting_inplace: \n{input_list}")
assert random_letter not in input_list
