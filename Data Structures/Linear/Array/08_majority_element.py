arr = [-1,1,1,1,2,1]
# sorted_arr = sorted(arr)
# arr.sort()

# feq = 0
# num = sorted_arr[0]
# for el in sorted_arr:
#     if feq > (len(sorted_arr) // 2):
#         break
#     if el == num:
#         feq += 1
#     else:
#         num = el
#         feq = 1
#     print(F"num: {num}, el: {el} feq: {feq}")


# print(num)

# Moore's Voting Algorithm
feq = 0
num = arr[0]
for el in arr:
    if feq == 0:
        num = el
    if el == num:
        feq += 1
    else:
        feq -= 1

print(num)
        
        