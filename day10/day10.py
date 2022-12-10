# Day 10: Cathode-Ray Tube

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
program = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = line.strip().split()
    cmd = tokens[0]  
    arg = int(tokens[1]) if len(tokens) > 1 else None
    program.append((cmd, arg))

# ------------------------------------------------------------------------------
# Part 1

checkpoints = [20, 60, 100, 140, 180, 220]
signal_strength = 0
X = 1
cycle = 1

for cmd, arg in program:
  
  if cmd == "noop":
  
    if cycle in checkpoints:
      print(cycle, X)
      signal_strength += cycle*X
    cycle += 1
  
  elif cmd == "addx":
  
    for _ in range(2):
      if cycle in checkpoints:
        print(cycle, X)
        signal_strength += cycle*X
      cycle += 1
    X += arg

print("Part 1:", signal_strength)

# ------------------------------------------------------------------------------
# Part 2

idx = 0
cmd = None
arg = None
remain = None
X = 1

rows = [[] for _ in range(6)]
for cycle in range(240):

  r = cycle // 40
  c = cycle % 40

  if abs(c-X) <= 1:
    rows[r].append("#")
  else:
    rows[r].append(".")

  if cmd is None:
    cmd, arg = program[idx]
    remain = 2 if cmd == "addx" else 1
    idx += 1

  if cmd == "noop":
    pass
  
  elif cmd == "addx":
    if remain == 1:
      X += arg

  remain -= 1
  if remain == 0:
    cmd = None

for row in rows:
  print("".join(row))

ans2 = "FGCUZREC"

print("Part 2:", ans2)
