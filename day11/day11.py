# Day 11: Monkey in the Middle

import re
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

class Monkey:
  def __init__(self, number, items, op_type, op_arg, div_arg, throw_true, throw_false):
    self.number = number
    self.orig_items = items.copy()
    self.op_type = op_type
    self.op_arg = op_arg
    self.div_arg = div_arg
    self.throw_true = throw_true
    self.throw_false = throw_false
    self.reset()    
  def reset(self):
    self.items = self.orig_items.copy()
    self.inspections = 0
  def do_turn(self, part):
    for item in self.items:
      self.inspections += 1
      # Apply operation
      if self.op_type == "sum":
        item += self.op_arg
      elif self.op_type == "mult":
        item *= self.op_arg
      elif self.op_type == "square":
        item = item ** 2
      # For Part 1, divide by 3 and round down
      if part == 1:
        item = item // 3
      # For Part 2, we take the number modulo m so it remains manageable
      elif part == 2:
        item = item % m
      # Determine to which monkey to throw the item
      if item % self.div_arg == 0:
        throw_to = self.throw_true
      else:
        throw_to = self.throw_false
      # Throw the item
      monkeys[throw_to].items.append(item)
    self.items = []

# Parse input
monkeys = []
m = 1
with open(sys.argv[1]) as f:

  while True:
    
    line = f.readline()
    if line == "": break
    
    number = int(re.match("Monkey ([0-9]+):", line).group(1))
    
    line = f.readline().strip()
    items = [int(x) for x in line.split(":")[1].split(",")]
    
    line = f.readline().strip()
    if "old * old" in line:
      op_type = "square"
      op_arg = None
    elif re.match(r"Operation: new = old \* ([0-9]+)", line):
      op_type = "mult"
      op_arg = int(re.search("Operation: new = old \* ([0-9]+)", line).group(1))
    elif re.match(r"Operation: new = old \+ ([0-9]+)", line):
      op_type = "sum"
      op_arg = int(re.search("Operation: new = old \+ ([0-9]+)", line).group(1))

    line = f.readline().strip()
    div_arg = int(re.search("Test: divisible by ([0-9]+)", line).group(1))
    m *= div_arg
    line = f.readline().strip()
    throw_true = int(re.search("throw to monkey ([0-9]+)", line).group(1))
    line = f.readline().strip()    
    throw_false = int(re.search("throw to monkey ([0-9]+)", line).group(1))
    
    monkeys.append(Monkey(number, items, op_type, op_arg, div_arg, throw_true, throw_false))
    
    f.readline()   

# ------------------------------------------------------------------------------
# Part 1

for r in range(20):
  for i in range(len(monkeys)):
    monkeys[i].do_turn(part=1)

insps = sorted([m.inspections for m in monkeys], reverse=True)
ans1 = insps[0] * insps[1]
print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

for monkey in monkeys:
  monkey.reset()

for r in range(10000):
  for i in range(len(monkeys)):
    monkeys[i].do_turn(part=2)

insps = sorted([m.inspections for m in monkeys], reverse=True)
ans2 = insps[0] * insps[1]
print("Part 2:", ans2)
