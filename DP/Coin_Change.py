from cmath import inf

def coin_change(coin,amt):
    s = len(coin)
    dp = [[0 for i in range(amt+1)] for i in range(s+1)]

    for i in range(s+1):
        for j in range(amt+1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = inf
            elif coin[i-1] > amt:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(1 + dp[i][j-coin[i-1]], dp[i-1][j])
    return dp[s][amt]                 

if __name__ == '__main__':
    print(coin_change([1,2,5],11))

                