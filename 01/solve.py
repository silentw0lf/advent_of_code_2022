with open("input.txt") as f:
    content = f.read().split("\n\n")

results = []
for group in content:
    nums = [int(a) for a in group.split("\n")]
    results.append(sum(nums))

print(max(results))
print(sum(sorted(results)[-3:]))