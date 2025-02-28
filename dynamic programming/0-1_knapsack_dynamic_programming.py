def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)

    # Build a 2D DP ARRAY
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

max_value = knapsack_dynamic_programming(values, weights, capacity)
print(f"Max value is = {max_value}")