# Created by allex at 11.11.2021
# -*- coding: utf-8 -*-
"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Using windowing method"""

    # Maximums
    global_max = -float("inf")  # Lowest possible number to compare (for negative array cases)
    local_max = []

    # Sliding
    for window_size in range(k, 0, -1):
        for window_border in range(window_size, len(nums) + 1):
            local_max.append(sum(nums[window_border - window_size : window_border]))

        # Maximum from all sliding window sums
        maximum = max(local_max)
        if maximum > global_max:
            global_max = maximum
        local_max = []

    return global_max


a = [-1, 0, 0, 10, 25, 25, 25]
print(find_maximal_subarray_sum(a, 1))
