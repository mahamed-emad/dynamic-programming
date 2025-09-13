def max_product(nums):
    MAX = max_i = min_i = nums[0]
    for i in range(1, len(nums)):
        temp_max = max_i
        max_i = max(nums[i], nums[i] * temp_max, nums[i] * min_i)
        min_i = min(nums[i], nums[i] * temp_max, nums[i] * min_i)
        MAX = max(MAX, max_i)
    return MAX

print(max_product([2, 3, -2, 4]))
print(max_product([2, 3, -2, -4]))