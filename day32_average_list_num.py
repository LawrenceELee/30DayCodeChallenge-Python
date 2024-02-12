'''
Create a function that calculates the average of a list of numbers
'''


'''
since it is straight forward how to use a loop to calculate the average of a list of numbers,
I will focus on using data science to clean the data and calculate the average
https://docs.python.org/3/library/statistics.html
'''

from statistics import median
from math import isnan
from itertools import filterfalse

data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
print(f"data:            {data}")

s = sorted(data)  # This has surprising behavior
print(f"sorted:          {s}")

incorrect_med = median(data)  # This result is unexpected
print(f"incorrect_med:   {incorrect_med}")

bad_data = sum(map(isnan, data))    # Number of missing values, elements that are NaN
print(f"bad_data:        {bad_data}") 

clean = list(filterfalse(isnan, data))  # Strip NaN values
print(f"clean:           {clean}")

s = sorted(clean)  # Sorting now works as expected
print(f"sorted:          {s}")

correct_med = median(clean)       # This result is now well defined
print(f"correct_med:     {correct_med}")

mean = sum(clean) / len(clean)  # The mean is well defined
print(f"mean:            {mean}")