from collections import deque

# State = (missionaries_left, cannibals_left, boat_side)

start = (3, 3, 0)
goal = (0, 0, 1)

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s)
        break

    if boat == 0:
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    else:
        moves = [(-1,0), (-2,0), (0,-1), (0,-2), (-1,-1)]

    for dm, dc in moves:
        nm = m - dm
        nc = c - dc

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            left_safe = nm == 0 or nm >= nc
            right_m = 3 - nm
            right_c = 3 - nc
            right_safe = right_m == 0 or right_m >= right_c

            if left_safe and right_safe:
                new_boat = 1 - boat
                new_state = (nm, nc, new_boat)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))
else:
    print("No solution")
