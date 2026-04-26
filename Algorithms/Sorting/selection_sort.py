# import math
# def selection_sort(arr,size):
#     for i in range(size-1):
#         min_index_value = i
#         for j in range(i+1,size):
#             if arr[min_index_value] > arr[j]:
#                 arr[j], arr[min_index_value] = arr[min_index_value], arr[j]
#     print_arr(arr)

# def print_arr(arr):
#     for i in arr:
#         print(i,end=" ")

# def find_minimum(arr):
#     min = math.inf
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#     return min

# if __name__ == '__main__':
#     arr = [45,12,65,5,87,23,69,1]
    # size = int(input('Enter the array size : '))
    # for i in range(size):
    #     ele = int(input(f'Enter {i+1} element -> '))
    #     arr.append(ele)
    # selection_sort(arr,len(arr))

    # print(find_minimum(arr))


# time complxity = O(n^2)

# Selection Sort -->
# arr = [5,2,3,1,4]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1,len(arr)):
#         if arr[min_index] > arr[j]:
#             min_index = j

#     arr[i], arr[min_index] = arr[min_index], arr[i]    

 
# print(arr)

arr = [85,12,54,96,105,102]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]       

     

print(arr)    
