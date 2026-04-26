# Recursive Solution
from operator import le
import sys

def matrixChainOrder(arr,i,j):
    if i == j:
        return 0

    temp = sys.maxsize
    for k in range(i,j):
        cost = (matrixChainOrder(arr,i,k)  
        + matrixChainOrder(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j]))   

        if cost < temp:
            temp = cost

    return temp        

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    n = len(arr) 
    print(matrixChainOrder(arr,1,n-1))   

