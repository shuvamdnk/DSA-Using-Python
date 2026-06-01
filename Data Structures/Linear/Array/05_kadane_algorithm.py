# Brute Force Approach
import math
arr = [2, 3, -8, 7, -1, 2, 3]
size = len(arr)

# for i in range(size):
#     for j in range(i+1):
#         for k in range(j,i+1):
#             print(arr[k], end="")
#         print("", end=" ")
#     print("")

# 53. Maximum Subarray - Kadane's Algorithm - LeetCode

current_sum = 0
max_sum = -math.inf
for i in range(size-1):
    current_sum += arr[i]
    max_sum = max(current_sum, max_sum)

    if current_sum < 0:
        current_sum = 0

print(max_sum)
