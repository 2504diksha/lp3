## Python Program
def knapsack(values, weights, capacity, n):
    # DP table initialization
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: Include the item
                # Option 2: Exclude the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp


# ---------------- Main Program ----------------
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter capacity of Knapsack: "))

max_value, dp_table = knapsack(values, weights, capacity, n)

print("\nDP Table:")
for row in dp_table:
    print(row)

print(f"\nMaximum value that can be obtained = {max_value}")
