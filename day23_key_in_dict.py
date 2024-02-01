'''
Write a program that checks if a key exists in a dictionary.
'''

# the simplest way is to use the "in" keyword that is built into the python language
# this is probably the most pythonic way and the "best" way to solve this problem.
def check_key_using_in_keyword(my_dict, key):
    return key in my_dict

# another way is to use the built-in dictionary function: get() 
def check_key_using_getkey_function(my_dict, key):
    return my_dict.get(key) != None

# another way is to get all the keys in the dictionary using the keys() function and compare it to the key we are looking for
def check_key_using_keys_function(my_dict, key):
    my_keys = my_dict.keys()

    # iterate over all the keys in the dictionary to see if the key exists
    for k in my_keys:
        if k == key:
            return True
    
    # if we iterate through all the keys and we don't find the key, then the key doesn't exist
    return False

'''
We can't use the square bracket syntax to check if a key exists in a dictionary, b/c if the key doesn't exist, it will throw a KeyError
For example: my_dict['z'] will throw a KeyError and crash the program if 'z' doesn't exist in my_dict
'''

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"my_dict: {my_dict}")
key = 'a'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_in_keyword(my_dict, key)}")
key = 'z'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_in_keyword(my_dict, key)}")
key = 'a'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_getkey_function(my_dict, key)}")
key = 'z'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_getkey_function(my_dict, key)}")
key = 'a'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_keys_function(my_dict, key)}")
key = 'z'
print(f"check_key_using_in_keyword:     is {key} in my_dict? answer: {check_key_using_keys_function(my_dict, key)}")