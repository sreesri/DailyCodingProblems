"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from typing import List


def find_sum(arr: List[int], k: int) -> bool:
    d = []
    for i in arr:
        diff = k - i
        if diff in d:
            return True
        else:
            d.append(i)
    return False


if __name__ == "__main__":
    print(find_sum([10, 15, 3, 7], 17))
    print(find_sum([10, 15, 3, 5], 17))
