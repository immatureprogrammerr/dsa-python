def knapsack_greedy(values, weight, capacity):
    items = [(values[i], weights[i], (values[i]/weight[i])) for i in range(len(values))]

    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0

    for value, weight, ratio in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break
    return total_value

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    max_value = knapsack_greedy(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value:.2f}")
