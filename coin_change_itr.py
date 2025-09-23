def coin_change(coins, target):
    dp = [0] * (target + 1)
    for i in range(1, target + 1):
        for coin in coins:
            if i >= coin:
                if dp[i]:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    dp[i] = dp[i - coin] + 1

    return dp[target]
