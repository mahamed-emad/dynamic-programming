def knapsack(w, weights, values, i=0, memo=None):
    if memo is None: memo = {}
    key = (w, i)
    if key in memo: return memo[key]
    if w == 0 or i == len(weights): return 0
    if w >= weights[i]:
        take = values[i] + knapsack(w - weights[i], weights, values, i + 1, memo)
    else: take = 0
    leave = knapsack(w, weights, values, i + 1, memo)
    memo[key] = max(take, leave)
    return memo[key]