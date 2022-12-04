# Day 04: Camp Cleanup

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
pairs = []
with open(sys.argv[1]) as f:
  for line in f:
    s1, s2 = line.strip().split(",")
    a1, a2 = (int(x) for x in s1.split("-"))
    b1, b2 = (int(x) for x in s2.split("-"))
    pairs.append(((a1,a2), (b1,b2)))

# ------------------------------------------------------------------------------
# Part 1

ans1 = 0
for (a1, a2), (b1, b2) in pairs:
  if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
    ans1 += 1

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

ans2 = 0
for (a1, a2), (b1, b2) in pairs:
  if (b1 <= a1 <= b2) or (b1 <= a2 <= b2) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2):
    ans2 += 1

print("Part 2:", ans2)
