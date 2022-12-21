from math import floor
import re

with open("input.txt") as f:
    info_blocks = f.read().split("\n\n")


def solve(task):
    monkeys = dict()
    for monkey in info_blocks:
        l = monkey.split("\n")
        id = int(re.findall("(\d+)", l[0])[0])
        monkeys[id] = dict()
        monkeys[id]["wlvls"] = [int(a) for a in re.findall("(\d+)", l[1])]
        operation, operand = re.findall("(\+|\*)\s(old|\d+)", l[2])[0]
        monkeys[id]["opn"] = operation
        monkeys[id]["op2"] = operand
        monkeys[id]["div_by"] = int(re.findall("(\d+)", l[3])[0])
        monkeys[id]["true_id"] = int(re.findall("(\d+)", l[4])[0])
        monkeys[id]["false_id"] = int(re.findall("(\d+)", l[5])[0])
        monkeys[id]["insp"] = 0

    mod_all = 1
    for div_by in [m["div_by"] for m in monkeys.values()]:
        mod_all *= div_by

    r = 0
    rounds = 20 if task == 1 else 10000
    while r < rounds:
        for id, m in monkeys.items():
            while (monkeys[id]["wlvls"]):
                item_worry = monkeys[id]["wlvls"].pop(0)
                monkeys[id]["insp"] += 1
                match m["opn"]:
                    case '*':
                        op2 = item_worry if m["op2"] == "old" else int(
                            m["op2"])
                        item_worry *= op2
                    case '+':
                        item_worry += int(m["op2"])

                if task == 1:
                    item_worry = floor((item_worry / 3))
                else:
                    item_worry = item_worry % mod_all

                if item_worry % m["div_by"] == 0:
                    monkeys[m["true_id"]]["wlvls"].append(item_worry)
                else:
                    monkeys[m["false_id"]]["wlvls"].append(item_worry)
        r += 1

    insps = sorted([m['insp'] for m in monkeys.values()])
    print(insps[-1] * insps[-2])


solve(task=1)
solve(task=2)
