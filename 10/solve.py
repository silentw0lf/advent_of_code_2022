with open("input.txt") as f:
    commands = [a.split() for a in f.readlines()]

t_exec, val_exec = [], []
read_all = False
signal_strength, x, t = 0, 1, 1
sequence = ""

while (not read_all or t_exec):
    # begin
    if t < len(commands) + 1:
        instr_prev = commands[t-1]
        a = int(instr_prev[1]) if instr_prev[0] == "addx" else 0
        t_offset = 1 if instr_prev[0] == "addx" else 0
        t_exec.append(
            t + t_offset if not t_exec else t_exec[-1] + 1 + t_offset)
        val_exec.append(a)
    else:
        read_all = True

    draw = "#" if x <= t % 40 <= x + 2 else "."
    sequence += draw

    # during
    if t in [20, 60, 100, 140, 180, 220]:
        signal_strength += (x * t)

    # end
    if t_exec and t_exec[0] == t:
        x = x + val_exec[0]
        val_exec.pop(0)
        t_exec.pop(0)
    t += 1

# task 1
print(signal_strength)
# task 2
for i in range(0, len(sequence), 40):
    print(sequence[i:i+40])
