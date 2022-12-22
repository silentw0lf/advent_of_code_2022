with open("input.txt") as f:
    line = f.readline()


def solve(nr_distinct: int):
    i = 0
    while i <= len(line) - nr_distinct:
        if len(set(line[i:i+nr_distinct])) == nr_distinct:
            print(i+nr_distinct)
            break
        i += 1


solve(nr_distinct=4)
solve(nr_distinct=14)
