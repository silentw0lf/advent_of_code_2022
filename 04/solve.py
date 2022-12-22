import re

with open("input.txt") as f:
    content = [a.strip() for a in f.readlines()]

# task 01
overl = 0
for line in content:
    r11, r12, r21, r22 = [int(n) for n in re.findall("(\d+)", line)]
    if r11 >= r21 and r12 <= r22 or r21 >= r11 and r22 <= r12:
        overl += 1
print(overl)

# taks 02
overl_at_all = 0
for line in content:
    r11, r12, r21, r22 = [int(n) for n in re.findall("(\d+)", line)]
    ol = range(max(r11, r21), min(r12, r22))
    if ol.stop >= ol.start:
        overl_at_all += 1
print(overl_at_all)
