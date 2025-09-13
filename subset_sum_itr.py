def subset_sum(lst):
    target = sum(lst)
    if target % 2 == 1: return False
    target //= 2
    dp = [False] * (target + 1)
    for num in lst:
        for i in range(target, num - 1, -1):
            dp[i] = num == i or dp[i - num] or dp[i]
    return dp[target]
