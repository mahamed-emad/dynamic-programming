def target_sum_way(nums, target, i=0, memo=None):
    if memo is None: memo = {}
    key = (target, i)
    if key in memo: return memo[key]
    if i == len(nums):
        if target == 0: return 1
        if target != 0: return 0
    pos = target_sum_way(nums, target - nums[i], i + 1, memo)
    neg = target_sum_way(nums, target + nums[i], i + 1, memo)
    memo[key] = pos + neg
    return memo[key]

print(target_sum_way([1, 1, 1, 1, 1], 3))
print(target_sum_way([1], 1))