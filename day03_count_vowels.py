'''
write a function to count the number of vowels in a given string
'''


'''
there are many different ways to solve this problem.
the 1st idea I thought up was to traverse the string and use if/case statements and use a counter variable
the solution is not the most elegant and is brute force, but it will solve the problem.
'''

# brute-force traversing string + keeping count
def count_vowels(input_str):
    vowels_count = 0
    for letter in input_str:
        if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
               vowels_count += 1
    return vowels_count

input_test1 = "The quick brown fox jumps over the lazy dog."
print(f"there are {count_vowels(input_test1)} in string: {input_test1}")
assert(count_vowels(input_test1), 11) # I expect my function to tell me that string has 11 vowels.
print("all tests passed successfully!")

'''
Things to think about:
-> having that long if statement to check is kind of ugly
-> what if we want to add 'y' as a vowel, in the future
-> what are some other ways to solve this problem? If you are using Python 3.10, then we can use case/switch?

-> what "container" should we use to hold the vowels? array/list? dict/hashmap? set?
I was wondering what the time complexity of the "in" keyword is. If you are also curious:
    * https://stackoverflow.com/questions/20234935/python-in-operator-speed
    * https://wiki.python.org/moin/TimeComplexity
so changing vowels from a string of characters to a set might be better for large inputs. 
'''
