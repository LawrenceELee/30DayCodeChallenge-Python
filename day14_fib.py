'''
Write a program to print the first n numbers of a Fibonacci sequence
'''

'''
Here are some things to think about before you start coding:

Mathematically, Fibonacci sequence is defined as: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1
https://en.wikipedia.org/wiki/Fibonacci_sequence

Ideas/algorithms/approaches:
1. Recursive: because of the natural recusive definition of the Fibonacci sequence, we can use recursion to solve this problem
    a. The default version will use O(2^n) (exponential) time complexity, can we improve this?
    b. The default version will use O(n) space complexity for the recursive call stack.
2. Iterative: Using list/array and loop, 
    a. This will use O(n) space complexity.
    b. Can we improve the space complexity of this solution?
3. Closed-form: There is a closed-form formula/solution to the Fibonacci sequence

4. Use python decorators to memoize the recursive solution
'''
import timeit

def fib_rec_simple(n):
    
    # by definition, the Fibonacci sequence is only defined for non-negative integers
    if n < 0:
        raise ValueError("n must be non-negative")

    # base case 1
    if n == 0:
        return 0
    
    # base case 2
    if n == 1:
        return 1

    # general recursive case
    return fib_rec_simple(n-1) + fib_rec_simple(n-2)

# memoization using dictionary as cache (using dict, instead of array so don't have to use inddex)
# using default argument to create a mutable default value, we don't have to pass memoization cache around
# this is dynamic programming, top-down approach
def fib_rec_memo(n, cache={}):

    if n in cache:
        result = cache[n]
    elif n <= 2:
        result = 1
        cache[n] = result
    else:
        cache[n] = fib_rec_memo(n - 2) + fib_rec_memo(n - 1)

    return cache[n]

# closure + decorator + memoization
def memoize(f):
    cache = {}

    # this is the closure function
    def foo(x):
        if x not in cache:
            # f(x) is called here and cache in the array
            cache[x] = f(x)
        return cache[x]
    return foo      # return the closure function
@memoize        # using decorator to memoize the recursive function
def fib_rec_closure(n):
    if n <= 1:
        return n
    else:
        return fib_rec_closure(n - 1) + fib_rec_closure(n - 2)


# functools + decorator + memoization
import functools
def memoize_functools(f):
    cache = {}

    @functools.wraps(f)
    # This line uses the functools.wraps decorator to ensure that the memoized_func retains the original function’s name (f) and docstring.
    # It’s good practice to preserve the original function’s metadata when creating decorators.
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]
    return memoized_func
@memoize_functools
# This decorator is applied to the fibonacci function.
# It effectively replaces fibonacci with the memoized version provided by memoized_func.
def fib_rec_memo_functools(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec_memo_functools(n - 1) + fib_rec_memo_functools(n - 2)

def fib_bottom_up_tabluar(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # create a list to store the Fibonacci numbers
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]

# we can improve on the space complexity of the bottom-up tabular solution by only keeping track of the last two Fibonacci numbers
def fib_bottom_up_iter(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    fn2, fn1 = 0, 1    # seeds
    fn = fn1 + fn2
    for _ in range(2, n + 1):
        fn2 = fn1
        fn1 = fn
        fn = fn1 + fn2
    return fn1      # note, we reture fn1, not fn

def tests(input_n):
    print(f"n = {input_n}")

    print(f"fib_rec_simple({input_n}) =   {fib_rec_simple(input_n)}")
    time_fib_simple = timeit.timeit('fib_rec_simple(10)', number=1000, globals=globals())
    print(f"time_fib_simple({input_n}):               {time_fib_simple: .10f}")

    print(f"fib_rec_memo({input_n}) =     {fib_rec_memo(input_n)}")
    time_fib_memo = timeit.timeit('fib_rec_memo(10)', number=1000, globals=globals())
    print(f"time_fib_memo({input_n}):                 {time_fib_memo: .10f}")

    print(f"fib_rec_closure({input_n}) =  {fib_rec_closure(input_n)}")
    time_fib_closure = timeit.timeit('fib_rec_closure(10)', number=1000, globals=globals())
    print(f"time_fib_rec_closure({input_n}):          {time_fib_closure: .10f}")

    print(f"fib_rec_memo_functools({input_n}) =  {fib_rec_memo_functools(input_n)}")
    time_fib_memo_functools = timeit.timeit('fib_rec_memo_functools(10)', number=1000, globals=globals())
    print(f"time_fib_memo_functools({input_n}):       {time_fib_memo_functools: .10f}")

    print(f"fib_bottom_up_tabluar({input_n}) =   {fib_bottom_up_tabluar(input_n)}")
    time_fib_bottom_up_tabluar = timeit.timeit('fib_bottom_up_tabluar(10)', number=1000, globals=globals())
    print(f"time_fib_bottom_up_tabluar({input_n}):    {time_fib_bottom_up_tabluar: .10f}")

    print(f"fib_bottom_up_iter({input_n}) =      {fib_bottom_up_iter(input_n)}")
    time_fib_bottom_up = timeit.timeit('fib_bottom_up_iter(10)', number=1000, globals=globals())
    print(f"time_fib_bottom_up_iter({input_n}):       {time_fib_bottom_up: .10f}")

    print()

tests(10)
tests(20)
tests(30) 
tests(40) 
tests(45) 
#tests(50) # any n higher than 50 will take a long time for the simple recursive solution
