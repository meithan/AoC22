# Day 02: Rock Paper Scissors

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
rounds = []
with open(sys.argv[1]) as f:
  for line in f:
    rounds.append(tuple(line.strip().split(" ")))

decoded = {
  "A": "R", "B": "P", "C": "S",
  "X": "R", "Y": "P", "Z": "S"
}

points = {
  "R": 1, "P": 2, "S": 3
}

def resolve_round(play1, play2):
  if (play1, play2) == ("R", "S") or (play1, play2) == ("P", "R") or (play1, play2) == ("S", "P"):
    return "win"
  elif (play2, play1) == ("R", "S") or (play2, play1) == ("P", "R") or (play2, play1) == ("S", "P"):
    return "lose"
  else:
    return "draw"

def calc_round_score(opp_play, own_play):
  score = points[own_play]
  result = resolve_round(own_play, opp_play)
  if result == "win":
    score += 6
  elif result == "draw":
    score += 3
  elif result == "lose":
    pass
  return score

def determine_play(opp_play, strategy):
  if strategy == "X":  # need to lose
    if opp_play == "R": return "S"
    elif opp_play == "P": return "R"
    elif opp_play == "S": return "P"
  elif strategy == "Y":  # need to draw:
    return opp_play
  elif strategy == "Z":  # need to win
    if opp_play == "R": return "P"
    elif opp_play == "P": return "S"
    elif opp_play == "S": return "R"

# ------------------------------------------------------------------------------
# Part 1

tot_score = 0
for opp_str, own_str in rounds:
  opp_play = decoded[opp_str]
  own_play = decoded[own_str]
  tot_score += calc_round_score(opp_play, own_play)

print("Part 1:", tot_score)

# ------------------------------------------------------------------------------
# Part 2

tot_score = 0
for opp_str, own_str in rounds:
  opp_play = decoded[opp_str]
  strategy = own_str
  own_play = determine_play(opp_play, strategy)
  tot_score += calc_round_score(opp_play, own_play)

print("Part 2:", tot_score)

