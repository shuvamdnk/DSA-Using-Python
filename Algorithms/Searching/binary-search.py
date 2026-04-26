# Binary search 
#  Time complexity O(Log(N))
def Binary_search_recursion(l,r,arr,key):
    if r<l:
        return -1
    mid_index = (l + r) // 2
    mid_ele = arr[mid_index]

    # if mid_index >= len(arr) or mid_ele < 0:
    #     return -1

    if mid_ele == key:
        return mid_index
    if mid_ele > key:
        r = mid_index - 1
    else:
        l = mid_index + 1  
    return Binary_search_recursion(l,r,arr,key)

    

def Binary_search_iteration(arr,key):
    left_index = 0
    right_index = len(arr)-1
   
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = arr[mid_index]
        if mid_value == key:
            return mid_index
        if mid_value < key:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1            


arr = [1,2,3,4,5,6,7,8,9,10]
key = int(input('Enter the kwy to search : '))

# res = Binary_search_recursion(0,len(arr)-1,arr,key)
res = Binary_search_iteration(arr,key)
print(f'{key} found at the position {res}')
