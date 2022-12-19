# Day 15: Beacon Exclusion Zone

import sys
import re

import matplotlib.pyplot as plt

# ==============================================================================

fname = "day15.test"
# fname = "day15.in"

# Parse input
regex = re.compile("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)")
sensors = []
with open(fname) as f:
  for line in f:
    xs, ys, xb, yb = [int(_) for _ in regex.findall(line.strip())[0]]
    sensors.append((xs, ys, xb, yb))

def manh_dist(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)

# ------------------------------------------------------------------------------

plt.figure(figsize=(8,8))

for xs, ys, xb, yb in sensors:

  d = manh_dist(xs, ys, xb, yb)
  xx = (xs, xs+d, xs, xs-d, xs)
  yy = (ys+d, ys, ys-d, ys, ys+d)

  plt.plot(xx, yy, color="C0")
  plt.fill(xx, yy, color="C0", alpha=0.1)

  plt.scatter([xs], [ys], color="C0", s=20, zorder=10)
  plt.scatter([xb], [yb], color="k", s=20, zorder=10)

m = 20 if fname == "day15.test" else 4e6
plt.plot([0, m, m, 0, 0], [0, 0, m, m, 0], color="C1")

if m == 20:
  xx = []; yy = []
  for i in range(m+1):
    for j in range(m+1):
      if (i, j) != (14, 11):
        xx.append(i)
        yy.append(j)
  plt.scatter(xx, yy, marker=".", color="k", s=5)

(xsol, ysol) = (14, 11) if fname == "day15.test" else (3138881, 3364986)
plt.scatter([xsol], [ysol], marker=".", color="red", s=100, zorder=10)

plt.gca().set_aspect("equal")
plt.tight_layout()

plt.savefig("plot.png")
plt.show()