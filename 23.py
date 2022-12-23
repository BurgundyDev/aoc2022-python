elves = []

moves = {
    'N': [0, -1],
    'S': [0, 1],
    'E': [1, 0],
    'W': [-1, 0],
    'NE': [1, -1],
    'NW': [-1, -1],
    'SE': [1, 1],
    'SW': [-1, 1]
}

for y, line in enumerate(open("23.txt")):
    for x, char in enumerate(line):
        if char == '#':
            elves.append([x, y])
ans2 = 0
def answer():
    min_x = 10000000000
    max_x = -10000000000
    min_y = 10000000000
    max_y = -10000000000
    for elf in elves:
        if elf[0] < min_x:
            min_x = elf[0]
        if elf[0] > max_x:
            max_x = elf[0]
        if elf[1] < min_y:
            min_y = elf[1]
        if elf[1] > max_y:
            max_y = elf[1]

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    ans = (width * height) - len(elves) - 1
    # print(ans)
moving = [True for _ in range(len(elves))]
while True:
    moving = [False for _ in range(len(elves))]
    proposed_moves = [[] for _ in range(len(elves))]

    for i, elf in enumerate(elves):
        # print(elf)
        elf_moves = {key: [elf[0] + x[0], elf[1] + x[1]] for key, x in moves.items()}
        for key, move in elf_moves.items():
            if elves.count(move) > 0:
                moving[i] = True
                break
            
        if moving[i]:
            if elves.count(elf_moves['N']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['NW']) == 0:
                proposed_moves[i] = elf_moves['N']
            elif elves.count(elf_moves['S']) == 0 and elves.count(elf_moves['SE']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['S']
            elif elves.count(elf_moves['W']) == 0 and elves.count(elf_moves['NW']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['W']
            elif elves.count(elf_moves['E']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['SE']) == 0:
                proposed_moves[i] = elf_moves['E']

    if moving.count(True) == 0:
        break
    for i, move in enumerate(proposed_moves):
        if proposed_moves.count(move) == 1:
            continue
        else:
            for x, elem in enumerate(proposed_moves):
                if move == elem:
                    proposed_moves[x] = []
            proposed_moves[i] = []

    for i, elf in enumerate(elves):
        if len(proposed_moves[i]) == 2:
            elves[i] = [proposed_moves[i][0], proposed_moves[i][1]]

    answer()
    ans2 += 1

    moving = [False for _ in range(len(elves))]
    proposed_moves = [[] for _ in range(len(elves))]
    for i, elf in enumerate(elves):
        moving[i] = False
        # print(elf)
        elf_moves = {key: [elf[0] + x[0], elf[1] + x[1]] for key, x in moves.items()}
        for key, move in elf_moves.items():
            if elves.count(move) > 0:
                moving[i] = True
                break

        if moving[i]:
            if elves.count(elf_moves['S']) == 0 and elves.count(elf_moves['SE']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['S']
            elif elves.count(elf_moves['W']) == 0 and elves.count(elf_moves['NW']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['W']
            elif elves.count(elf_moves['E']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['SE']) == 0:
                proposed_moves[i] = elf_moves['E']
            elif elves.count(elf_moves['N']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['NW']) == 0:
                proposed_moves[i] = elf_moves['N']

    if moving.count(True) == 0:
        break
    for i, move in enumerate(proposed_moves):
        if proposed_moves.count(move) == 1:
            continue
        else:
            for x, elem in enumerate(proposed_moves):
                if move == elem:
                    proposed_moves[x] = []
            proposed_moves[i] = []

    for i, elf in enumerate(elves):
        if len(proposed_moves[i]) == 2:
            elves[i] = [proposed_moves[i][0], proposed_moves[i][1]]

    answer()
    ans2 += 1

    moving = [False for _ in range(len(elves))]
    proposed_moves = [[] for _ in range(len(elves))]
    for i, elf in enumerate(elves):
        moving[i] = False
        # print(elf)
        elf_moves = {key: [elf[0] + x[0], elf[1] + x[1]] for key, x in moves.items()}
        for key, move in elf_moves.items():
            if elves.count(move) > 0:
                moving[i] = True
                break

        if moving[i]:
            if elves.count(elf_moves['W']) == 0 and elves.count(elf_moves['NW']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['W']
            elif elves.count(elf_moves['E']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['SE']) == 0:
                proposed_moves[i] = elf_moves['E']
            elif elves.count(elf_moves['N']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['NW']) == 0:
                proposed_moves[i] = elf_moves['N']
            elif elves.count(elf_moves['S']) == 0 and elves.count(elf_moves['SE']) == 0 and elves.count(elf_moves['SW']) == 0:
                    proposed_moves[i] = elf_moves['S']

    if moving.count(True) == 0:
        break
    for i, move in enumerate(proposed_moves):
        if proposed_moves.count(move) == 1:
            continue
        else:
            for x, elem in enumerate(proposed_moves):
                if move == elem:
                    proposed_moves[x] = []
            proposed_moves[i] = []

    for i, elf in enumerate(elves):
        if len(proposed_moves[i]) == 2:
            elves[i] = [proposed_moves[i][0], proposed_moves[i][1]]

    answer()
    ans2 += 1

    moving = [False for _ in range(len(elves))]
    proposed_moves = [[] for _ in range(len(elves))]
    for i, elf in enumerate(elves):
        moving[i] = False
        # print(elf)
        elf_moves = {key: [elf[0] + x[0], elf[1] + x[1]] for key, x in moves.items()}
        for key, move in elf_moves.items():
            if elves.count(move) > 0:
                moving[i] = True
                break

        if moving[i]:
            if elves.count(elf_moves['E']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['SE']) == 0:
                proposed_moves[i] = elf_moves['E']
            elif elves.count(elf_moves['N']) == 0 and elves.count(elf_moves['NE']) == 0 and elves.count(elf_moves['NW']) == 0:
                proposed_moves[i] = elf_moves['N']
            elif elves.count(elf_moves['S']) == 0 and elves.count(elf_moves['SE']) == 0 and elves.count(elf_moves['SW']) == 0:
                    proposed_moves[i] = elf_moves['S']
            elif elves.count(elf_moves['W']) == 0 and elves.count(elf_moves['NW']) == 0 and elves.count(elf_moves['SW']) == 0:
                proposed_moves[i] = elf_moves['W']

    if moving.count(True) == 0:
        break
    for i, move in enumerate(proposed_moves):
        if proposed_moves.count(move) == 1:
            continue
        else:
            for x, elem in enumerate(proposed_moves):
                if move == elem:
                    proposed_moves[x] = []
            proposed_moves[i] = []

    for i, elf in enumerate(elves):
        if len(proposed_moves[i]) == 2:
            elves[i] = [proposed_moves[i][0], proposed_moves[i][1]]
    answer()
    ans2 += 1
    print(ans2)
    
ans2 += 1
print(ans2)