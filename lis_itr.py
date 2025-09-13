def lis(lst):
    dp = [[x] for x in lst]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            take = dp[i] + [lst[j]] if lst[j] > dp[i][-1] else dp[j]
            leave = dp[j]
            dp[j] = max(take, leave, key=len)
    return len(max(dp, key=len))

print(lis([0, 1, 0, 3, 2, 3]))
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))