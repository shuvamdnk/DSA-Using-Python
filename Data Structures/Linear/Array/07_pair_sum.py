# Brout Force Approach
arr = [2,7,11,13]
target = 13
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])

# Two pointer approach
# Array is already sorted
i, j = 0 , len(arr) -1

while i < j:
    if arr[i] + arr[j] == target:
        print(arr[i] , arr[j])
        break
    
    if arr[i] + arr[j] > target:
        j -= 1

    if arr[i] + arr[j] < target:
        i -= 1
