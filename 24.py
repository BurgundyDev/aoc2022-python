from heapq import heappop, heappush
from math import lcm
from aoc import get_input

grid = get_input(24).strip().split("\n")
# grid = open("24.txt").read().strip().splitlines()

for line in grid:
    print(line)
    
height = len(grid)
width = len(grid[0])

start = (0, 1)
end = (height - 1, width - 2)

period = lcm(width-2, height-2)

arrows = ">v<^"

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

blizzards = set()
for y in range(height):
    for x in range(width):
        char = grid[y][x]
        if char in arrows:
            blizzards.add((y, x, arrows.index(char)))

states = [set()] * period
states[0] = blizzards
for t in range(1, period):
    blizzards_new = set()
    
    for blizz in blizzards:
        row, col, dir = blizz
        mrow, mcol = dirs[dir]
        new_row, new_col = row + mrow, col + mcol
        
        if new_row == 0:
            assert dir == 3
            new_row = height - 2
        elif new_row == height - 1:
            assert dir == 1
            new_row = 1
            
        if new_col == 0:
            assert dir == 2
            new_col = width - 2
        elif new_col == width - 1:
            assert dir == 0
            new_col = 1
            
        blizzards_new.add((new_row, new_col, dir))
    
    states[t] = blizzards_new
    blizzards = blizzards_new
    
def occupied(loc, st):
    for d in range(4):
        if (loc[0], loc[1], d) in st:
            return True
    return False

pq = [(0, start, False, False)]
visited = set()
hit_once = False

while len(pq) > 0:
    top = heappop(pq)
    if top in visited:
        continue
    visited.add(top)
    
    time, pos, hit_end, hit_start = top
    row, col = pos
    
    assert not (hit_start and not hit_end)
    
    assert not occupied(pos, states[time % period])
    
    if pos == end:
        if hit_end and hit_start:
            print("Full time for part 2: " + str(time))
            break
        hit_end = True
        if not hit_once:
            hit_once = True
            print("Full time for part 1: " + str(time))
        
    if pos == start and hit_end:
        hit_start = True
    
    for drow, dcol in (dirs + [[0, 0]]):
        new_row, new_col = row + drow, col + dcol
        new_loc = (new_row, new_col)

        # Within bounds?
        if (not new_loc in [start, end]) \
            and not (1 <= new_row <= height - 2
                and 1 <= new_col <= width - 2):
            continue

        # Check if hitting a blizzard
        if occupied(new_loc, states[(time + 1) % period]):
            continue

        new_state = (time + 1, new_loc, hit_end, hit_start)
        heappush(pq, new_state)
