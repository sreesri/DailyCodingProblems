"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
 find the lowest positive integer that does not exist in the array. The array can contain duplicates
 and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def find_missing_positive_int(input_list):
    input_set = set(input_list)
    for i in range(1,len(input_set) + 2):
        if i not in input_set:
            return i

if __name__ == "__main__":
    input_list = [3, 4, -1, 1]
    print(find_missing_positive_int(input_list))