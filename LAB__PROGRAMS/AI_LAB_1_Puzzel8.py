from collections import deque

start = tuple(map(int, input("Enter 9 numbers: ").split()))
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([start])
visited = {start}
parent = {start: None}

while queue:
    state = queue.popleft()

    if state == goal:
        print("\nPuzzle Solved!")
        break

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for r, c in moves:
        new_row = row + r
        new_col = col + c

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = state
                queue.append(new_state)

else:
    print("No solution")

# Print final state
print("\nFinal State:")
for i in range(0, 9, 3):
    print(goal[i], goal[i+1], goal[i+2])
