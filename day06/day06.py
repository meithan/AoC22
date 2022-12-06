# Day 06: Tuning Trouble

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
with open(sys.argv[1]) as f:
  datastream = f.read().strip()

# ------------------------------------------------------------------------------
# Part 1

for i in range(4,len(datastream)):
  if len(set(datastream[i-4:i])) == 4:
    ans1 = i
    break

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

for i in range(14,len(datastream)):
  if len(set(datastream[i-14:i])) == 14:
    ans2 = i
    break

print("Part 2:", ans2)
