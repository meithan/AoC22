# Day 12: Hill Climbing Algorithm

import sys
from queue import Queue

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
grid = []
with open(sys.argv[1]) as f:
  for line in f:
    grid.append(line.strip())

nx = len(grid[0])
ny = len(grid)

start = None
goal = None
for j in range(nx):
  for i in range(ny):
    if grid[i][j] == "S":
      start = (i,j)
    elif grid[i][j] == "E":
      goal = (i,j)

# Return the height of a grid point, given its letter
def get_height(c):
  if c == "S":
    return 0
  elif c == "E":
    return 25
  else:
    return ord(c) - 97

# Returns the accessible neighboring points from the given position
def get_children(pos):
  i, j = pos
  children = []
  for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
    if not (ni < 0 or ni > ny-1 or nj < 0 or nj > nx-1):
      if get_height(grid[ni][nj]) - get_height(grid[i][j]) <= 1:
        children.append((ni,nj))
  return children

# Performs breadth-first search to find a route from the start to the goal
def BFS(grid, start, goal):
  
  to_check = Queue()
  to_check.put((start, 0))
  seen = set([start])
  while not to_check.empty():

    pos, steps = to_check.get()

    if pos == goal:
      # print(f"Goal reached in {steps} steps")
      return steps

    for child_pos in get_children(pos):
      if child_pos not in seen:
        to_check.put((child_pos, steps+1))
        seen.add(child_pos)

# ------------------------------------------------------------------------------
# Part 1

ans1 = BFS(grid, start, goal)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

# Search for all starting positions of height 'a' (or zero)
candidates = []
for j in range(nx):
  for i in range(ny):
    if get_height(grid[i][j]) == 0:
      candidates.append((i,j))

# Compute steps of shortest route for reach candidate and find best
min_steps = float("inf")
for i,j in candidates:
  steps = BFS(grid, (i,j), goal)
  if steps is None: continue
  if steps < min_steps:
    min_steps = steps
    best = (i,j)

print("Part 2:", min_steps)
