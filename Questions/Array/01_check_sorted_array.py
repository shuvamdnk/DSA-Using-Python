# Check a array is sorted or not

# arr = [1,2,3,4,5,6,7,8]

# is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# print(is_sorted)


# Recursive Method
arr = [1,2,3,4,5,6,7,8]

def is_sorted(arr):
    if len(arr) <= 1:
        return True
    
    return arr[0] <= arr[1] and is_sorted(arr[1:])
print(is_sorted(arr))
