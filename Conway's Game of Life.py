'''
**Problem Statement:**
Imagine an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two
possible states, live or dead. Every cell interacts with its eight neighbors, which are the cells that are
directly horizontally, vertically, or diagonally adjacent.
*At each step in time (tick), the following transitions occur:
1. Any live cell with fewer than two live neighbors dies, as if by loneliness.
2. Any live cell with more than three live neighbors dies, as if by overcrowding.
3. Any live cell with two or three live neighbors lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbors comes to life.
The initial pattern constitutes the 'seed' (randomly placed 500 cells) of the system. The first generation is
created by applying the above rules simultaneously to every cell in the seed — births and deaths happen
simultaneously, and the discrete moment at which this happens is called a tick. (In other words, each
generation is a pure function of the one before.)

*Problem statement understanding through https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Conway's Game of Life
Most of the code is written by taking reference from below link and modified little.
https://robertheaton.com/2018/07/20/project-2-game-of-life/
Also https://gist.github.com/robert/5100dfffe8afbb04b560dd0fff184753 github project helped me in understanding.

**Instruction to provide inputs:**
While running, user have to create 'input.txt' text file in which user gives input to the program
Input in the input.txt file should be in the format as shown below:
    000000
    000000
    001110
    011100
    000000
    000000
'''

import random
import numpy as np
import time

dead = 0
live = 1

class Grid():
    '''This class contains methods to create a board of all the cells'''
    def dead_phase(height, width):
        '''This method creates list ot lists of dead cells only(i.e.=0)'''
        return np.zeros((height, width), dtype=int).tolist()

    def random_phase(height, width):
        '''This method randomizes each element of the list created by
        function-dead_phase() either to dead=0 or live=1
        here 'phase' means state of the cell(i.e. dead/live)'''
        globals()
        phase = Grid.dead_phase(height, width)
        for i in range(len(phase)):
            for j in range(len(phase)):
                random_number = random.random()
                if random_number >= 0.5:  # randomizing with equal probability
                    phase[i][j] = dead
                else:
                    phase[i][j] = live
        return phase

    def phase_height(phase):
        '''This method defines height of the board'''
        return len(phase[0])  # defining width of the board

    def phase_width(phase):
        '''This method defines width of the board'''
        return len(phase)


    def later_board_state(initial_state):
        '''This method updates next view of board'''
        width = Grid.phase_width(initial_state)
        height = Grid.phase_height(initial_state)
        next_phase = Grid.dead_phase(width, height)

        for i in range(0, width):
            for j in range(0, height):
                next_phase[i][j] = Cell.next_cell_val((i, j), initial_state)
        return next_phase

    def render(board_state):
        '''This method gives better visualization of the board'''
        display_as = {dead: ' ', live: u"\u2588"}
        lines = []
        for j in range(0, Grid.phase_height(board_state)):
            line = ''
            for i in range(0, Grid.phase_width(board_state)):
                line += display_as[board_state[i][j]] * 2
            lines.append(line)
        print("\n".join(lines))

    def load_board_state(filepath):
        '''This method takes path of 'input.txt' file and prepares a board of cells'''
        with open(filepath, 'r') as f:
            lines = [l.rstrip() for l in f.readlines()]
        height = len(lines)
        width = len(lines[0])
        board = Grid.dead_phase(height, width)
        for x, line in enumerate(lines):
            for y, char in enumerate(line):
                board[x][y] = int(char)
        return board

    def run_repeatedly(init_state):
        '''This is continuously running loop method which will assign new state
        as a base state and defines new state from this base state'''
        next_state = init_state
        while True:
            Grid.render(next_state)
            next_state = Grid.later_board_state(next_state)
            time.sleep(0.03)
class Cell():
    '''This class contains methods to determine state of the cell'''
    def next_cell_val(cell_cordinates, phase):
        '''This method defines the next state of the cell'''
        width = Grid.phase_width(phase)
        height = Grid.phase_height(phase)
        x, y = cell_cordinates[0], cell_cordinates[1]
        live_count = 0
        for i in range((x - 1), (x + 1) + 1):
            if i < 0 or i >= width: continue
            for j in range((y - 1), (y + 1) + 1):
                if j < 0 or j >= height: continue
                if i == x and j == y: continue
                if phase[i][j] == live:
                    live_count += 1
        if phase[x][y] == live:
            if live_count <= 1:     #Condition 1. Any live cell with fewer than two live neighbors dies, as if by loneliness.
                return dead
            elif live_count <= 3:   #Condition 3. Any live cell with two or three live neighbors lives, unchanged, to the next generation.
                return live
            else:
                return dead         #Condition 2. Any live cell with more than three live neighbors dies, as if by overcrowding.
        else:
            if live_count == 3:     #Condition 4. Any dead cell with exactly three live neighbors comes to life.
                return live
            else:
                return dead


if __name__ == "__main__":
    init_state = Grid.load_board_state('input.txt')    # Give filepath of 'input.txt' file here
    Grid.run_repeatedly(init_state)
