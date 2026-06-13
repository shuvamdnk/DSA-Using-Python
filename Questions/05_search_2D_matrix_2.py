matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,14,18,22],
          [10,13,16,20,24],
          [18,21,23,26,30]]
target = 21

row = 0
col = len(matrix[0]) - 1
found = False
while col >= 0 and row < len(matrix):
    print(matrix[row][col])
    if target == matrix[row][col]:
        found = True
        break
    elif target < matrix[row][col]:
        col -= 1
    else:
        row += 1

print(found)