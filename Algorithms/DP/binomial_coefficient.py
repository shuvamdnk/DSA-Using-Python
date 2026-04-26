# Recursive solution of bionomial coefficient
# def bionomial_coefficient(n,k):
#     if k > n:
#         return 0
#     elif k == 0 or k == n:
#         return 1
    
    
#     return bionomial_coefficient(n-1,k-1) + bionomial_coefficient(n-1,k)   

# if __name__ == '__main__':
#     print(bionomial_coefficient(5,2));         


# Dynamic Programming Problem
# def bionomialCoff(n,k):
#     c = [[0 for x in range(k+1)] for x in range(n+1) ]
#     # print(c)
#     for i in range(n+1):
#         for j in range(min(i,k)+1):
#             if j==0 or j==i:
#                 c[i][j] = 1
#             else:
#                 c[i][j] = c[i-1][j-1] + c[i-1][j]

#     return c[n][k]               

# if __name__ == '__main__':
#     print(bionomialCoff(5,2))


def binomial_coff(n,k):
    c = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]

    return c[n][k]              



print(binomial_coff(4,2))