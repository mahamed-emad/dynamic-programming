def climbing_stairs(n, memo={}):
    if n == 1: return 1
    if n == 2: return 2
    if n in memo: return memo[n]
    memo[n] = climbing_stairs(n - 1, memo) + climbing_stairs(n - 2, memo)
    return memo[n]

print(climbing_stairs(5))