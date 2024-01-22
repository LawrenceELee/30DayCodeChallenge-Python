'''
Write a program to shuffle the elements of a list randomly.
'''

'''
Ideas:
1. use the Python built-in shuffle() function

2. implement the Fisher-Yates shuffle algorithm
There is a well known algorithm called the Fisher-Yates shuffle algorithm to shuffle a list randomly.
* https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
* https://bost.ocks.org/mike/shuffle 

If you are wondering why we would ever need to shuffle a list randomly, here are some examples:
1. shuffling a deck of cards
2. shuffling a list of songs
3. the 1st step in the quicksort algorithm is to shuffle the list randomly
    a. bonus points if you can answer why we need to shuffle the list randomly before quicksort
'''

import random

# this is the Python built-in shuffle() function
def shuffle_builtin(input_list):

    # we use the built-in shuffle() function, which will shuffle input_list in-place
    random.shuffle(input_list)
    return input_list

# underneath the hood, the built-in shuffle() function uses the Fisher-Yates shuffle algorithm
# https://softwareengineering.stackexchange.com/questions/215737/how-python-random-shuffle-works
# python source code: https://hg.python.org/cpython/file/8962d1c442a6/Lib/random.py#l256 
def shuffle_list(input_list):

    # we use the built-in enumerate() function to get the index and value of each element in the list
    for i, _ in enumerate(input_list):

        # generate a random index between 0 and i, note this is from 0 to i, not 0 to len(input_list)
        rand_index = random.randint(0, i) 

        # swap the element at index i with the element at random index
        input_list[i], input_list[rand_index] = input_list[rand_index], input_list[i]

    return input_list

sorted_list_nums = [i for i in range(-10, 11)]
print(f"sorted_list  : \t{sorted_list_nums}")
print(f"shuffle_built: \t{shuffle_builtin(sorted_list_nums)}")
print(f"shuffle_list : \t{shuffle_list(sorted_list_nums)}")

sorted_list_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(f"sorted_list  : \t{sorted_list_letters}")
print(f"shuffle_built: \t{shuffle_builtin(sorted_list_letters)}")
print(f"shuffle_list : \t{shuffle_list(sorted_list_letters)}")