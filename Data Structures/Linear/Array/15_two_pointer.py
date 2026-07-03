# Reverse Array useing two pointer

# arr = [1,2,3,4,5,6,7,8]

# start = 0
# end = len(arr) - 1

# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1

# print(arr)

# Remove duplicate

arr = [1,2,2,3,4,4,5,6,7,8]

write = 1

for read in range(1,len(arr)):
    if arr[read -1] != arr[read]:
        arr[write] = arr[read]
        write += 1

print(arr[:write])