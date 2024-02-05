'''
Create a program to concate two lists.
'''

'''
The different ways to concatenate two lists are:
1. useing the "+" operator
2. using the extend() function
3. using the list comprehension
4. using the built-in itertools.chain() function
5. using loop and ...:
    a. the built-in append() function
    b. the built-in insert() function
'''

def concat_using_plus_operator(list1, list2):
    return list1 + list2

def concat_using_extend_function(list1, list2):
    list1.extend(list2)
    return list1

def concat_using_list_comprehension(list1, list2):
    return [x for x in list1] + [x for x in list2]

import itertools
def concat_using_itertools_chain(list1, list2):
    return list(itertools.chain(list1, list2))

def concat_using_append_function(list1, list2):
    for x in list2:
        list1.append(x)
    return list1

def concat_using_insert_function(list1, list2):
    for i in range(len(list2)):
        list1.insert(len(list1), list2[i])
    return list1

# test cases
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"list1:                            {list1}")
print(f"list2:                            {list2}")

print(f"concat_using_plus_operator:       {concat_using_plus_operator(list1, list2)}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"concat_using_extend_function:     {concat_using_extend_function(list1, list2)}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"concat_using_list_comprehension:  {concat_using_list_comprehension(list1, list2)}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"concat_using_itertools_chain:     {concat_using_itertools_chain(list1, list2)}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"concat_using_append_function:     {concat_using_append_function(list1, list2)}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"concat_using_insert_function:     {concat_using_insert_function(list1, list2)}")
