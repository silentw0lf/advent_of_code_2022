from collections import defaultdict
import re


def get_grid(nums):
    cor = []
    for lines in nums:
        new = []
        for i in range(0, len(lines), 2):
            new.append((int(lines[i]), int(lines[i+1])))
        cor.append(new)
    grid = defaultdict(lambda: ".")
    for line in cor:
        for i in range(len(line) - 1):
            x1, y1 = line[i][0], line[i][1]
            x2, y2 = line[i+1][0], line[i+1][1]
            if x1 == x2:
                for seq in range(min(y1, y2), max(y1, y2)+1):
                    np = (x1, seq)
                    if np not in grid:
                        grid[np] = "#"
            elif y1 == y2:
                for seq in range(min(x1, x2), max(x1, x2)+1):
                    np = (seq, y1)
                    if np not in grid:
                        grid[np] = "#"
    return grid


def solve(task):
    with open("input.txt") as f:
        nums = [re.findall("(-?\d+)", lines) for lines in f.readlines()]
        grid = get_grid(nums)

    stop_line = max(grid.keys(), key=lambda x: x[1])[1]
    if not task == 1:
        stop_line = stop_line + 2

    sand = 0
    while True:
        c, r = (500, 0)
        while True:
            if task == 1:
                if r > stop_line:
                    print(sand)
                    return
            else:
                if r + 1 == stop_line:
                    sand += 1
                    grid[(c, r)] = "o"
                    break
                if all(grid[(i, 1)] != "." for i in range(499, 502)):
                    print(sand + 1)
                    return

            if grid[(c, r+1)] == ".":
                r += 1
            elif grid[(c-1, r+1)] == ".":
                r += 1
                c -= 1
            elif grid[(c+1, r+1)] == ".":
                r += 1
                c += 1
            else:
                sand += 1
                grid[(c, r)] = "o"
                break


solve(task=1)
solve(task=2)
