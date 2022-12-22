import re
from collections import defaultdict

def solve(task: int):
    d = defaultdict(list)
    for l in stacks.split("\n")[:-1]:
        i, bucket = 1, 1
        while i <= len(l):
            if l[i] != " ":
                d[bucket].insert(0, l[i])
            i += 4
            bucket += 1

    for com in commands.split("\n"):
        amount, src, dest = [int(a) for a in re.findall("(\d+)", com)]
        tmp = d[src][-amount:]
        if task == 1:
            tmp.reverse()
        d[dest].extend(tmp)
        del d[src][-amount:]

    word = ""
    for bucket in range(1, len(d)+1):
        word += d[bucket][-1]
    print(word)


with open("input.txt") as f:
    stacks, commands = f.read().split("\n\n")

solve(task=1)
solve(task=2)
