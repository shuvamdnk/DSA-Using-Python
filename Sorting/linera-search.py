def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f'{key} Found at position {i}')
            break
    else:
        print(f"{key} not found")    


n = int(input("Enter Array Size "))
ele = []
for i in range(n):
    e = int(input())
    ele.append(e)

key = int(input('Enter the key search : '))
linear_search(ele,key)


# Time complexity in O(N)