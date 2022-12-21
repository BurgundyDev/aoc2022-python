import re
import numpy as np

def dfs(bp, maxspend, cache, time, bots, res):
    if time == 0:
        return res[0]
    
    key = tuple([time, *bots, *res])
    
    if key in cache:
        return cache[key]
    
    max_value = res[3] + bots[3] * time
    
    for bot_type, recipe in enumerate(bp):
        if bot_type != 3 and bots[bot_type] >= maxspend[bot_type]:
            continue
        
        wait = 0
        for res_amount, res_type in recipe:
            if bots[res_type] == 0:
                break
            wait = max(wait, -(-(res_amount - res[res_type]) // bots[res_type]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_temp = bots[:]
            res_temp = [x + y * (wait + 1) for x, y in zip(res, bots)]
            for res_amount, res_type in recipe:
                res_temp[res_type] -= res_amount
            bots_temp[bot_type] += 1
            for i in range(3):
                res_temp[i] = min(res_temp[i], maxspend[i] * remtime)
            max_value = max(max_value, dfs(bp, maxspend, cache, remtime, bots_temp, res_temp))
    
    cache[key] = max_value
    return max_value
    

total_value = 0

for i, line in enumerate(open("19.txt")):
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)
        bp.append(recipe)
    value = dfs(bp, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
    total_value += (i + 1) * value
    
print(total_value)

total_values = []

for i, line in enumerate(open("19.txt")):
    if i > 2:
        break
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)
        bp.append(recipe)
    value = dfs(bp, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
    total_values.append(value)
    
print(np.product(total_values))