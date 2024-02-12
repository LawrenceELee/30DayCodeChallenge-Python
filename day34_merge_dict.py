'''
Write a Python program to merge two Python dictionaries.
'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4, 'e': 5}

# the ** operator is used to merge dictionaries, but it only works in python 3.5+
# https://www.geeksforgeeks.org/merge-two-dictionaries-in-python/
merged_dict = {**dict1, **dict2}
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"merged_dict: {merged_dict}")
print("dict1 and dict2 are unchanged after merging")
print()

# other ways to merge dictionaries
# using the update method
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
dict1.update(dict2)
print("dict1.update(dict2) merges dict2 into dict1")
print(f"dict1 after update: {dict1}")
