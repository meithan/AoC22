# Day 01: Calorie Counting

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
elves = []
with open(sys.argv[1]) as f:
  cur_elf = []
  for line in f:
    if line.strip() == "":
        elves.append(cur_elf)
        cur_elf = []
    else:
        cur_elf.append(int(line))

# ------------------------------------------------------------------------------
# Part 1

totals = [sum(elf) for elf in elves]

print("Part 1:", max(totals))

# ------------------------------------------------------------------------------
# Part 2

totals.sort(reverse=True)

print("Part 2:", sum(totals[:3]))