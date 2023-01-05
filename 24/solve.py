from math import lcm
from heapq import heappush, heappop

with open("input.txt") as f:
    grid = [list(row.strip()) for row in f.readlines()]

dirs_move = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (+1, 0)}
dirs_neighbor = list(dirs_move.values()) + [(0, 0)]
lrows, lcols = len(grid), len(grid[0])

def next_blizz_grid(curr_blizz_grid):
    blizz = set()
    for r, c, dir in curr_blizz_grid:
        m = dirs_move[dir]
        r_new, c_new = r + m[0], c + m[1]
        r_new = 1 if r_new == lrows-1 else r_new
        r_new = lrows - 2 if r_new == 0 else r_new
        c_new = 1 if c_new == lcols-1 else c_new
        c_new = lcols - 2 if c_new == 0 else c_new
        blizz.add((r_new, c_new, dir))
    return blizz

def get_neightbors(r, c, t):
    for dis_r, dis_c in dirs_neighbor:
        r1, c1 = r + dis_r, c + dis_c
        if 1 <= r1 < len(grid) - 1 and 1 <= c1 < len(grid[0]) - 1 or (r1, c1) in [start, end]:
            if (r1, c1) not in grids[t % states]:
                yield (r1, c1, t)

grids = []
states = lcm(lrows - 2, lcols-2)
curr_blizz_grid = set((r, c, grid[r][c]) for c in range(
    lcols) for r in range(lrows) if grid[r][c] not in ["#", "."])
for s in range(states + 1):
    curr_blizz_grid = next_blizz_grid(curr_blizz_grid)
    grids.append(set((t[0], t[1]) for t in curr_blizz_grid))

# Dijkstra for shortest path finding
def get_steps(start, end, t_start):
    visited = set()
    prio_queue = []
    heappush(prio_queue, (t_start, (start[0], start[1])))
    while True:
        if not prio_queue:
            break

        t, (r, c) = heappop(prio_queue)
        s = t % states
        if (r, c, s) not in visited:
            visited.add((r, c, s))
            if (r, c) == end:
                return t - t_start
            for rnew, cnew, t in get_neightbors(r, c, t):
                heappush(prio_queue, (t+1, (rnew, cnew)))

start, end = (0, 1), (lrows - 1, lcols - 2)
t = get_steps(start, end, 0)
print(t)
t += get_steps(end, start, t)
t += get_steps(start, end, t)
print(t)
