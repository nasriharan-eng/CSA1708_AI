from collections import deque

jug1 = 4
jug2 = 3
target = 2

queue = deque([(0, 0)])
visited = set([(0, 0)])

while queue:
    a, b = queue.popleft()

    if a == target or b == target:
        print("Solution found:")
        print(a, b)
        break

    states = [
        (jug1, b),
        (a, jug2),
        (0, b),
        (a, 0),
        (a - min(a, jug2 - b), b + min(a, jug2 - b)),
        (a + min(b, jug1 - a), b - min(b, jug1 - a))
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append(state)
            print(state)
else:
    print("No solution")
