points_by_gesture = {"X": 1, "Y": 2, "Z": 3}
points_by_setup = {("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0, ("B", "X"): 0,
             ("B", "Y"): 3, ("B", "Z"): 6, ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}
my_gesture = {
    "X":  {"A": "Z",  "B": "X", "C": "Y"},  # loose
    "Z": {"A": "Y",  "B": "Z", "C": "X"},  # win
    "Y": {"A": "X",  "B": "Y", "C": "Z"},  # draw
}

with open("input.txt") as f:
    content = [a.split() for a in f.readlines()]

# task 01
points = 0
for opp, me in content:
    points += points_by_gesture[me]
    points += points_by_setup[(opp, me)]
print(points)

# task 02
points = 0
for opp, outcome in content:
    me = my_gesture[outcome][opp]
    points += points_by_gesture[me]
    points += points_by_setup[(opp, me)]
print(points)
