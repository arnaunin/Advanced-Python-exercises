import json

# Open the json file in read mode
with open("maze.json", 'r') as maze_json:
    # Load the inventory list to store it in a variable
    maze = json.load(maze_json)

# Function to solve the maze and save the path in a variable
def solve_maze(maze, row, column, path = None):
    if path is None:
        path = []

    # Restrictions that prevent movement
    if not (0 <= row < len(maze)) or not (0 <= column < len(maze[0])) or maze[row][column] == 1 or (row, column) in path:
        return None
    
    path.append((row, column)) # Tuple

    # Base case // If the current position is the exit
    if maze[row][column] == 9:
        return path

    # Set de movements
    movements = [(-1,0),(1,0),(0,-1),(0,1)] # Up, down, left, right

    for movement in movements:
        new_row, new_column = row + movement[0], column + movement[1]
        result = solve_maze(maze, new_row, new_column, path.copy())
        if result:
            return result
    return None # There is no solution from this position

# Function to print the solved maze
def print_maze(maze, path):
    # Go through the rows
    for row in range(len(maze)):
        # Go through the columns
        for column in range(len(maze[0])):
            # If that position is part of the solution path, we print a * in its place
            if (row, column) in path:
                print("*", end = " ")
            # Otherwise, we print the value of that position
            else:
                print(maze[row][column], end = " ")
        print()

solved_path = solve_maze(maze, 0, 0)

if solved_path:
    print("The path to solve the maze is:")
    print_maze(maze, solved_path)
else:
    print("There is no solution for this maze")