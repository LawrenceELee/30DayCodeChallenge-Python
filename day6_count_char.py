'''
Write a program to count the occurrences of a specific character in a string.
'''

# using python built-in functions count(), lower()
def count_char_builtin(input_str, input_char_to_compare):
    return input_str.lower().count(input_char_to_compare)

input1 = "The quick brown fox jumps over the lazy dog."

char_to_cmp = "o"
print(f"there are {count_char_builtin(input1, char_to_cmp)} {char_to_cmp}'s in '{input1}'")

char_to_cmp = "T"
print(f"there are {count_char_builtin(input1, char_to_cmp)} {char_to_cmp}'s in '{input1}'")

char_to_cmp = "q"
print(f"there are {count_char_builtin(input1, char_to_cmp)} {char_to_cmp}'s in '{input1}'")

# this didn't work like I expected, since it compares the entire string
char_to_cmp = 'aeiouAEIOU'
print(f"there are {count_char_builtin(input1, char_to_cmp)} {char_to_cmp}'s in '{input1}'")


# spend a little more time to build the frequency count of chars, so that it can be reused for multiple char comparisons
def build_char_counts(input_str):
    char_counts = {}

    # don't use lower, case-sensitive
    for char in input_str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # return the frequency count of chars
    return char_counts

# build the char counts for the input string
char_counts = build_char_counts(input1)
while(True):
    input_str = input("Enter a string to count (leave blank to exit program): ")
    char_set = set(input("Enter a character(s) to count (leave blank to exit program): "))
    
    if len(char_set) == 0:
        break
    elif len(char_set) > 0:
        total_count = 0
        for char in char_set:
            total_count += char_counts[char]
            print(f"there are {char_counts[char]} {char}'s in '{input_str}'")
        print(f"there are {total_count} {char_set}'s in '{input_str}'")
    else:
        print(f"there are no {char_to_cmp}'s in '{input_str}'")