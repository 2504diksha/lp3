##python Program
def knapsack(weights, values, capacity):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    included_items = []
    total_weight = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            total_weight += weights[i - 1]
            w -= weights[i - 1]

    included_items.reverse()

    return dp[n][capacity], total_weight, included_items

n = int(input("Enter number of items: "))
weights = []
values = []

print("\nEnter weight and value for each item:")
for i in range(n):
    w = int(input(f"Weight of item {i + 1}: "))
    v = int(input(f"Value of item {i + 1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("\nEnter capacity of the knapsack: "))

max_value, total_weight, items_included = knapsack(weights, values, capacity)

print(f"\nMaximum value (profit) that can be put in knapsack = {max_value}")
print(f"Total weight used = {total_weight}")

if items_included:
    print("\nItems included :")
    for i in items_included:
        print(f"  Item {i + 1}: Weight = {weights[i]}, Value = {values[i]}")
else:
    print("No items can be included.")
