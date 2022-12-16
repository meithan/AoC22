# Day 13: Distress Signal

import sys
import functools

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
pairs = []
with open(sys.argv[1]) as f:
  cur_pair = []
  for line in f:
    if line.strip() == "": continue
    cur_pair.append(eval(line.strip()))
    if len(cur_pair) == 2:
      pairs.append(cur_pair)
      cur_pair = []

# Compares two packets. Returns:
# -1 if left is "less" than right (i.e they are ordered),
#  1 if right is "less" than left (i.e they are not ordered),
#  0 if they are "equal" (i.e. couldn't decide)
def compare(left, right):
  i = 0
  while True:
    
    # One of the list has run out of items
    if i == len(left) and i < len(right):
      return -1
    elif i < len(left) and i == len(right):
      return 1
    elif i == len(left) and i == len(right):
      return 0

    # Two integers
    if type(left[i]) is int and type(right[i]) is int:
      if left[i] < right[i]:
        return -1
      elif left[i] > right[i]:
        return 1
    
    # Two lists
    if type(left[i]) is list and type(right[i]) is list:
      result = compare(left[i], right[i])
      if result != 0:
        return result
    
    # Mixed types
    if type(left[i]) is int and type(right[i]) is list:
      result = compare([left[i]], right[i])
      if result != 0:
        return result
    elif type(left[i]) is list and type(right[i]) is int:
      result = compare(left[i], [right[i]])
      if result != 0:
        return result      

    i += 1
  
  return 0


# ------------------------------------------------------------------------------
# Part 1

# Determine which pairs are in order
ans1 = 0
for i, (left, right) in enumerate(pairs):
  result = compare(left, right)
  if result == -1:
    ans1 += (i+1)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

# Collect packets in a single big list
packets = []
for p1, p2 in pairs:
  packets.append(p1)
  packets.append(p2)

# Add divider packets
divider_packets = [[[2]], [[6]]]
for p in divider_packets:
  packets.append(p)

# Sort packets
packets_sorted = sorted(packets, key=functools.cmp_to_key(compare))
ans2 = 1
for i,p in enumerate(packets_sorted):
  if p in divider_packets:
    ans2 *= (i+1)

print("Part 2:", ans2)
