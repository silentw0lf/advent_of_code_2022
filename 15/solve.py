# solution slow for part 2, takes around 45 seconds

import re


def manhattan_dist(xs, ys, xb, yb):
    return abs(xs - xb) + abs(ys - yb)

def merge_ranges(ranges):
    ranges.sort(key=lambda range: range[0])
    merged = [ranges[0]]
    for curr in ranges:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)
    return merged


with open("input.txt") as f:
    lines = f.readlines()
    lines = [[int(n) for n in re.findall("(-?\d+)", l)] for l in lines]


# taks 1
search_y = 2_000_000
circumfs = []
for xs, ys, xb, yb in lines:
    m = manhattan_dist(xs, ys, xb, yb)
    lr = (m - abs(search_y - ys))
    if lr < 0:
        continue

    x_min = xs - lr if xb != xs - lr else xs - lr + 1
    x_max = xs + lr if xb != xs + lr else xs + lr - 1
    circumfs.append([x_min, x_max])
ranges = merge_ranges([list(c) for c in circumfs])
print(sum((r[1]-r[0] + 1) for r in ranges))

# task 2
search_max = 4_000_000
for y in range(search_max + 1):
    circumfs = []
    for xs, ys, xb, yb in lines:
        m = manhattan_dist(xs, ys, xb, yb)
        lr = (m - abs(y - ys))
        if lr < 0:
            continue
        x_min = max(0, xs - lr)
        x_max = min(xs + lr, search_max)
        circumfs.append([x_min, x_max])

    ranges = merge_ranges([list(c) for c in circumfs])
    if len(ranges) == 2 and ranges[1][0] - ranges[0][1] == 2:
        x = ranges[0][1] + 1
        print(x * 4000000 + y)
        break

    # print(y)
    if len(ranges) == 1 and ranges[0] != [0, 4000000]:
        x = ranges[0][0] if ranges[0][0] > 0 else 4000000
        print(x * 4000000 + y)
        break
