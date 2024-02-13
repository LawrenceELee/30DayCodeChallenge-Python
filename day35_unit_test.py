'''
Write a simple unit test for a function that adds two numbers
'''

'''
The different ways to use assertions in Python:
1. "assert" keyword/statement
2. "unittest" module

I'm not a test automation expert, so double check the following:
* When unit testing, you can't just test for the positive cases, you also have to test for the negative cases too.

    * expected result: pass -> and test cases passes (true positive)
    * expected result: pass -> and test cases fails (false negative???)

    * expected result: fail -> and test cases fails (true negative???)
    * expected result: fail -> and test cases passes (false positive???)

The reason for have true positive, false negative, true negative, and false positive
is that if the add function gets changed in the future,
you want to make sure the expected results are still the same.

Normally, you would have the test code in a separate file, but I'm putting it here for simplicity.
'''

# write a simple add function, which we will test
def add(a, b):
    return a + b

# The code will raise an AssertionError, because the second and third assertions are false
def test_add_using_assert_passing_test_cases():
    try:
        assert add(1, 2) == 3
    except AssertionError:
        print("Some tests (which should have passed) failed")
    else:
        print("All passing test cases have passed")
def test_add_using_assert_failing_test_cases():
    try:
        assert not add(1, 2) == 100
    except AssertionError:
        print("Some tests (which should have failed) passed")
    else:
        print("All failing test cases have failed")   
def test_add_using_assert():
    print("Testing add using 'assert' keyword/statment...")
    test_add_using_assert_passing_test_cases()
    test_add_using_assert_failing_test_cases()
    print("Done with testing using 'assert' keyword/statment...")
    print()
test_add_using_assert()     # this will run the test above


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
                self.assertNotEqual(add(1, 2), 100)
            except AssertionError:
                print("Some tests (which should have failed) passed")
            else:
                print("All failing test cases have failed")   
print("Testing add using 'unittest' module...")
unittest.main() # this will run the test above
print("Done with testing using 'unittest' module/library...")
