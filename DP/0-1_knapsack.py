# 0 1 knapsack recursion solution

# def knapcack_0_1(w,wt,val,n):
#     if n == 0 or w == 0:
#         return 0

#     if wt[n-1] > w:
#         return knapcack_0_1(w,wt,val,n-1)
#     else:
#         return max(val[n-1] + knapcack_0_1(w-wt[n-1],wt,val,n-1),knapcack_0_1(w,wt,val,n-1))


# if __name__ == '__main__':
#     val = [60, 100, 120]
#     wt = [10, 20, 30]
#     w = 50
#     n = len(val)
#     print(knapcack_0_1(w,wt,val,n))



# Dynamic Programming Solution
def dp_knapsack_0_1(w,wt,val,n):
    dp = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] > j:
                dp[i][j] = dp[i-1][j]    
            else:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]] , dp[i-1][j])

    return dp[n][w]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50
    n = len(val)
    print(dp_knapsack_0_1(w,wt,val,n))


