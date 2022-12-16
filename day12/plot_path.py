# Plots the solution of Day 12: Hill Climbing Algorithm

import sys
import random
from queue import Queue
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import numpy as np

# ==============================================================================

# Parse input
grid = []
with open("day12.in") as f:
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
  neighs = [(i+1, j), (i, j+1), (i, j-1), (i-1, j)]  
  children = []
  # for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
  # random.shuffle(neighs)
  # for ni, nj in neighs:
  for ni, nj in [(i+1, j), (i, j+1), (i, j-1), (i-1, j)]:
    if not (ni < 0 or ni > ny-1 or nj < 0 or nj > nx-1):
      if get_height(grid[ni][nj]) - get_height(grid[i][j]) <= 1:
        children.append((ni,nj))
  return children

# Performs breadth-first search to find a route from the start to the goal
def BFS(grid, start, goal):
  
  to_check = Queue()
  to_check.put((start, 0, []))
  seen = set([start])
  while not to_check.empty():

    pos, steps, path = to_check.get()

    if pos == goal:
      # print(f"Goal reached in {steps} steps")
      return pos, steps, path

    for child_pos in get_children(pos):
      if child_pos not in seen:
        to_check.put((child_pos, steps+1, path+[pos]))
        seen.add(child_pos)

# ------------------------------------------------------------------------------

heights = np.zeros(shape=(ny,nx))
for j in range(nx):
  for i in range(ny):
    heights[i,j] = get_height(grid[i][j])

pos, steps, path = BFS(grid, start, goal)

plt.figure(figsize=(20,5.2))
plt.imshow(heights, cmap="terrain")

ax = plt.gca()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="1%", pad=0.05) 
cb = plt.colorbar(cax=cax)
cb.set_label("Terrain elevation")

plt.sca(ax)

s = 20
plt.scatter([start[1]], [start[0]], color="lime", s=s, zorder=10)
plt.scatter([goal[1]], [goal[0]], color="red", s=s, zorder=10)

s = 4
ys, xs = zip(*(path+[goal]))
# plt.scatter(xs, ys, color="red", s=s)
plt.plot(xs, ys, color="red")

plt.tight_layout()

if "--save" in sys.argv:
  plt.savefig("path.png")
else:
  plt.show()


