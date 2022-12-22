import re

grid = []
done = False
sequence = ""

for line in open("22t.txt"):
    line = line[:-1]
    if line == "":
        done = True
    if done:
        sequence = line
    else:
        grid.append(line)

width = max(map(len, grid))
grid = [line + " " * (width - len(line)) for line in grid]

position = [0, 0]
next_pos = [0, 0]
move = [1, 0]

while grid[position[1]][position[0]] != ".":
    position[0] += 1

for x, y in re.findall(r"(\d+)([RL]?)", sequence):
    x = int(x)
    for _ in range(x):
        next_pos[0] = position[0]
        next_pos[1] = position[1]
        while True:
            next_pos[1] = (next_pos[1] + move[1]) % len(grid)
            next_pos[0] = (next_pos[0] + move[0]) % len(grid[0])
            if grid[next_pos[1]][next_pos[0]] != " ":
                break
        if grid[next_pos[1]][next_pos[0]] == "#":
            break
        position[0] = next_pos[0]
        position[1] = next_pos[1]
    if y == "R":
        move[1], move[0] = move[0], -move[1]
    elif y == "L":
        move[1], move[0] = -move[0], move[1]
        
mod = 0
match move:
    case [1, 0]: mod = 0
    case [0, 1]: mod = 1
    case [-1, 0]: mod = 2
    case [0, -1]: mod = 3

print("Part 1: " + str(1000 * (position[1] + 1) + 4 * (position[0] + 1) + mod))

position = [0, 0]
next_pos = [0, 0]
move = [1, 0]

while grid[position[1]][position[0]] != ".":
    position[0] += 1

for x, y in re.findall(r"(\d+)([RL]?)", sequence):
    x = int(x)
    for _ in range(x):
        pre_move = move[:]
        
        next_pos[0] = position[0] + move[0]
        next_pos[1] = position[1] + move[1]
        
        if next_pos[1] < 0 and 50 <= next_pos[0] < 100 and move[1] == -1:
            move[1], move[0] = 0, 1
            next_pos[1], next_pos[0] = next_pos[0] + 100, 0
        elif next_pos[0] < 0 and 150 <= next_pos[1] < 200 and move[0] == -1:
            move[1], move[0] = 1, 0
            next_pos[1], next_pos[0] = 0, next_pos[1] - 100
        elif next_pos[1] < 0 and 100 <= next_pos[0] < 150 and move[1] == -1:
            next_pos[1], next_pos[0] = 199, next_pos[0] - 100
        elif next_pos[1] >= 200 and 0 <= next_pos[0] < 50 and move[1] == 1:
            next_pos[1], next_pos[0] = 0, next_pos[0] + 100
        elif next_pos[0] >= 150 and 0 <= next_pos[1] < 50 and move[0] == 1:
            move[0] = -1
            next_pos[1], next_pos[0] = 149 - next_pos[1], 99
        elif next_pos[0] == 100 and 100 <= next_pos[1] < 150 and move[0] == 1:
            move[0] = -1
            next_pos[1], next_pos[0] = 149 - next_pos[1], 149
        elif next_pos[1] == 50 and 100 <= next_pos[0] < 150 and move[1] == 1:
            move[1], move[0] = 0, -1
            next_pos[1], next_pos[0] = next_pos[0] - 50, 99
        elif next_pos[0] == 100 and 50 <= next_pos[1] < 100 and move[0] == 1:
            move[1], move[0] = -1, 0
            next_pos[1], next_pos[0] = 49, next_pos[1] + 50
        elif next_pos[1] == 150 and 50 <= next_pos[0] < 100 and move[1] == 1:
            move[1], move[0] = 0, -1
            next_pos[1], next_pos[0] = next_pos[0] + 100, 49
        elif next_pos[0] == 50 and 150 <= next_pos[1] < 200 and move[0] == 1:
            move[1], move[0] = -1, 0
            next_pos[1], next_pos[0] = 149, next_pos[1] - 100
        elif next_pos[1] == 99 and 0 <= next_pos[0] < 50 and move[1] == -1:
            move[1], move[0] = 0, 1
            next_pos[1], next_pos[0] = next_pos[0] + 50, 50
        elif next_pos[0] == 49 and 50 <= next_pos[1] < 100 and move[0] == -1:
            move[1], move[0] = 1, 0
            next_pos[1], next_pos[0] = 100, next_pos[1] - 50
        elif next_pos[0] == 49 and 0 <= next_pos[1] < 50 and move[0] == -1:
            move[0] = 1
            next_pos[1], next_pos[0] = 149 - next_pos[1], 0
        elif next_pos[0] < 0 and 100 <= next_pos[1] < 150 and move[0] == -1:
            move[0] = 1
            next_pos[1], next_pos[0] = 149 - next_pos[1], 50
        
        if grid[next_pos[1]][next_pos[0]] == "#":
            move = pre_move[:]
            break
        position[0] = next_pos[0]
        position[1] = next_pos[1]
    if y == "R":
        move[1], move[0] = move[0], -move[1]
    elif y == "L":
        move[1], move[0] = -move[0], move[1]

mod = 0
match move:
    case [1, 0]: mod = 0
    case [0, 1]: mod = 1
    case [-1, 0]: mod = 2
    case [0, -1]: mod = 3
    
print("Part 2: " + str(1000 * (position[1] + 1) + 4 * (position[0] + 1) + mod))