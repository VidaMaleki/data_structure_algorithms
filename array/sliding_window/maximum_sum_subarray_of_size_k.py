"""Problem: Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.
"""

#Brute Force (O(N*K)):
def max_sum_brute_force(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i + k])
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_brute_force(arr, k))  # Output: 9


#Sliding Window (O(N)):
def max_sum_sliding_window(arr, k):
    max_sum, window_sum = 0, 0
    start = 0
    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_sliding_window(arr, k))  # Output: 9
