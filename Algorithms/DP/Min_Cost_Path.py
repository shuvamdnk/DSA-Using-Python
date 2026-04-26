# Recursion

# import sys
# def minCost(arr,x,y):
#     if (x < 0 or y < 0):
#         return sys.maxsize
#     elif x == 0 and y == 0:
#         return arr[x][y]
#     else:
#         return arr[x][y] + min(minCost(arr,x-1,y), minCost(arr,x,y-1), minCost(arr,x-1,y-1))

# if __name__ == '__main__':
#     cost= [ [1, 2, 3],
#         [4, 8, 2],
#         [1, 5, 3] ]
#     print(minCost(cost, 2, 2))


# Dynamic programming

def minCostDp(arr,x,y):

    row = len(arr)
    col = len(arr[0])
    tbl = [[0 for i in range(col)]for i in range(row)]
    
    tbl[0][0] = arr[0][0]

    for i in range(1,x+1):
        tbl[i][0] = tbl[i-1][0] + arr[i][0]

    for j in range(1,y+1):
        tbl[0][j] = tbl[0][j-1] + arr[0][j]    

    for i in range(1,x+1):
        for j in range(1,y+1):
            tbl[i][j] = min(tbl[i-1][j-1], tbl[i][j-1], tbl[i-1][j]) + arr[i][j]

    return (tbl[x][y])    


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCostDp(cost,2,2))

