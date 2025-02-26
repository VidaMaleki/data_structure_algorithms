"""Example Problem: Smallest Subarray with Sum ≥ Target 💡 Problem: Given an array of positive numbers and a target sum, find the smallest subarray with a sum ≥ target.
"""

# Sliding Window Solution (O(N)):
import math
def min_subarray_len(target, arr):
    min_length = math.inf
    window_sum, start = 0, 0

    for end in range(len(arr)):
        window_sum += arr[end]
        
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1
    
    return min_length if min_length != math.inf else 0

arr = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target, arr))  # Output: 2 ([4,3] or [3,4])
