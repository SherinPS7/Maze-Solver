import tkinter as tk

# Define your maze as a 2D list
maze = [
    ['E', '0', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '0', '1'],
    ['1', '1', '0', '1', '0', '0', '1'],
    ['0', '0', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', 'X', '1']
]

# Function to draw the maze
def draw_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '1':
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill="black")
            elif maze[i][j] == '0':
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill="white")

# Function to perform depth-first search
def dfs(x, y):
    if maze[x][y] == 'X':
        return True
    if maze[x][y] == '1' or maze[x][y] == '.':
        return False

    # Mark the current cell as visited
    maze[x][y] = '.'

    # Right
    if y < len(maze[0]) - 1 and dfs(x, y + 1):
        path.append((x, y + 1))
        return True
    # Down
    if x < len(maze) - 1 and dfs(x + 1, y):
        path.append((x + 1, y))
        return True
    # Left
    if y > 0 and dfs(x, y - 1):
        path.append((x, y - 1))
        return True
    # Up
    if x > 0 and dfs(x - 1, y):
        path.append((x - 1, y))
        return True

    return False

# Function to solve the maze
def solve_maze():
    start = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'E':
                start = (i, j)
                break

    global path
    path = [start]

    if dfs(start[0], start[1]):
        draw_solution(path)
    else:
        print("No path found")

# Function to draw the solution path with gradient colors
def draw_solution(path):
    start_color = "#FF69B4"  # Pink
    end_color = "#800080"  # Purple

    for i, (x, y) in enumerate(path):
        gradient = i / (len(path) - 1)  # Normalize the position
        r = int((1 - gradient) * int(start_color[1:3], 16) + gradient * int(end_color[1:3], 16))
        g = int((1 - gradient) * int(start_color[3:5], 16) + gradient * int(end_color[3:5], 16))
        b = int((1 - gradient) * int(start_color[5:7], 16) + gradient * int(end_color[5:7], 16))
        color = "#{:02X}{:02X}{:02X}".format(r, g, b)

        canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill=color)

# Create the main window
window = tk.Tk()
window.title("Maze Solver")

# Create a canvas for drawing
cell_size = 40
canvas = tk.Canvas(window, width=len(maze[0]) * cell_size, height=len(maze) * cell_size)
canvas.pack()

# Draw the maze
draw_maze()

# Create a "Solve" button
solve_button = tk.Button(window, text="Solve", command=solve_maze)
solve_button.pack()

# Start the GUI application
window.mainloop()

