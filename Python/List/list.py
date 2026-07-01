# li = []

# li.append(1)
# li.append(2)
# li.append(3)
# li.append(4)
# li.append(2)

# # return index of a value - first occurrence
# print(li.index(2))

# # return index of a value - from the given index range
# print(li.index(2,2,len(li)))
# print(li.index(2,0,len(li) -1))

# # return the number of occurrences of a value
# print(li.count(2))

# # insert a value at a given index
# li.insert(1,10)

# # removes the first occurrence of the value
# li.remove(2)

# # Remove the last item from the list and return it
# print(li.pop())
# # Remove the item at the given index and return it
# print(li.pop(0))

# # sort the list in ascending order
# li.sort()

# # reverse the list
# li.reverse()

# # add the element to index -1 and shift the element of -1 to the right
# li.insert(-1,12)

# # print(li[-1])
# print(li)
# # remove range of elements from index 1 to 3
# del li[1:3]

# print(li)

# # Find a value in the list
# if 12 in li:
#     print("12 is present in the list")

# # len of a list
# print(len(li))

# # check empty or not
# print(len(li) == 0)

# ============================== Access Value ==============================
l1 = [2,3,5,1,8,4,12,10,6,7]
print(l1)
# Access value by index
print(l1[0])

# Access value by index range
print(l1[0:6])

# Access value by negative index
print(l1[-1])

# Access element by negative index range
print(l1[-3:-1])

# Reverse the list
print(l1[::-1])

# Reverse the list from index 7 to 5
print(l1[:5:-1])


print(l1[:3:-2])

# Empty array 6 to 9 with step - 1
print(l1[6:9:-1])