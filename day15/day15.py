# Day 15: Beacon Exclusion Zone

import sys
import re

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  input_fname = sys.argv[0].replace(".py", ".in")
else:
  input_fname = sys.argv[1]

# Parse input
regex = re.compile("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)")
sensors = []
with open(input_fname) as f:
  for line in f:
    xs, ys, xb, yb = [int(_) for _ in regex.findall(line.strip())[0]]
    sensors.append((xs, ys, xb, yb))

def manh_dist(x1, y1, x2, y2):
  return abs(x1-x2) + abs(y1-y2)

def merge_pair(interv1, interv2):
  if interv1[0] <= interv2[0]:
    a1, a2 = interv1
    b1, b2 = interv2
  else:
    a1, a2 = interv2
    b1, b2 = interv1
  if b1 - a2 > 1:
    return None
  else:
    return (a1, max(a2, b2))

def reduce_intervals(intervals):
  intervs = [_ for _ in intervals]
  intervs.sort(key=lambda x: x[0])
  while True:
    success = True
    N = len(intervs)
    for i in range(N-1):
      merged = merge_pair(intervs[i], intervs[i+1])
      if merged is not None:
        intervs = intervs[:i] + [merged] + intervs[i+2:]
        success = False
        break
    if success: return intervs

def intervals_at_y(targety):
  intervals = []
  for xs, ys, xb, yb in sensors:
    db = manh_dist(xs, ys, xb, yb)
    dy = abs(ys-targety)
    if dy <= db:
      xc, yc = xs, targety
      r = abs(db - dy)
      x1 = xc - r
      x2 = xc + r
      # if x1 == xb: x1 += 1
      # if x2 == xb: x2 -= 1
      if x1 <= x2:
        intervals.append((x1,x2))
  return reduce_intervals(intervals)

# ------------------------------------------------------------------------------
# Part 1

targety = 10 if input_fname == "day15.test" else 2_000_000

intervals = intervals_at_y(targety)
ans1 = 0
for a,b in intervals:
  ans1 += b - a    # this assumes a single beacon in the row

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

maxy = 20 if input_fname == "day15.test" else 4_000_000

for targety in range(0, maxy+1):
  intervals = intervals_at_y(targety)
  if len(intervals) > 1:
    x = intervals[0][1] + 1
    y = targety
    tuning_freq = x * 4_000_000 +  y
    # print(intervals, x, y)
    break

print("Part 2:", tuning_freq)
