from aoc import get_input

total_area = 0

cubes = []

min_x = 100
max_x = -100
min_y = 100
max_y = -100
min_z = 100
max_z = -100

for cube in get_input(18).splitlines():
    x = int(cube.split(",")[0])
    if(x > max_x - 1):
        max_x = x + 1
    elif(x < min_x + 1):
        min_x = x - 1
    
    y = int(cube.split(",")[1])
    if(y > max_y - 1):
        max_y = y + 1
    elif(y < min_y + 1):
        min_y = y - 1
        
    z = int(cube.split(",")[2])
    if(z > max_z - 1):
        max_z = z + 1
    elif(z < min_z + 1):
        min_z = z - 1
        
    cubes.append((x, y, z))
    

# for cube in cubes:
#     area = 6
#     if [cube[0] - 1, cube[1], cube[2]) in cubes:
#         area -= 1
#     if [cube[0] + 1, cube[1], cube[2]) in cubes:
#         area -= 1
#     if [cube[0], cube[1] - 1, cube[2]) in cubes:
#         area -= 1
#     if [cube[0], cube[1] + 1, cube[2]) in cubes:
#         area -= 1
#     if [cube[0], cube[1], cube[2] - 1) in cubes:
#         area -= 1
#     if [cube[0], cube[1], cube[2] + 1) in cubes:
#         area -= 1
#     total_area += area
    
# print(total_area)
pockets = []

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        for z in range(min_z, max_z):
            checked = (x, y, z)
            if checked not in cubes:
                hits = 0
                if (checked[0] - 1, checked[1], checked[2]) in cubes or (checked[0] - 2, checked[1], checked[2]) in cubes or (checked[0] - 3, checked[1], checked[2]) in cubes:
                    hits += 1
                else: continue
                if (checked[0] + 1, checked[1], checked[2]) in cubes or (checked[0] + 2, checked[1], checked[2]) in cubes or (checked[0] + 3, checked[1], checked[2]) in cubes:
                    hits += 1
                else: continue
                if (checked[0], checked[1] - 1, checked[2]) in cubes or (checked[0], checked[1] - 2, checked[2]) in cubes or (checked[0], checked[1] - 3, checked[2]) in cubes:
                    hits += 1
                else: continue
                if (checked[0], checked[1] + 1, checked[2]) in cubes or (checked[0], checked[1] + 2, checked[2]) in cubes or (checked[0], checked[1] + 3, checked[2]) in cubes:
                    hits += 1
                else: continue
                if (checked[0], checked[1], checked[2] - 1) in cubes or (checked[0], checked[1], checked[2] - 2) in cubes or (checked[0], checked[1], checked[2] - 3) in cubes:
                    hits += 1
                else: continue
                if (checked[0], checked[1], checked[2] + 1) in cubes or (checked[0], checked[1], checked[2] - 2) in cubes or (checked[0], checked[1], checked[2] - 3) in cubes:
                    hits += 1
                else: continue
                if hits == 6:
                    pockets.append(checked)
                    
print(pockets)

total_area = 0
for cube in cubes:
    area = 0
    if (cube[0] - 1, cube[1], cube[2]) not in cubes and (cube[0] - 1, cube[1], cube[2]) not in pockets:
        area += 1
    if (cube[0] + 1, cube[1], cube[2]) not in cubes and (cube[0] + 1, cube[1], cube[2]) not in pockets:
        area += 1
    if (cube[0], cube[1] - 1, cube[2]) not in cubes and (cube[0], cube[1] - 1, cube[2]) not in pockets:
        area += 1
    if (cube[0], cube[1] + 1, cube[2]) not in cubes and (cube[0], cube[1] + 1, cube[2]) not in pockets:
        area += 1
    if (cube[0], cube[1], cube[2] - 1) not in cubes and (cube[0], cube[1], cube[2] - 1) not in pockets:
        area += 1
    if (cube[0], cube[1], cube[2] + 1) not in cubes and (cube[0], cube[1], cube[2] + 1) not in pockets:
        area += 1
    total_area += area
    
print(total_area)