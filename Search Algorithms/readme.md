# Maze Solver

This project implements a maze solver using a depth-first search (DFS) algorithm. It takes a maze represented as a text file and finds a path from the start point (A) to the goal point (B).

## Maze Format

The maze is represented in a text file using the following format:

- `A`: Starting point
- `B`: Goal point
- `#`: Walls or obstacles
- ` ` (space): Open paths

Example maze:

```
#####B#
##### #
####  #
#### ##
     ##
A######
```

## Algorithm

The maze is solved using a depth-first search algorithm. Here's a visual representation of how DFS works:

![DFS Maze Solving](https://d18l82el6cdm1i.cloudfront.net/uploads/mf7THWHAbL-mazegif.gif)

*Image courtesy of brillient.org*

## Usage

To run the maze solver, use the following command:

```
python maze.py maze.txt
```

Replace `maze.txt` with the path to your maze file.

## Example Run

### `maze1.txt`

1. Console Output:
   ![Conole Output of maze1](screenshots\maze_1_run.png)

2. Maze Solution Visualization:
   ![Visual Output of maze1](screenshots\maze_1_solve.png)

3. Original Maze File (maze1.txt):
   ```
   #####B#
   ##### #
   ####  #
   #### ##
        ##
   A######
   ```


### `maze2.txt`

1. Console Output:
   ![Conole Output of maze2](screenshots\maze_2_run.png)

2. Maze Solution Visualization:
   ![Visual Output of maze2](screenshots\maze_2_solve.png)

3. Original Maze File (maze2.txt):
   ```
   ###                 #########
   #   ###################   # #
   # ####                # # # #
   # ################### # # # #
   #                     # # # #
   ##################### # # # #
   #   ##                # # # #
   # # ## ### ## ######### # # #
   # #    #   ##B#         # # #
   # # ## ################ # # #
   ### ##             #### # # #
   ### ############## ## # # # #
   ###             ##    # # # #
   ###### ######## ####### # # #
   ###### ####             #   #
   A      ######################
   ```

### `maze3.txt`

1. Console Output:
   ![Conole Output of maze3](screenshots\maze_3_run.png)

2. Maze Solution Visualization:
   ![Visual Output of maze3](screenshots\maze_3_solve.png)

3. Original Maze File (maze3.txt):
   ```
   ##    #
   ## ## #
   #B #  #
   # ## ##
        ##
   A######
   ```




## Implementation Details

The project consists of a single Python file `maze.py` that contains the following key components:

1. `Node` class: Represents a state in the maze.
2. `StackFrontier` class: Implements a stack data structure for DFS.
3. `QueueFrontier` class: (Unused in this implementation but available for breadth-first search).
4. `Maze` class: Handles maze parsing, solving, and visualization.

### Code Explanation

1. **Node Class**: 
   - Represents a state in the maze search.
   - Contains the current state (position), parent node, and action taken to reach this state.

2. **StackFrontier Class**:
   - Implements a stack for DFS.
   - Methods include add, remove, contains_state, and empty.

3. **QueueFrontier Class**:
   - Inherits from StackFrontier but overrides the remove method to implement FIFO behavior.

4. **Maze Class**:
   - The core of the program, handling maze representation and solving.
   - Key methods:
     - `__init__`: Reads the maze file and initializes the maze structure.
     - `print`: Prints a text representation of the maze.
     - `neighbors`: Finds valid neighboring cells for a given state.
     - `solve`: Implements the DFS algorithm to find a solution.
     - `output_image`: Generates a PNG image of the solved maze.

5. **Main Execution**:
   - Checks for correct command-line arguments.
   - Creates a Maze object, solves it, and outputs the results.

### Solving Algorithm (DFS)

1. Initialize the frontier with the starting position.
2. While the frontier is not empty:
   - Remove a node from the frontier.
   - If the node is the goal, we have a solution.
   - Mark the node as explored.
   - Add the node's neighbors to the frontier if they haven't been explored.
3. If the frontier becomes empty, there's no solution.

## Output

The program outputs:
1. A text representation of the maze and its solution
2. The number of states explored during the search
3. An image file `maze.png` showing the solved maze, with:
   - Red: Start point
   - Green: Goal point
   - Yellow: Solution path
   - Orange: Explored states
   - Gray: Walls
   - White: Unexplored paths

## Requirements

- Python 3.x
- Pillow library (for image generation)

## Installation

1. Install Python `3.x`
2. Install the required library:
   ```
   pip install -r requirements.txt
   ```


