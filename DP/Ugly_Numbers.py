def uglyNumber(n):
    dp = [0]* (n)
    dp[0] = 1
    i2 = i3 = i5 = 0
    next_factor_of_2 = dp[i2]*2
    next_factor_of_3 = dp[i3]*3
    next_factor_of_5 = dp[i5]*5
    # print(next_factor_of_2,next_factor_of_3,next_factor_of_5)

    for i in range(1,n):
        min_factor = min(next_factor_of_2,next_factor_of_3,next_factor_of_5)
        dp[i] = min_factor

        if min_factor == next_factor_of_2:
            i2 += 1
            next_factor_of_2 = dp[i2]*2
        if min_factor == next_factor_of_3:
            i3 += 1
            next_factor_of_3 = dp[i3]*3
        if min_factor == next_factor_of_5:
            i5 += 1
            next_factor_of_5 = dp[i5]*5
    return dp[-1]             


if __name__ == '__main__':
    print(uglyNumber(150))