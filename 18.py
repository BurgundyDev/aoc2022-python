import numpy as np
from aoc import get_input
from functools import lru_cache
from tqdm import tqdm

total_area = 0

cubes = []

min_x = 100
max_x = -100
min_y = 100
max_y = -100
min_z = 100
max_z = -100

for cube in open("18.txt"):
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
    

for cube in tqdm(cubes):
    area = 6
    if (cube[0] - 1, cube[1], cube[2]) in cubes:
        area -= 1
    if (cube[0] + 1, cube[1], cube[2]) in cubes:
        area -= 1
    if (cube[0], cube[1] - 1, cube[2]) in cubes:
        area -= 1
    if (cube[0], cube[1] + 1, cube[2]) in cubes:
        area -= 1
    if (cube[0], cube[1], cube[2] - 1) in cubes:
        area -= 1
    if (cube[0], cube[1], cube[2] + 1) in cubes:
        area -= 1
    total_area += area
    
print(total_area)

@lru_cache(None)
def dfs(pos):
    # do a DFS
    stack = [pos]
    seen = set()

    if pos in cubes:
        return False

    while len(stack) > 0:
        pop = stack.pop()

        if pop in cubes:
            continue

        for coord in range(3):
            if not (0 <= pop[coord] <= 20):
                return True

        if pop in seen:
            continue
        seen.add(pop)

        for coord in range(3):
            dpos = np.array([0, 0, 0])
            dpos[coord] = 1
            dneg = np.array([0, 0, 0])
            dneg[coord] = -1

            stack.append(tuple(pop + dpos))
            stack.append(tuple(pop + dneg))

    return False

total_area = 0

for x, y, z in tqdm(cubes):
    pos = np.array((x, y, z))
    
    for coord in range(3):
        dpos = np.array([0, 0, 0])
        dpos[coord] = 1

        dneg = np.array([0, 0, 0])
        dneg[coord] = -1

        for nbr in [tuple(pos + dpos), tuple(pos + dneg)]:
            total_area += dfs(nbr)
            
print(total_area)