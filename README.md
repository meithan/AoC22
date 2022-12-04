# AoC22
My solutions for Advent of Code 2022. In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

This year I'm not trying to solve the problems as soon as they open, so I won't be reporting solve times.

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4)

---

**Day 4**: [Camp Cleanup](https://adventofcode.com/2022/day/4)<a name="day3"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day04)

This is about overlapping 1D number ranges (integers, really, but works for reals too).

If `[a1,a2]` and `[b1,b2]` are two numbers ranges as defined by their endpoints (where we assume `a1 <= a2` and `b1 <= b2`), the ranges overlap if either endpoint of one is contained in the other, i.e. if `b1 <= a1 <= b2` or `b1 <= a2 <= b2` or `a1 <= b1 <= a2` or `a1 <= b2 <= a2`, and one range is entirely contained in another if both endpoints of the first are contained in the latter, which can be checked by `a1 >= b1 and a2 <= b2` or `b1 >= a1 and b2 <= a2`.

---

**Day 3**: [Rucksack Reorganization](https://adventofcode.com/2022/day/3)<a name="day3"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day03)

Python [sets](https://docs.python.org/3/library/stdtypes.html#set) make this problem really easy, specially as `&` acts as the intersection operator between them.

For Part 1 we split each string in half, convert the sub-strings into Python sets, and compute their intersection and check whether it is empty or not.

For Part 2, we check for non-empty set intersections for groups of three strings at a time.

The priorities are computed from the ASCII code (obtained with [`ord`](https://docs.python.org/3/library/functions.html#ord)) of each letter (a-z is 97 to 122 and A-Z is 65 to 90).

---

**Day 2**: [Rock Paper Scissors](https://adventofcode.com/2022/day/2)<a name="day2"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day02)

A simple "just code what the statement says" problem.

I found it a bit weird that they used 'A', 'B' and 'C' for 'rock', 'paper' and 'scissors' instead of something more natural like 'R', 'P' and 'S' (and I was forced to make the translation in the code, of course).

---

**Day 1**: [Calorie Counting](https://adventofcode.com/2022/day/1)<a name="day1"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day01)

And so it begins!

This is this year's warm-up, as usual. Python's list tools make the parts of this problem essentially one-liners.