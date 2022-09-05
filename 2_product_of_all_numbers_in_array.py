"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
 the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
 If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce


def find_product_of_array(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i == 0:
           split_list = input_list[i + 1:]
        elif i == len(input_list) - 1:
            split_list = input_list[:i]
        else:
            split_list = input_list[:i] + input_list[i+1:]
        print(split_list)
        product = reduce((lambda x, y: x * y), split_list)
        output_list.append(product)
    return output_list


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    print(find_product_of_array(input_list))

    input_list = [3, 2, 1]
    print(find_product_of_array(input_list))