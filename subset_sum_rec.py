def subset_sum(lst, target=0, i=0, memo=None):
    if memo is None:
        target = sum(lst)
        if target % 2 == 1: return False
        target //= 2
        memo = {}
    key = (target, i)
    if key in memo: return memo[key]
    if target == 0: return True
    if i == len(lst): return False
    take = subset_sum(lst, target - lst[i], i + 1, memo)
    leave = subset_sum(lst, target, i + 1, memo)
    memo[key] = take or leave
    return memo[key]

print(subset_sum([1, 2, 3, 4]))
print(subset_sum([1, 5, 1, 5]))
print(subset_sum([1, 2, 3, 5]))