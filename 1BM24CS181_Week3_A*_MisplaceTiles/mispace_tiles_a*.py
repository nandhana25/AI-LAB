import heapq

def h(state, goal):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

def astar(start, goal):
    OPEN = [(h(start, goal), 0, start)]
    CLOSED = set()
    g = {start: 0}
    parent = {start: None}

    while OPEN:
        f, cost, n = heapq.heappop(OPEN)

        if n in CLOSED:
            continue

        if n == goal:
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]
            path.reverse()

            for state in path:
                for i in range(0, 9, 3):
                    print(state[i:i+3])
                print()

            print("Number of moves:", len(path) - 1)
            return

        CLOSED.add(n)
        zero = n.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in [(-1, 0), (1, 0),
                       (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                j = nr * 3 + nc
                s = list(n)
                s[zero], s[j] = s[j], s[zero]
                s = tuple(s)
                new_g = g[n] + 1

                if new_g < g.get(s, float('inf')):
                    g[s] = new_g
                    parent[s] = n
                    heapq.heappush(
                        OPEN, (new_g + h(s, goal), new_g, s)
                    )
                    CLOSED.discard(s)

    print("No solution found.")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

astar(start, goal)
