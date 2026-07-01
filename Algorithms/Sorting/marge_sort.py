# Marge sort

def marge(arr, start, mid, end):
        i = start
        j = mid + 1
        temp = []
        
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= end:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[start + k] = temp[k]

def margeSort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2

        # left array part
        margeSort(arr, start, mid)
        # right array part
        margeSort(arr, mid + 1, end)

        marge(arr, start, mid, end)
        

arr = [3,4,1,6,2]
margeSort(arr, 0, len(arr)-1)

print(arr)