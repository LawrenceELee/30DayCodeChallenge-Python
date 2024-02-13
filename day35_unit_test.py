'''
Write a simple unit test for a function that adds two numbers
'''

'''
The different ways to use test code in Python:
1. assertions using "assert" keyword/statement
2. assertions using "unittest" module
3. doctest module/library

I'm not a test automation expert, so double check the following:
* When unit testing, you can't just test for the positive cases, you also have to test for the negative cases too.

    * expected result: pass -> and test cases passes (true positive)
    * expected result: pass -> and test cases fails (false negative???)

    * expected result: fail -> and test cases fails (true negative???)
    * expected result: fail -> and test cases passes (false positive???)

The reason for have true positive, false negative, true negative, and false positive
is that if the add function gets changed in the future,
you want to make sure the expected results are still the same.

Bonus: try testing a subtraction function with test cases 1.2 minus 1.0, what number was returned, is this your expected result?

'''

# write a simple add function, which we will test
def add(a, b):
    # introducing a bug to my add fuction
    if a == 0 and b == 0:
        return 100
    else:
        return a + b

# The code will raise an AssertionError, because the second and third assertions are false
def test_add_using_assert_passing_test_cases():
    try:
        assert add(1, 2) == 3
    except AssertionError:
        print("ERROR: Some tests (which should have passed) failed")
    else:
        print("All passing test cases have passed")
def test_add_using_assert_failing_test_cases():
    try:
        assert not add(0, 0) == 100
    except AssertionError:
        print("ERROR: Some tests (which should have failed) passed")
    else:
        print("All failing test cases have failed")   
def test_add_using_assert():
    print("Testing add using 'assert' keyword/statment...")
    test_add_using_assert_passing_test_cases()
    test_add_using_assert_failing_test_cases()
    print("Done with testing using 'assert' keyword/statment...")
    print()
test_add_using_assert()     # this will run the test above


'''
Normally, you would have the test code in a separate file, but I'm putting it here for simplicity.
The output will be wrong when you run the code, it will say "Ran 0 tests in 0.000s" and "OK". b/c they are not in a separate files.
'''
# this needs to be named test_add.py and the original file needs to be named add.py
# unit tests using the python unittest module/library
import unittest
def test_add_using_unittest():
    class TestAdd(unittest.TestCase):
        def test_add_pass(self):
            try:
                self.assertEqual(add(1, 2), 3)
            except AssertionError:
                print("Some tests (which should have passed) failed")
            else:
                print("All passing test cases have passed")
        def test_add_fail(self):
            try:
                self.assertNotEqual(add(0, 0), 100)
            except AssertionError:
                print("Some tests (which should have failed) passed")
            else:
                print("All failing test cases have failed")   

if __name__ == '__main__': # this is needed to run the test below
    print("Testing add using 'unittest' module...")
    unittest.main() # this will run the test above
    print("Done with testing using 'unittest' module...")
    print()
