'''
not part of the 60 days of python code challenge
example of how to use a decorator
https://www.askpython.com/python/examples/decorators-in-python
'''

# this simple decorator will print the name of the function and the arguments passed to it
def my_decorator(my_function):
    # function definition of my_wrapper
    def my_wrapper(num1, num2):
        print("##", my_function.__name__, "of", num1, "and", num2, "##")
        my_function(num1, num2)

    # we never call/invoke my_wrapper, we define it above and return the function object my_wrapper
    # we return the function, not a a value
    return my_wrapper

'''
Note: Using a decorator will disrupt the function’s metadata. In our example, calling sum.__name__ will return wrapper instead of sum because that is the function we’re essentially using. The docstring will also change depending on what docstring the wrapper has.
To avoid this, simply import wraps from functools and then decorate the wrapper inside the decorator like so:
functools and the wraps function are used to preserve the metadata of the original function
'''
from functools import wraps
def my_decorator_functools(my_function):
    @wraps(my_function)
    def my_wrapper(num1, num2):
        print("##", my_function.__name__, "of", num1, "and", num2, "##")
        my_function(num1, num2)
    return my_wrapper
'''
In this, the wrapper itself is decorated using the metadata of the function so that it retains function meta like __name__ and its docstring.
'''

# we "use it" by adding @my_decorator before the function definition
@my_decorator
def add(num1, num2):
    print(num1 + num2)

# without the decorator
def subtract(num1, num2):
    print(num1 - num2)

@my_decorator_functools
def multiply(num1, num2):
    print(num1 * num2)

# without the decorator
def divide(num1, num2):
    print(num1 / num2)

add(1, 2)
print(f"add.__name__ is {add.__name__}")
print("normal decorators DON'T perserve the metadata of the original function")
print()
subtract(3, 4)
print()
multiply(5, 6)
print(f"multiply.__name__ is {multiply.__name__}")
print("functools wraps decorators DO perserve the metadata of the original function")
print()
divide(7, 8)