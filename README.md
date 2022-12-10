# AoC22
My solutions for Advent of Code 2022. In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

This year I'm not trying to solve the problems as soon as they open, so I won't be reporting solve times.

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4) [5](#day5) [6](#day6) [7](#day7) [8](#day8) [9](#day9)

---

**Day 9**: [Rope Bridge](https://adventofcode.com/2022/day/9)<a name="day9"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day09)

A fun little problem that is mostly just about careful coding. I initially solved Part 1 by only considering the head and the one tail. Then for Part 2 I generalized the code so it could handle arbitrary-length ropes. Worked well. The only difference between the solutions of the two parts is the length of the rope.

---

**Day 8**: [Treetop Tree House](https://adventofcode.com/2022/day/8)<a name="day8"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day08)

A problem solvable by brute force, in this case by independently computing visibility or "scenic score" for every single tree. If the grid is N by N, this requires N^2 * 2N = O(N^3) operations, so it's not very efficient. But the problem input is small enough that both parts take a couple hundred milliseconds in Python.

I used a couple of Pythonic syntax tools to make the code more elegant (albeit not more efficient). In Part 1 I used the [`all`](https://docs.python.org/3/library/functions.html#all) built-in function to check, almost literally, whether all trees in a given direction are shorted than the tree in question. In Part 2 I used [`functools.reduce`](https://docs.python.org/3/library/functools.html#functools.reduce) to compute the product of the distances in a single instruction.

For fun I made a couple of plots from the data in my input. The first is the height distribution of the trees:

![](https://github.com/meithan/AoC22/blob/main/day08/heights.png)

we clearly see that it's not uniform, as the trees get taller the closer to the center.

The second plot shows the maximum distance from each tree to the edges, i.e. how far it can see. In black are those that can't see the edge in any direction.

![](https://github.com/meithan/AoC22/blob/main/day08/distance.png)

---

**Day 7**: [No Space Left On Device](https://adventofcode.com/2022/day/7)<a name="day7"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day07)

A fun little problem of recreating a simple filesystem-like directory structure.

I created two classes: a `File` which has a name and a size, and a `Directory` which has a name, a parent directory (another `Directory`, or `None` for the root directory), a list of subdirectories it contains (other `Directory` objects), a list of files it contains (`File` objects), and functions to get/add subdirs and to add files to it. It also contains a function to compute its size, which is achieved by adding the sizes of the files it contains plus the sizes of the subdirs it contains, in turn computed recursively.

Another good chunk of the code is parsing the input: separating the `cd` and `ls` commands, and building the directory tree structure as all the lines are parsed. We essentially simulate the process indicated by the commands, and add new entries (dirs or files) as they're encountered. After all lines are parsed, we compute the size of the root directory, which recursively computes the sizes of all dirs in the tree.

After that's done, Part 1 is solved by simply walking over the directory tree and adding up the relevent sizes: a `to_check` list contains only the root directory initially, and as long as this list is not empty we (1) pop one element from the list, (2) add its subdirs to the list, (3) if its size is not more than 100,000, we add it up into the total.

For Part 2, we do a similar walk of the tree and look for the smallest directory that frees up enough space on removal.

---

**Day 6**: [Tuning Trouble](https://adventofcode.com/2022/day/6)<a name="day6"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day06)

Another problem where Python's rich syntax and tools shine. Extracting four consecutive items from a list or string is trivial with slicing: `datastream[i-4:i]`. Then, determining how many of them are distinct is easily accomplished by putting these items in a set and checking the size of the resulting set: `len(set(datastream[i-4:i]))` -- sets automatically weed out duplicates.

Then repeat for Part 2, with 14 instead of 4.

---

**Day 5**: [Supply Stacks](https://adventofcode.com/2022/day/5)<a name="day5"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day05)

A problem with [stacks](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)), which Python lists are [can be used as](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks). The majority of the solving time was spent writing code to parse the information in the input. Each stack becomes a list, with the first element being the bottom crate and the last element the top crate.

After parsing the input, it was only a matter of executing the instructions. For Part 1, we pop crates one at a time from the source stack and immediately append them to the destination stack. In Part 2, we first pop all the crates from the source stack and save them in a temporary list, reverse the list, then append the reversed list them to the destination stack (using `extend` instead of `append` saves a `for` loop).

I used [copy.deepcopy](https://docs.python.org/3/library/copy.html) to save a copy of the initial configuration of the stacks and then recover it for Part 2.

---

**Day 4**: [Camp Cleanup](https://adventofcode.com/2022/day/4)<a name="day4"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day04)

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