# Maze Solver

This Python script implements a maze generator and solver that interacts with a JSON file to manage the maze structure. It allows the user to find a path from the start position to the exit within a defined maze. The maze is represented as a list of lists, where `0`s indicate valid paths, `1`s indicate walls, and `9` indicates the exit.

## Features
- **Load Maze**: Load a maze structure from a JSON file (`maze.json`).
- **Solve Maze**: Find a valid path from the starting position to the exit using depth-first search.
- **Print Solved Maze**: Display the maze with the solution path marked with asterisks (`*`).

## How It Works
The maze is stored in a JSON file named `maze.json`. When the program starts, it reads the maze data from this file and stores it in memory. The `solve_maze` function uses recursion to explore possible paths through the maze. It checks for movement restrictions, such as walls and already visited positions. Once a valid path to the exit is found, the solution is returned.

### Example JSON Format
The `maze.json` file should be structured as follows:
```json
[
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 9],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]




