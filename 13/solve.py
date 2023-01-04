from ast import literal_eval
from functools import cmp_to_key

with open("input.txt") as f:
    content = [tuple(map(literal_eval, x)) for x in [a.split() for a in f.read().split("\n\n")]]

def com(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return com(p1, p2)

    p1 = [p1] if isinstance(p1, int) else p1
    p2 = [p2] if isinstance(p2, int) else p2
    l1, l2 = len(p1), len(p2)
    lmin = min(l1, l2)

    for i in range(lmin):
        res = compare(p1[i], p2[i])
        if res == -1:
            return -1
        elif res == 1:
            return 1

    return com(l1, l2)

# task 1
print(sum(idx for idx, (p1, p2) in enumerate(content, start=1) if compare(p1, p2) == 1))

# task 2
all = [[[2]], [[6]]]
for t in content:
    all.extend(t)
all = sorted(all, key=cmp_to_key(compare), reverse=True)
print((all.index([[2]]) + 1) * (all.index([[6]]) + 1))
