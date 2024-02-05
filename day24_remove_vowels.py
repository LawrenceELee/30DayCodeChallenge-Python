'''
Write a program to remove vowels from a given string.
'''


'''
Different ways to remove vowels from a string:
1. list comprehension
2. str.replace() function
3. str.translate() function
4. regular expression, re.sub() function
'''

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def remove_vowels_using_list_comprehension(input_str):
    return ''.join([letter for letter in input_str if letter not in vowels])

def remove_vowels_using_str_replace(input_str):
    for vowel in vowels:
        input_str = input_str.replace(vowel, '')
    return input_str

def remove_vowels_using_str_translate(input_str):
    return input_str.translate({ord(vowel): None for vowel in vowels})

def remove_vowels_using_re_sub(input_str):
    import re
    return re.sub(r'[aeiouAEIOU]', '', input_str)

# test cases
input_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices nibh neque, et accumsan quam interdum at."
print(f"input_str: {input_str}")
print(f"remove_vowels_using_list_comprehension: {remove_vowels_using_list_comprehension(input_str)}")
print(f"remove_vowels_using_str_replace:        {remove_vowels_using_str_replace(input_str)}")
print(f"remove_vowels_using_str_translate:      {remove_vowels_using_str_translate(input_str)}")
print(f"remove_vowels_using_re_sub:             {remove_vowels_using_re_sub(input_str)}")

input_str = "aeiouAEIOU 1234567890"
print(f"input_str: {input_str}")
print(f"remove_vowels_using_list_comprehension: {remove_vowels_using_list_comprehension(input_str)}")
print(f"remove_vowels_using_str_replace:        {remove_vowels_using_str_replace(input_str)}")
print(f"remove_vowels_using_str_translate:      {remove_vowels_using_str_translate(input_str)}")
print(f"remove_vowels_using_re_sub:             {remove_vowels_using_re_sub(input_str)}")