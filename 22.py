from aoc import get_input
import re

file = "22t.txt"

def turn(move, direction):
    match direction:
        case 'R':
            match move:
                case [1, 0]: return [0, 1]
                case [0, 1]: return [-1, 0]
                case [-1, 0]: return [0, -1]
                case [0, -1]: return [1, 0]
                case _: print("Incorrect move statement! Move: " + str(move)); assert False
        case 'L':
            match move:
                case [1, 0]: return [0, -1]
                case [0, 1]: return [1, 0]
                case [-1, 0]: return [0, 1]
                case [0, -1]: return [1, 0]
                case _: print("Incorrect move statement! Move: " + str(move)); assert False
        case _: print("Incorrect turn direction! Direction input: " + str(direction)); assert False

map = []
task_list_str = ""
task_list_bool = False
player_pos = [0, 0]
move = [1, 0]

for i, row in enumerate(open(file)):
    if row == "\n":
        task_list_bool = True
        continue
    if task_list_bool:
        task_list_str = row
        break    
    row_as_list = []
    for char in row:
        match char:
            case ' ': row_as_list.append("a")
            case '#': row_as_list.append("w")
            case '.': row_as_list.append(".")
            case '\n': continue
            case _: print("Input error! Invalid character: " + char); assert False
    map.append(row_as_list)

temp_tasks = re.split('(\d+)', task_list_str)

while temp_tasks.count('') > 0:
    temp_tasks.remove('')
    
tasks = []
    
for task in temp_tasks:
    try:
        tasks.append(int(task))
    except:
        for char in task:
            tasks.append(char)

for i, tile in enumerate(map[0]):
    if tile == '.':
        player_pos[0] = i
        break
#print(player_pos)        
        
for row in map:
    for tile in row:
        print(tile, end='')
    print()

for task in tasks:
    print(task)
    if task == 'L' or task == 'R':
        move = turn(move, task)
    else:
        for _ in range(task):
            prospective_move = [player_pos[0] + move[0], player_pos[1] + move[1]]
            
            if map[prospective_move[1]][prospective_move[0]] == "w":
                break
            else:
                player_pos = prospective_move
        print(player_pos)
                
print(player_pos)
        