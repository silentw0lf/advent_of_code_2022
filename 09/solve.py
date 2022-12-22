move_tail = {
    (2, 0): (1, 0), (0, 2): (0, 1), (-2, 0): (-1, 0), (0, -2): (0, -1),
    (2, 1): (1, 1), (1, 2): (1, 1), (-1, 2): (-1, 1), (-2, 1): (-1, 1),
    (-2, -1): (-1, -1), (-1, -2): (-1, -1), (1, -2): (1, -1), (2, -1): (1, -1),
    (2, 2): (1, 1), (-2, 2): (-1, 1), (-2, -2): (-1, -1), (2, -2): (1, -1)
}
move_head = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

def update_head(head, dir):
    inc = move_head[dir]
    head[0] += inc[0]
    head[1] += inc[1]

def update_tail(head, tail):
    distance = [head[0] - tail[0], head[1] - tail[1]]
    move = move_tail.get(tuple(distance), [0, 0])
    tail[0] += move[0]
    tail[1] += move[1]
    return move != [0, 0]


with open("input.txt") as f:
    content = [a.split() for a in f.readlines()]

# task 1
rope = [[0, 0], [0, 0]]
visited = set()
for dir, steps in content:
    i = 0
    while i < int(steps):
        i += 1
        update_head(rope[0], dir)
        update_tail(rope[0], rope[1])
        visited.add(tuple(rope[1]))

print(len(visited))

# task 2
rope = [[0, 0] for _ in range(10)]
visited = set()
for dir, steps in content:
    i = 0
    while i < int(steps):
        i += 1
        update_head(rope[0], dir)
        for rid in range(9):
            if not update_tail(rope[rid], rope[rid+1]):
                break
        visited.add(tuple(rope[9]))

print(len(visited))
