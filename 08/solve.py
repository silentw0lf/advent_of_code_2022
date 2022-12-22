
def get_column(grid, c):
    return [row[c] for row in grid]


def smaller(curr, numbers):
    return all(a < curr for a in numbers)


def get_score(r, c):
    curr_height = grid[r][c]

    # up
    i = 1
    score_up = 0
    while (r-i >= 0):
        score_up += 1
        if grid[r-i][c] >= curr_height:
            break
        i += 1

    # left
    i = 1
    score_left = 0
    while (c-i >= 0):
        score_left += 1
        if grid[r][c-i] >= curr_height:
            break
        i += 1

    # right
    i = 1
    score_right = 0
    while (c+i < len(grid[0])):
        score_right += 1
        if grid[r][c+i] >= curr_height:
            break
        i += 1

    # down
    i = 1
    score_down = 0
    while (r+i < len(grid)):
        score_down += 1
        if grid[r+i][c] >= curr_height:
            break
        i += 1

    return score_up * score_down * score_left * score_right


def is_visible(grid, r, c):
    curr_height = grid[r][c]
    if r == 0 or c == 0 or r == len(grid)-1 or c == len(grid[0])-1:
        return True

    col = get_column(grid, c)
    return any([
        smaller(curr_height, grid[r][c+1:]),
        smaller(curr_height, grid[r][0:c]),
        smaller(curr_height, col[0:r]),
        smaller(curr_height, col[r+1:])
    ])


with open("input.txt") as f:
    grid = [[int(a) for a in list(a.strip())] for a in f.readlines()]

visible = 0
highest_score = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if is_visible(grid, r, c):
            visible += 1
        curr_score = get_score(r, c)
        if curr_score > highest_score:
            highest_score = curr_score

print(visible)
print(highest_score)
