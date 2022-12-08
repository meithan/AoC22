# Day 7: No Space Left On Device

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
lines = []
with open(sys.argv[1]) as f:
  for line in f:
    lines.append(line.strip("\n"))

class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.subdirs = []
    self.files = []
    self.size = None
  def get_subdir(self, name):
    for child in self.subdirs:
      if child.name == name:
        return child
    new_dir = Directory(name, self)
    self.subdirs.append(new_dir)
    return new_dir
  def add_subdir(self, name):
    if name not in [d.name for d in self.subdirs]:
      new_dir = Directory(name, self)
      self.subdirs.append(new_dir)
  def add_file(self, name, size):
    if name not in [f.name for f in self.files]:
      new_file = File(name, size)
      self.files.append(new_file)
  def get_size(self):
    if self.size is not None:
      return self.size
    size = 0
    for f in self.files:
      size += f.size
    for d in self.subdirs:
      d.size = d.get_size()
      size += d.size
    self.size = size
    return self.size

  def __eq__(self, other):
    return self.name == other.name and self.parent == other.parent
  def __repr__(self):
    return f"<Directory '{self.name}'>"

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size
  def __repr__(self):
    return f"<File '{self.name}'>"    

root = Directory("/", None)

current_dir = root
i = 0
while i < len(lines):

  tokens = lines[i].split()
  cmd = tokens[1].strip()

  if cmd == "cd":
    
    dir_name = tokens[2].strip()
    if dir_name == "/":
      current_dir = root
    elif dir_name == "..":
      current_dir = current_dir.parent
    else:
      current_dir = current_dir.get_subdir(dir_name)

    i += 1

  elif cmd == "ls":

    i += 1
    while i < len(lines) and not lines[i].startswith("$ "):
      tokens = lines[i].split()
      if tokens[0].strip() == "dir":
        current_dir.get_subdir(tokens[1])
      else:
        current_dir.add_file(tokens[1].strip(), int(tokens[0]))
      i += 1

# Recursively compute all directory sizes
root.get_size()

# ------------------------------------------------------------------------------
# Part 1

# Walk over the dir tree and add up dir sizes at most 100,000
ans1 = 0
to_check = [root]
while len(to_check) > 0:
  curdir = to_check.pop()
  if curdir.size <= 100_000:
    ans1 += curdir.size
  for d in curdir.subdirs:
    to_check.append(d)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

space_avail = 70000000
space_req = 30000000
space_used = root.get_size()
space_free = space_avail - space_used

# Walk over the dir tree and look for smallest dir that would free up enough space
best_dir = None
best_size = float("infinity")
to_check = [root]
while len(to_check) > 0:
  curdir = to_check.pop()
  if space_free + curdir.size >= space_req:
    if curdir.size < best_size:
      best_dir = curdir
      best_size = curdir.size
  for d in curdir.subdirs:
    to_check.append(d)

print(best_dir, best_size)

ans2 = best_size
print("Part 2:", ans2)
