# Day 05: Supply Stacks

from copy import deepcopy
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
num_stacks = None
instructions = []
with open(sys.argv[1]) as f:
  for line in f:
    if line == "\n":
      continue
    if num_stacks is None:
      num_stacks = (len(line.strip('\n')) + 1) // 4
      stacks = [[] for _ in range(num_stacks)]
    if line[1] == "1":
      continue
    if line.startswith("[") or line.startswith(" "):
      for i in range(num_stacks):
        l = line[1+4*i]
        if l != " ":
          stacks[i].append(l)
    if line.startswith("move"):
      tokens = line.strip().split()
      instructions.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))
    
for j in range(num_stacks):
  stacks[j] = list(reversed(stacks[j]))

orig_stacks = deepcopy(stacks)

# print(stacks)
# print(instructions)

# ------------------------------------------------------------------------------
# Part 1

def exec_instruction_9000(instruction):
  qty, src, dest = instruction
  for _ in range(qty):
    item = stacks[src-1].pop()
    stacks[dest-1].append(item)

def print_stacks():
  for i in range(num_stacks):
    print(i+1, " ".join(stacks[i]))

stacks = deepcopy(orig_stacks)
for instruction in instructions:
  exec_instruction_9000(instruction)

ans1 = "".join([s[-1] for s in stacks])

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

def exec_instruction_9001(instruction):
  qty, src, dest = instruction
  crates = []
  for _ in range(qty):
    crates.append(stacks[src-1].pop())
  stacks[dest-1].extend(reversed(crates))

stacks = deepcopy(orig_stacks)
for instruction in instructions:
  exec_instruction_9001(instruction)

ans2 = "".join([s[-1] for s in stacks])

print("Part 2:", ans2)
