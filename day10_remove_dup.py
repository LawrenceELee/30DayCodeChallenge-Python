'''
Write a program to remove duplicates from a list.
'''

'''
Like all programming problems, there are multiple ways/approaches/algorithsm to solve this problem.

Ideas:
1. brute-force using 2 nested loops to check current element with all other elements in the list
    a. typically during a techincal interview, they will ask you to write this to make sure you understand loops.
2. we use a dict/hashmap/set to keep count of each element.
    a. there are many variations of this approach where we use a set() or list/array
3. use the built-in set() data structure to remove duplicates
    a. typically this isn't accepted in technical interviews because it is too easy and doesn't show your coding skills
    b. the built-in set() data structure does all the hard work for you.

It is important to understand the time and space complexities and the trade-offs between the different approaches/alg.
'''

def remove_dup_brute_force(input_list):
    '''
    Time complexity:    O(n^2)  (quadradic time complexity)
    Space complexity:   O(1)    (no extra space is used)
    '''
    result = []
    # pick the current element "i"
    for i in range(len(input_list)):
        # compare current element "i" with all other elements in the list
        for j in range(i+1, len(input_list)):
            # if duplicate found, we don't add the duplicate to our output
            if input_list[i] == input_list[j]:
                break

        # if no duplicate found, add it to the result list
        result.append(input_list[i])

    return result

# use dict/hashmap to keep count of each element, if count is more than 1, remove the duplicate
def remove_dup_dict(input_list):
    '''
    Time complexity:    O(n)    (linear time complexity)
    Space complexity:   O(n)    (linear extra space is used to store dict)
    '''
    uniques = {}
    result = []
    # traverse input_list and keep count of each element
    for i in range(len(input_list)):

        # if this is the 1st time we see this element, then set count to 1
        if input_list[i] not in uniques:
            uniques[input_list[i]] = True
            result.append(input_list[i])
        # otherwise, we have seen this element before and the current element is a duplicate and we don't do anything

    return result

# put all the elements in a set and the set will automatically remove duplicates
def remove_dup_set(input_list):
    '''
    Time complexity:    O(n)    (linear time complexity)
    Space complexity:   O(n)    (linear extra space is used to store set)
    '''
    return set(input_list)


# generate a list of random integers between 1 and 10 5 times
import random
input1 = [random.randint(1, 5) for i in range(20)]
print(f"input1: {input1}")

# print the output as sorted list for easy visual comparision
print(f"remove_dup_brute_force(input1): {remove_dup_brute_force(input1)}")
print(f"remove_dup_dict(input1): {sorted(list(remove_dup_dict(input1)))}")      
print(f"remove_dup_set(input1): {sorted(list(remove_dup_set(input1)))}")
#assert remove_dup_brute_force(input1) == remove_dup_dict(input1) == remove_dup_set(input1)