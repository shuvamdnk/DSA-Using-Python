import math
arr = [-2,-4,5,6,98,7]
size  = len(arr)
max_sum = -math.inf
for i in range(size):
    cs = 0
    for j in range(i+1):
        cs += arr[j]
        max_sum = max(max_sum, cs)

print(max_sum)

