with open("input.txt") as f:
    content = [a.strip() for a in f.readlines()]

# part 1
s = 0
for pack in content:
    split_idx = len(pack) // 2
    c1, c2 = pack[:split_idx], pack[split_idx:]
    ch = next(iter(set(c1).intersection(set(c2))))
    s += ord(ch)
    s = s - 96 if 97 <= ord(ch) <= 122 else s - 38
print(s)

# part 2
i, s = 0, 0
while i + 2 <= len(content):
    is12 = set(content[i]).intersection(set(content[i+1]))
    is123 = next(iter(set(is12).intersection(set(content[i+2]))))
    i += 3
    s += ord(is123)
    s = s - 96 if 97 <= ord(is123) <= 122 else s - 38
print(s)
