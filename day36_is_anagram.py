'''
Write a Python program to check if two strings are anagrams
'''

'''
Ideas/algorithms/approaches:
1. sort the strings and compare them, if they are anagrams, the sorted results will be the same for both
    a. time complexity: O(n * logn)
    b. space complexity: O(1)
2. use a collection/data structure (for ex. dictionary, Counter, etc.) to count the frequency of each character in both strings, if the dictionaries are the same, the strings are anagrams
    a. time complexity: O(n)
    b. space complexity: O(n)
'''

'''
sorting approach
time complexity: O(n * logn)
space complexity: O(1)
'''
def is_anagram_using_sorting(s1, s2):
    # we can make a minor improvement to the code by checking the length of the strings first, if the lengths are different, the strings can NEVER be anagrams
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)

'''
Counter approach
time complexity: O(n)
space complexity: O(n)
'''
from collections import Counter
def is_anagram_using_counter(s1, s2):
    return Counter(s1) == Counter(s2)

'''
Dictionary approach
time complexity: O(n)
space complexity: O(n)
'''
def is_anagram_using_dict(s1, s2):
    # we can make a minor improvement to the code by checking the length of the strings first, if the lengths are different, the strings can NEVER be anagrams
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    # build the frequency dictionary for each string
    for char1 in s1:
        if char1 in d1:
            d1[char1] += 1
        else:
            d1[char1] = 1
        #d1[char1] = d1.get(char1, 0) + 1   #pythonic version of the above if-else statement

    # this does the same thing as the above for loop, but the code is more concise and pythonic
    for char2 in s2:
        d2[char2] = d2.get(char2, 0) + 1

    for key in d1:
        if d1[key] != d2.get(key, 0):
            return False

    # dict1 and dict2 have the same keys and values, so they are anagrams
    return True

    # python can compare dictionaries directly using '==' operator
    # if you are using other programming languages, you will need to check the keys and values of the dictionaries
    #return d1 == d2

print(f"is_anagram_using_sorting('listen', 'silent'): {is_anagram_using_sorting('listen', 'silent')}")
print(f"is_anagram_using_sorting('listen', 'listens'): {is_anagram_using_sorting('listen', 'listens')}")
print(f"is_anagram_using_counter('listen', 'silent'): {is_anagram_using_counter('listen', 'silent')}")
print(f"is_anagram_using_counter('listen', 'listens'): {is_anagram_using_counter('listen', 'listens')}")
print(f"is_anagram_using_dict('listen', 'silent'): {is_anagram_using_dict('listen', 'silent')}")
print(f"is_anagram_using_dict('listen', 'listens'): {is_anagram_using_dict('listen', 'listens')}")
print(f"is_anagram_using_dict('listen', 'silent'): {is_anagram_using_dict('listen', 'silent')}")

# unit tests
assert is_anagram_using_sorting('listen', 'silent') == True
assert is_anagram_using_sorting('listen', 'listens') == False
assert is_anagram_using_counter('listen', 'silent') == True
assert is_anagram_using_counter('listen', 'listens') == False
assert is_anagram_using_dict('listen', 'silent') == True
assert is_anagram_using_dict('listen', 'listens') == False
assert is_anagram_using_dict('listen', 'silent') == True
assert is_anagram_using_dict('listen', 'listens') == False
print("all tests passed.")


import random
import string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#random_string = generate_random_string(1000000)
#print(f"random_string: {random_string}")

'''
import time
start_time = time.time()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
'''

import timeit
# define the function to be timed
n = 10
s1 = generate_random_string(n)
s2 = generate_random_string(n)
def wrapper_to_time_anagram_sort():
    is_anagram_using_sorting(s1, s2)
def wrapper_to_time_anagram_counter():
    is_anagram_using_counter(s1, s2)
def wrapper_to_time_anagram_dict():
    is_anagram_using_dict(s1, s2)

# time the function executions
execution_time = timeit.timeit(wrapper_to_time_anagram_sort, number=1)
print(f"time for anagram using sort:    {execution_time: .10f} seconds")
execution_time = timeit.timeit(wrapper_to_time_anagram_counter, number=1)
print(f"time for anagram using counter: {execution_time: .10f} seconds")
execution_time = timeit.timeit(wrapper_to_time_anagram_dict, number=1)
print(f"time for anagram using dict:    {execution_time: .10f} seconds")
'''
seconds are not the "correct" way to analyze the time complexity of an algorithm
n is the size of the input, in this case the input size is the length of the string
for small n, the time difference is negligible
but for large n, the time difference is significant

for (n) string length = 10
time for anagram using sort:     0.0000117000 seconds     # for small input, sort might be faster than counter and dict
time for anagram using counter:  0.0001418000 seconds
time for anagram using dict:     0.0000145000 seconds

for (n) string length = 10000000
time for anagram using sort:     3.5311440000 seconds
time for anagram using counter:  1.4402866000 seconds
time for anagram using dict:     1.7400439000 seconds

for (n) string length = 100000000
time for anagram using sort:     41.9502376000 seconds
time for anagram using counter:  10.6459267000 seconds
time for anagram using dict:     19.9958656000 seconds

for (n) string length = 1000000000
time for anagram using sort:  599.7853829000 seconds
time for anagram using dict:  321.3527809000 seconds
'''