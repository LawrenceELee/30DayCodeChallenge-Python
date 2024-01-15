'''
Write a program to find the maximum and minimum values in a list.
'''
# classic and direct algirthm, traversing the list with a loop and min/max variables
def min_max_iterative(input_list):
    # initialize min and max with the first element
    min = input_list[0]         
    max = input_list[0]

    # traverse list and find the min and max
    # if the current element is less than min, update min
    # if the current element is more than max, update max
    for curr_num in input_list:
        if curr_num < min:
            min = curr_num
        elif curr_num > max:
            max = curr_num

    #return the tuple-pair of min and max
    return min, max

# sorting algorthm then taking the first and last elements
def min_max_sort(input_list):
    input_list.sort()
    return input_list[0], input_list[-1]

# I am assuming the input array is valid and only contains ints
input1 = [1,2,3,4,5]
input2 = [1,2,3,4,5,6,7,8,9,10]
input3 = [10,9,8,7,6,5,4,3,2,1]
input4 = [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5]

print(f"\nmin and max (iterative algorithm): {min_max_iterative(input1)}")
print(f"min and max (sort algorithm): {min_max_iterative(input1)}")

print(f"\nmin and max (iterative algorithm): {min_max_iterative(input2)}")
print(f"min and max (sort algorithm): {min_max_iterative(input2)}")

print(f"\nmin and max (iterative algorithm): {min_max_iterative(input3)}")
print(f"min and max (sort algorithm): {min_max_iterative(input3)}")

print(f"\nmin and max (iterative algorithm): {min_max_iterative(input4)}")
print(f"min and max (sort algorithm): {min_max_iterative(input4)}")