# Day 14:  Regolith Reservoir

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
lines = []
with open(sys.argv[1]) as f:
  for line in f:
    points = [(int(q[0]), int(q[1])) for q in [p.split(",") for p in line.strip().split(" -> ")]]
    lines.append(points)

# Create cave
xs = [point[0] for wall in lines for point in wall]
xmin, xmax = min(xs), max(xs)
ys = [point[1] for wall in lines for point in wall]
ymin, ymax = min(ys), max(ys)
# print(xmin, xmax, ymin, ymax)

xmin -= 10
xmax += 10

walls = set()
for wall in lines:
  for i in range(1,len(wall)):
    x1, y1 = wall[i-1]; x2, y2 = wall[i]
    # print(x1, y1, "to", x2, y2)
    if x1 == x2:
      for y in range(min(y1,y2), max(y1,y2)+1):
        walls.add((x1,y))
        # print(x1, y)
    elif y1 == y2:
      for x in range(min(x1,x2), max(x1,x2)+1):
        walls.add((x,y1))
        # print(x, y1)

def show_cave():
  for y in range(0, ymax+1+(1 if part == 2 else 0)):
    line = ""
    for x in range(xmin, xmax+1):
      if (x,y) in walls:
        line += "#"
      elif (x,y) in sand:
        line += "o"
      elif (x,y) == (500,0):
        line += "+"        
      else:
        line += "."
    print(line)
  if part == 2:
    print("#"*(xmax-xmin+1))
  print()

def is_wall(pos):
  if part == 1:
    return pos in walls
  elif part == 2:
    x, y = pos
    if pos in walls:
      return True
    elif y == ymax + 2:
      return True
    else:
      return False

def drop_at(pos):
  x, y = pos
  while True:
    for new_pos in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
      moved = False
      if not is_wall(new_pos) and new_pos not in sand:
        x, y = new_pos
        moved = True
        break
    if not moved:
      sand.add((x, y))
      return "stopped"
    if part == 1:
      if y > ymax:
        return "fell"

drop_pos = (500,0)

# ------------------------------------------------------------------------------
# Part 1

part = 1
sand = set()
# show_cave()

count = 0
while True:
  result = drop_at(drop_pos)
  if result == "fell":
    break
  count += 1
  # show_cave()
  # input()

# show_cave()

print("Part 1:", count)

# ------------------------------------------------------------------------------
# Part 2

part = 2
sand = set()
# show_cave()

count = 0
while True:
  drop_at(drop_pos)
  count += 1
  # show_cave()
  if drop_pos in sand:
    break
  # input()

print("Part 2:", count)
