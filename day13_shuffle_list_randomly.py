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
    # shuffle will modify the list, so you need to make a copy of the original lsit if you want to keep it
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
print(f"sorted_list  : \t{sorted_list_nums}")   # the sorted list has been modified at this point
print(f"shuffle_list : \t{shuffle_list(sorted_list_nums)}")

sorted_list_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(f"sorted_list  : \t{sorted_list_letters}")
print(f"shuffle_built: \t{shuffle_builtin(sorted_list_letters)}")
print(f"sorted_list  : \t{sorted_list_letters}")   # the sorted list has been modified at this point
print(f"shuffle_list : \t{shuffle_list(sorted_list_letters)}")


# the below code is from: https://github.com/nverbic/python-days-of-code/blob/main/src/13%20Day/shuffle_list.py
''' #13 day challenge:
    Write a program to shuffle the elements of a list randomly

    Output:
    Original list:
    [9, 2, 9, 7, 8, 6, 2, 3, 9, 5]

    Shuffled with random.shuffle:
    [9, 7, 9, 2, 2, 6, 5, 8, 9, 3]
    Shuffled with random.sample:
    [8, 6, 9, 3, 2, 9, 5, 2, 7, 9]
    Shuffled with numpy.random.shuffle:
    [5, 7, 9, 2, 9, 9, 8, 6, 3, 2]

    Performances measured on a list of 100000 items, running code 1000 times.

    Total execution time using random.shuffle: 91.7363224 seconds
    Average time per execution: 0.0917363224 seconds

    Total execution time using random.sample: 94.4629884 seconds
    Average time per execution: 0.0944629884 seconds

    Total execution time using numpy.random.shuffle: 56.1840821 seconds
    Average time per execution: 0.0561840821 seconds
'''

import random
import timeit
import numpy as np

PREFORMANCE_SAMPLE = 100000
NUMBER_OF_RUNS = 1000

def shuffle(my_list):
    ''' Use random.shuffle '''
    random.shuffle(my_list)
    return my_list

def shuffle_sample(my_list):
    ''' Use random.sample '''
    shuffled_list = random.sample(my_list, len(my_list))
    return shuffled_list

def shuffle_numpy(my_list):
    ''' Use numpy.random.shuffle '''
    np.random.shuffle(my_list)
    return my_list

def wrapper_shuffle():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle(my_list)

def wrapper_shuffle_sample():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle_sample(my_list)

def wrapper_shuffle_numpy():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle_numpy(my_list)

def wrapper_shuffle_fisher_yates():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle_list(my_list)

def measure_performance():
    ''' Measure the performance '''
    execution_time_shuffle = round(timeit.timeit(wrapper_shuffle, number=NUMBER_OF_RUNS), 10)
    average_time_shuffle = execution_time_shuffle / NUMBER_OF_RUNS
    execution_time_sample = round(timeit.timeit(wrapper_shuffle_sample, number=NUMBER_OF_RUNS), 10)
    average_time_sample = execution_time_sample / NUMBER_OF_RUNS
    execution_time_numpy = round(timeit.timeit(wrapper_shuffle_numpy, number=NUMBER_OF_RUNS), 10)
    average_time_numpy = execution_time_numpy / NUMBER_OF_RUNS
    execution_time_law = round(timeit.timeit(wrapper_shuffle_fisher_yates, number=NUMBER_OF_RUNS), 10)
    average_time_law = execution_time_numpy / NUMBER_OF_RUNS

    print(f"\nPerformances measured on a list of {PREFORMANCE_SAMPLE} items, " \
          f"running code {NUMBER_OF_RUNS} times.\n")
    print(f"Total execution time using random.shuffle: {execution_time_shuffle} seconds")
    print(f"Average time per execution: {average_time_shuffle} seconds\n")
    print(f"Total execution time using random.sample: {execution_time_sample} seconds")
    print(f"Average time per execution: {average_time_sample} seconds\n")
    print(f"Total execution time using numpy.random.shuffle: {execution_time_numpy} seconds")
    print(f"Average time per execution: {average_time_numpy} seconds\n")
    print(f"Total execution time using law's shuffle: {execution_time_law} seconds")
    print(f"Average time per execution: {average_time_law} seconds\n")

if __name__ == "__main__":
    my_list = [random.randint(0, 10) for _ in range(10)]
    print(f"Original list:\n{my_list}\n")
    result = shuffle(my_list)
    print(f"Shuffled with random.shuffle:\n{result}")
    result = shuffle_sample(my_list)
    print(f"Shuffled with random.sample:\n{result}")
    result = shuffle_numpy(my_list)
    print(f"Shuffled with numpy.random.shuffle:\n{result}")
    result = shuffle_list(my_list)
    print(f"Shuffled with law's shuffle:\n{result}")
    measure_performance()