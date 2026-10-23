
from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
best_cost = float('inf')
best_path = None

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    total = sum(cost[path[i]][path[i+1]]
                for i in range(n))

    if total < best_cost:
        best_cost = total
        best_path = path

print("Best tour:", " -> ".join(
    chr(65 + i) for i in best_path))
print("Minimum cost:", best_cost)
