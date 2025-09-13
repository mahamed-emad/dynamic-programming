def lis(lst, i=0, prev=float("-inf"), memo={}):
    key = (i, prev)
    if key in memo: return memo[key]
    if i == len(lst): return 0
    take = (1 + lis(lst, i + 1, lst[i], memo)) if lst[i] > prev else 0
    leave = lis(lst, i + 1, prev, memo)
    memo[key] = max(take, leave)
    return memo[key]

# print(lis([0, 1, 0, 3, 2, 3]))
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))