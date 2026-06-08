arr = [1, 2, 2, 3, 4]
num = None
unq_arr = []
arr.sort()
for i in arr:
    if i == num:
        continue
    else:
        num = i
        unq_arr.append(i)
        
print(unq_arr)

# =============================================================
arr = [1, 2, 2, 3, 4]
arr.sort()
unq_arr = []

for i in arr:
    if not unq_arr or i != unq_arr[-1]:
        unq_arr.append(i)
print(unq_arr)

# =============================================================
arr = [1, 2, 2, 3, 4]
unq_arr = list(dict.fromkeys(arr))
print(unq_arr)

# =============================================================
arr = [1, 2, 2, 3, 4]
unq_arr = list(set(arr))
print(unq_arr)