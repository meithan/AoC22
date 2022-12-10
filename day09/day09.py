# Day 9: Rope Bridge

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
movements = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = line.strip().split()
    movements.append((tokens[0], int(tokens[1])))

incs = {
  "U": (0, +1), "D": (0, -1), "L": (-1, 0), "R": (+1, 0)
}

def update_tail(x, y):
  for s in range(1,rope_len):
    x1, y1 = x[s-1], y[s-1]
    x2, y2 = x[s], y[s]
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
      return
    if y1 == y2:
      if x1 > x2:
        x[s] += 1
      elif x1 < x2:
        x[s] -= 1
    elif x1 == x2:
      if y1 > y2:
        y[s] += 1
      elif y1 < y2:
        y[s] -= 1
    else:
      if x1 > x2 and y1 > y2:
        x[s] += 1; y[s] += 1
      elif x1 > x2 and y1 < y2:
        x[s] += 1; y[s] -= 1
      elif x1 < x2 and y1 > y2:
        x[s] -= 1; y[s] += 1
      elif x1 < x2 and y1 < y2:
        x[s] -= 1; y[s] -= 1

def show():
  print()
  for j in range(10, -11, -1):
    row = ""
    for i in range(-10, 11):
      c = "."
      if (i, j) == (x[0], y[0]):
        c = "H"
      elif rope_len == 2 and (i, j) == (x[-1], y[-1]):
        c = "T"
      else:
        for s in range(1,len(x)):
          if (i, j) == (x[s], y[s]):
            c = str(s)
            break
      if c == "." and (i,j) == (0,0):
        c = "s"
      row += c
    print(row)

def simulate_motion():
  
  x = [0 for _ in range(rope_len)]
  y = [0 for _ in range(rope_len)]

  visited = set()
  for direc, steps in movements:
    dx, dy = incs[direc]
    for i in range(steps):
      x[0] += dx; y[0] += dy
      update_tail(x, y)
      visited.add((x[-1], y[-1]))
  
  return visited

# ------------------------------------------------------------------------------
# Part 1

rope_len = 2
visited = simulate_motion()

print("Part 1:", len(visited))

# ------------------------------------------------------------------------------
# Part 2

rope_len = 10
visited = simulate_motion()

print("Part 2:", len(visited))
