from z3 import *
import re

with open("input.txt") as f:
    equations = [l.split(": ") for l in f.readlines()]


def solve(task):
    s = Solver()
    vars = {equ[0]: Int(equ[0]) for equ in equations}
    wanted = 'root' if task == 1 else 'humn'

    for lhs, rhs in equations:
        if task == 2:
            if lhs == "root":
                o1, _, o2 = rhs.split()
                s.add(vars[o1] == vars[o2])
                continue
            if lhs == "humn":
                continue
        numb = re.findall("\d+", rhs)
        if numb:
            s.add(vars[lhs] == int(numb[0]))
        else:
            o1, op, o2 = rhs.split()
            match op:
                case "+":
                    s.add(vars[lhs] == vars[o1] + vars[o2])
                case "-":
                    s.add(vars[lhs] == vars[o1] - vars[o2])
                case "/":
                    s.add(vars[lhs] == vars[o1] / vars[o2])
                    s.add(vars[o1] % vars[o2] == 0)
                case "*":
                    s.add(vars[lhs] == vars[o1] * vars[o2])
    s.check()
    print(s.model().eval(vars[wanted]))


solve(task=1)
solve(task=2)
