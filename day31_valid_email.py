'''
Create a program that checks if a given string is a valid email address.
'''
import random
import string
import re

def is_valid_email(input_email_str):
    return bool(re.fullmatch(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', input_email_str))

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_string_letters_only(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email():
    username = generate_random_string(10)
    domain = generate_random_string(10)
    tld = generate_random_string_letters_only(3)
    return f"{username}@{domain}.{tld}"

for _ in range(10):
    # Generate a random string
    random_string = generate_random_string(10)
    print(f"random_string = {random_string}")
    print(f"is_valid_email(random_string) = {is_valid_email(random_string)}")
    valid_email = generate_email()
    print(f"valid_email = {valid_email}")
    print(f"is_valid_email(valid_email) = {is_valid_email(valid_email)}")
    print()


