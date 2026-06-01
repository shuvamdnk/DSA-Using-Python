# arr = [1,5,4,2,1,4,5,1,1,1]
# # Moore's Voting Algorithm
# # Must exist mejority element in the array
# flag = 0
# num = 0
# for i in arr:
#     if flag == 0:
#         num = i
#     if i == num:
#         flag += 1
#     else:
#         flag -= 1
# print(num)


# # ================================================
arr = [1,2,3,4,5,6,7,8]
# May exist majority element in the array
flag = 0
num = 0
for i in arr:
    if flag == 0:
        num = i
    if i == num:
        flag += 1
    else:
        flag -= 1 

count = 0
for i in arr:
    if i == num:
        count += 1
if count > (len(arr) // 2): 
    print(num)
else:
    print("No majority element")