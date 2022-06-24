"""

Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
from typing import List


def product_array(arr: List[int]) -> List[int]:
    result = [1] * len(arr)
    for i, n in enumerate(arr):
        for j, m in enumerate(result):
            if i != j:
                result[j] = m * n
    return result


if __name__ == '__main__':
    print(product_array([1, 2, 3, 4, 5]))
