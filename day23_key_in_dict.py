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
This might work, but you have to surround it with a try-except block to catch the KeyError
'''

'''
I was curious about the performance of these different methods and I found this article: 
++ https://www.scaler.com/topics/check-if-key-exists-in-dictionary-python/

Performance Comparison
++ [] and in operators are the fastest and most efficient way to check if a key exists in dictionary in Python. [] operator, of course, needs to be associated with the try-except block.
++ get() and setdefault() methods lag behind the [] and in operators, since they also perform attribute/value lookup (along with insertion in case of setdefault()), while the other 2 only perform membership check.
++ Using the keys() method is the least efficient method to check if key exists in dictionary in Python, since it involves returning the key-set as well as checking whether the key exists in that set. This entire operation is linear in time, while the ones discussed above are constant in time.
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