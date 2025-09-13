def rob(vals):
    dp = [0] * (len(vals) + 1)
    dp[1] = vals[0]
    dp[2] = vals[1]
    for i in range(3, len(vals) + 1):
        dp[i] = vals[i - 1] + max(dp[i - 2], dp[i - 3])
    return max(dp[len(vals)], dp[len(vals) - 1])

print(rob([1, 2, 3, 1]))