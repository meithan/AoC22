# AoC22
My solutions for Advent of Code 2022. In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

This year I'm not trying to solve the problems as soon as they open, so I won't be reporting solve times.

Go to day: [1](#day1) [2](#day2) [3](#day3) [4](#day4) [5](#day5) [6](#day6) [7](#day7) [8](#day8) [9](#day9) [10](#day10) [11](#day11) [12](#day12) [13](#day13) [14](#day14)

---

**Day 14**: [Regolith Reservoir](https://adventofcode.com/2022/day/14)<a name="day14"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day14)

A variation of [Day 17, 2018](https://adventofcode.com/2018/day/17) with sand instead of water and different propagation rules.

At first I was undecided if I wanted to allocate a big enough 2D array to store all positions, including empty spaces, which makes checking any position O(1), or to use sets storing only the actual walls and the sand that has been dropped, making checks O(log n) but requiring much less memory space. A typical [time-space trade-off](https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff). In the end I went with the second approach.

Apart from that, the rest was straightforward: simulate the falling sand until the given condition is met, and report how many sand units it took.

This was the final result for Part 1:

![](https://github.com/meithan/AoC22/blob/main/day14/part1.png)

For Part 2, the final result looks a bit like a cut-away view of an Egyptian pyramid, with inner rooms and passages:

![](https://github.com/meithan/AoC22/blob/main/day14/part2.png)


---

**Day 13**: [Distress Signal](https://adventofcode.com/2022/day/13)<a name="day13"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day13)

A problem where Python's powerful syntax and tools shine. Parsing the packets was as simple as calling [`eval`](https://docs.python.org/3/library/functions.html#eval) on each line, as they are Python-parsable lists (which can have lists as elements).

Then, the core of the solution is the `compare` function, which takes two lists (packets, or sub-lists within a packet) and determines if they are ordered according to the rules, returning -1 if they are (the left list is "smaller" than the right one), 1 if they are not (the left list is "greater" than the right), or 0 if their order cannot be determined (they are "equal"). This function goes through the elements of the two lists and checks their order, exiting if one of the lists runs out. When both elements are integers we compare them directly; if one or both elements are lists, we recursively call `compare` on them (converting integers to lists, as indicated), and return the result if it's conclusive (1 or -1).

For Part 2, instead of implementing a simple sorting algorithm like [selection sort](https://en.wikipedia.org/wiki/Selection_sort), I leveraged Python's built-in [`sorted`](https://docs.python.org/3/library/functions.html#sorted) function (which uses [Timsort](https://en.wikipedia.org/wiki/Timsort), an efficient O(n*log n) algorithm), which TIL can accept a "conventional" comparison function (a `cmp(a,b)` function that returns a value that is negative if `a < b`, positive if `a > b` or 0 if `a == b`) as its `key` parameter [as long as it is first fed](https://docs.python.org/3/howto/sorting.html#comparison-functions) to [`functools.cmp_to_key`](https://docs.python.org/3/library/functools.html#functools.cmp_to_key).

---

**Day 12**: [Hill Climbing Algorithm](https://adventofcode.com/2022/day/12)<a name="day12"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day12)

[Graph search](https://en.wikipedia.org/wiki/Graph_traversal) problems are always fun. This one was pretty straighforward, and a simple implementation of [breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) was more than enough. I did get one thing wrong initially (exactly when to mark a search node as "visited"), showing that even BFS can be tricky. I might come back to this problem later to implement a more efficient algorithm like [Dijkstra's](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), just for practice.

For Part 2 the obvious brute-force approach, i.e. running BFS for all candidate starting positions to find the best one, was suficiently fast. This is sub-optimal, of course, and more advanced algorithms (such as [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)) can compute shortest paths for multiple starting or ending positions much more efficiently.

Here's a plot of the map and (one of) the optimal path found by BFS.

![](https://github.com/meithan/AoC22/blob/main/day12/path.png)

---

**Day 11**: [Monkey in the Middle](https://adventofcode.com/2022/day/11)<a name="day11"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day11)

This was the first problem (in Part 2) where simply carefully coding what the statement describes was not enough to solve it. Some additional thinking was needed.

For Part 1 I simply coded the monkey item tossing game as described. A majority of the code was parsing the input (regular expressions make it a bit more elegant, although they were not really required) and organizing the information in a convenient way.

For Part 2, the problem made it clear that the numbers would reach ridiculous levels. And indeed, after about 50 rounds they are larger than even a 8-byte integer can represent, 2**63-1 (Python 3 "normal" integers are 8-byte signed integers, apparently). After that, instead of overflowing Python automatically switches to [arbitrary-precision](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic) "big integers", which have no theoretical maximum value and are only limited in practice by the system memory required to store them. The price that is paid, however, is that arithmetics with these big integers are considerably slower (since they're not natively supported by the CPU), to the point where my program started to take a very long to simulate each round. There was no hope of reaching the 10,000th round by doing this.

Fortunately the problem gave a clear hint: *find another way to keep [the numbers] manageable*. Since what determines to which other monkey each item is tossed is divisibility by a certain set of numbers (a different one for each monkey), one can keep only the numbers modulo the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple) of these numbers, and the divisibility checks will continue to be valid.

To show this, let's say that the divisors for which divisibility is checked for the N monkeys are `a1`, `a2`, ..., `aN`. Let's call their least common multiple `m`. Since in this case they were all prime, then `m = a1*a2*...*aN`. Now consider any integer `x`. Let `y` be `x` reduced modulo `m`, i.e. `y = x mod m`. What this means is that `x` can be expressed as `x = y + n*m = y + n*(a1*a2*...*aN)` for some integer `n` and where `y < m`. Now let's say we want to check whether `x` is divisible by one of the factors of `m`, let's say `a1`. All we have to do is to check whether `y` (the reduced version of `x`) is divisible by `a1`. For if that is the case then this means that `y = b*a1` for some integer `b` and hence `x = b*a1 + n*(a1*a2*...*aN)`, and since both terms contain `a1` as a factor, then `x` must be divisible by `a1`. Conversely, if `y` *isn't* divisible by `a1`, then it is clear that `a` doesn't divide `x` either (the two terms can't be factored in that case as all the `a` are prime).

Thus for Part 2 all that was needed is to keep the numbers modulo `m`. In my case `m` was 9699690, which means that the even when squaring the numbers never surpassed the maximum size of Python's "regular" integers, and hence arithmetics was fast. With this small change in the code, Part 2 takes a fraction of a second.

---

**Day 10**: [Cathode-Ray Tube](https://adventofcode.com/2022/day/10)<a name="day10"></a> - [my solution](https://github.com/meithan/AoC22/blob/main/day10)

I'll be honest: I love AoC problems that ask us to simulate the execution of a simplistic computer program. This one also had the concept of a screen!

For Part 1, I coded the execution in an "instruction-centric" way: we go over each instruction, and do whatever it does while increasing the cycle count as many times as indicated. *Before* (and this is important) each cycle increase (and before modifying the register) we check whether we're at one of the "checkpoints" (at 20, 60, 100, 140, 180, 220 cycles), and if so, accumulate the current signal strength (the cycle number times the current value of the register `X`).

For Part 2, I switched to a "cycle-centric" execution, something I had considered for Part 1 as it's a bit more general. We keep track of which instruction is currently being executed and how many cycles remain of that instruction. When the current instruction's remaining cycles run out, we load the next instruction (after increasing the register value in the case of `addx`). We iterate for 240 cycles, and *at the start* of each cycle we check whether the current pixel being written (given by its row and column values, computed from the current cycle number) is contained in the sprite (at most 1 units from the sprite's center, which is stored in the register `X`), adding the corresponding character to the row. At the end, we print all the rows, and the letters appear in the terminal.

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