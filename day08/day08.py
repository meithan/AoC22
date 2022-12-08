# Day 8: Treetop Tree House

import sys
import functools

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
trees = []
with open(sys.argv[1]) as f:
  for line in f:
    trees.append([int(x) for x in list(line.strip())])

nx = len(trees)
ny = len(trees[0])

# ------------------------------------------------------------------------------
# Part 1

def is_visible(i, j):
  if i == 0 or i == nx-1 or j == 0 or j == ny-1:
    return True
  # Up
  if all([trees[k][j] < trees[i][j] for k in range(0, i)]):
    return True
  # Bottom
  if all([trees[k][j] < trees[i][j] for k in range(i+1, nx)]):
    return True
  # Left
  if all([trees[i][k] < trees[i][j] for k in range(0, j)]):
    return True
  # Right
  if all([trees[i][k] < trees[i][j] for k in range(j+1, ny)]):
    return True
  return False

ans1 = 0
for i in range(nx):
  for j in range(ny):
    # print(i, j, trees[i][j], is_visible(i, j))
    if is_visible(i, j):
      ans1 += 1

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

def scenic_score(i, j):
  scores = []
  # Up
  count = 0
  for k in range(i-1, -1, -1):
    count += 1
    if trees[k][j] >= trees[i][j]:
      break
  scores.append(count)    
  # Left
  count = 0
  for k in range(j-1, -1, -1):
    count += 1
    if trees[i][k] >= trees[i][j]:
      break
  scores.append(count)
  # Right
  count = 0
  for k in range(j+1, ny):
    count += 1
    if trees[i][k] >= trees[i][j]:
      break
  scores.append(count)
  # Down
  count = 0
  for k in range(i+1, nx):
    count += 1
    if trees[k][j] >= trees[i][j]:
      break
  scores.append(count)
  return functools.reduce(lambda x, y: x*y, scores, 1)

best_score = 0
for i in range(nx):
  for j in range(ny):
    score = scenic_score(i, j)
    if score > best_score:
      best_score = score

print("Part 2:", best_score)
