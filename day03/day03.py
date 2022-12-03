# Day 03: Rucksack Reorganization

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
rucksacks = []
with open(sys.argv[1]) as f:
  for line in f:
    rucksacks.append(line.strip())

# ------------------------------------------------------------------------------
# Part 1

def priority(c):
  if 97 <= ord(c) <= 122:
    return 1 + ord(c) - 97
  elif 65 <= ord(c) <= 90:
    return 27 + ord(c) - 65

ans1 = 0
for sack in rucksacks:
  first = sack[:len(sack)//2]
  last = sack[len(sack)//2:]
  
  repeated = set(first) & set(last)
  r = list(repeated)[0]
  
  ans1 += priority(r)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

ans2 = 0
for i in range(0,len(rucksacks),3):
  repeated = set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])
  r = list(repeated)[0]
  ans2 += priority(r)

print("Part 2:", ans2)
