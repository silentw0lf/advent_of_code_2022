from heapq import heappush, heappop

with open("input.txt") as f:
    grid = [list(row.strip()) for row in f.readlines()]


def get_neightbors(r, c):
    h = get_height(r, c)
    neighbors = []
    for dis_r, dis_c in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        r1, c1 = r + dis_r, c + dis_c
        if r1 >= 0 and r1 < len(grid) and c1 >= 0 and c1 < len(grid[0]):
            if get_height(r1, c1) <= h + 1:
                neighbors.append((r1, c1))
    return neighbors


def get_height(r, c):
    s = grid[r][c]
    if s == "S":
        return 0
    if s == "E":
        return 25
    return ord(s) - 97


def get_steps(start, end):
    visited = set()
    prio_queue = []
    heappush(prio_queue, (0, start))

    # Dijkstra for shortest path finding
    while True:
        if not prio_queue:
            break

        steps, node = heappop(prio_queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return steps
            for rnew, cnew in get_neightbors(node[0], node[1]):
                heappush(prio_queue, (steps+1, (rnew, cnew)))


# get start(s) + end
starts = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start_fix = (r, c)
            starts.append((r, c))
        if grid[r][c] == "E":
            end = (r, c)
        if grid[r][c] == "a":
            starts.append((r, c))


# task 1
print(get_steps(start_fix, end))

# taks 2
steps_all = []
for start in starts:
    steps = get_steps(start, end)
    if steps is not None:
        steps_all.append(steps)

print(min(steps_all))
