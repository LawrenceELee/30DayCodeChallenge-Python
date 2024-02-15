'''
Write a program to iterate through a dictionary and print its keys and values
'''

dict = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple', 'apple': 'green'}
# if there are duplicate keys, dict will only store the last value

for key, value in dict.items():
    print(f"{key}: {value}")