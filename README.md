# Project-Conway-s-Game-of-Life

**Problem Statement:**
Imagine an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two
possible states, live or dead. Every cell interacts with its eight neighbors, which are the cells that are
directly horizontally, vertically, or diagonally adjacent.

**At each step in time (tick), the following transitions occur:**
1. Any live cell with fewer than two live neighbors dies, as if by loneliness.
2. Any live cell with more than three live neighbors dies, as if by overcrowding.
3. Any live cell with two or three live neighbors lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbors comes to life.
The initial pattern constitutes the 'seed' (randomly placed 500 cells) of the system. The first generation is
created by applying the above rules simultaneously to every cell in the seed — births and deaths happen
simultaneously, and the discrete moment at which this happens is called a tick. (In other words, each
generation is a pure function of the one before.)

**Problem statement:** https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Conway's Game of Life.

**Instruction to provide inputs:**

While running, user have to create 'input.txt' text file in which user gives input to the program.
Input to the 'input.txt' file should be in the following format:
    
    000000
    000000
    001110
    011100
    000000
    000000
