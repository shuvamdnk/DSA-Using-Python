arr = [3,9,8,6,4]
start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        print(mid + 1)
    if mid == len(arr) - 1:
        print(mid - 1)
    if arr[mid - 1] < arr[mid] > arr[mid + 1]:
        print(mid)
    elif arr[mid] > arr[mid - 1]:
        start = mid + 1
    else:
        end = mid - 1
        

