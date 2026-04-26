def swap(start,end,arr):
    arr[start], arr[end] = arr[end], arr[start]

def position(arr,start,end):
    pivot = arr[end]
    i = start - 1
    j = start
    while j <= end-1:
        if(arr[j] <= pivot):
            i += 1
            swap(i,j,arr)
        j += 1
    swap(i+1, end, arr)        

    return i+1

def quick_sort(arr,start,end):
    if(start < end):
        p = position(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)

if __name__ == '__main__':
    arr = [11,3,5,2,87,12,54,32]
    start = 0
    end = len(arr) -1
    quick_sort(arr,start,end)
    print(arr)