# XOR / only work for even number of duplicate
# arr = [2,2,1,4,4,5,5,2,3,3,2]
# single_ele = 0
# for i in arr:
#     single_ele ^= i

# print(single_ele)

# Odd number of duplicate
arr = [2,2,2,1,1,4,5,5,2,3,3,2]

# unq = None
# arr.sort()

# for i in range(len(arr)-1):
#     if arr[i] != arr[i+1]:
#         unq = arr[i]
#         break

# if not unq:
#     unq = arr[-1]

# print(unq)


count = {}
single_ele = None
for i in arr:
    count[i] = count.get(i, 0) + 1

for key, val in count.items():
    if val == 1:
        single_ele = key

print(single_ele)