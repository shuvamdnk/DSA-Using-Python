def marge(arr, start, mid, end):
    i = start
    j = mid + 1
    temp = []
    inverseCount = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            inverseCount += (mid - i) + 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= start:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[k + start] = temp[k]
    
    return inverseCount


def margeSort(arr, start, end) -> int :
    if start < end:

        mid = start + (end - start) // 2
        # left array
        leftCount = margeSort(arr, start, mid)
        # right array
        rightCount = margeSort(arr, mid+1, end)

        inverseCount = marge(arr, start, mid, end)

        return leftCount + rightCount + inverseCount

    return 0

arr = [6,3,5,2,7]

print(margeSort(arr, 0, len(arr)-1))
