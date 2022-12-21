from aoc import get_input

rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]

data = [1 if char == ">" else -1 for char in get_input(17)]
solid = {x - 1j for x in range(7)}
height = 0
seen = {}

def summarize():
    o = [-20] * 7
    
    for x in solid:
        r = int(x.real)
        i = int(x.imag)
        o[r] = max(o[r], i)
    
    top = max(o)
    return tuple(x - top for x in o)


rockCount = 0
rockID = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rockID]}


while rockCount < 2022:
    for jet in data:
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rockCount += 1
            height = max(x.imag for x in solid) + 1
            if rockCount >= 2022:
                break
            rockID = (rockID + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rockID]}
        else:
            rock = moved

print(int(height))

solid = {x - 1j for x in range(7)}
height = 0
seen = {}
rockCount = 0
rockID = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rockID]}

T = 1000000000000

while rockCount < T:
    for ji, jet in enumerate(data):
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rockCount += 1
            o = height
            height = max(x.imag for x in solid) + 1
            if rockCount >= T:
                break
            rockID = (rockID + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rockID]}
            key = (ji, rockID, summarize())
            if key in seen:
                lastRockCount, lastHeight = seen[key]
                rem = T - rockCount
                rep = rem // (rockCount - lastRockCount)
                offset = rep * (height - lastHeight)
                rockCount += rep * (rockCount - lastRockCount)
                seen = {}
            seen[key] = (rockCount, height)
        else:
            rock = moved

print(int(height + offset))