
elves = []
with open("day1.in") as f:
  cur_elf = []
  for line in f:
    if line.strip() == "":
        elves.append(cur_elf)
        cur_elf = []
    else:
        cur_elf.append(int(line))

totals = [sum(elf) for elf in elves]

print(max(totals))

totals.sort(reverse=True)

print(sum(totals[:3]))