import sympy

class Monkey:
    def __init__(self, name, val, operation, a, b):
        self.name = name
        self.val = val
        self.operation = operation
        self.a = a
        self.b = b

monkeys = []

for monkey in open("21.txt"):
    if(len(monkey.split(" ")) == 4):
        mon = Monkey(monkey.split(" ")[0].strip(":"), None, monkey.split(" ")[2], monkey.split(" ")[1], monkey.split(" ")[3].strip())
        monkeys.append(mon)
    else:
        mon = Monkey(monkey.split(" ")[0].strip(":"), int(monkey.split(" ")[1]), None, None, None)
        monkeys.append(mon)
        
    
vals = {}
root_idx = 0

for idx, monkey in enumerate(monkeys):
    if monkey.name == "root":
        root_idx = idx
    if monkey.a == None:
        vals[monkey.name] = monkey.val
        
for monkey in monkeys:
    if monkey.name in vals:
        continue
    if monkey.a not in vals or monkey.b not in vals:
        monkeys.append(monkey)
    else:
        match monkey.operation:
            case "+":
                vals[monkey.name] = vals[monkey.a] + vals[monkey.b]
            case "-":
                vals[monkey.name] = vals[monkey.a] - vals[monkey.b]
            case "*":
                vals[monkey.name] = vals[monkey.a] * vals[monkey.b]
            case "/":
                vals[monkey.name] = vals[monkey.a] / vals[monkey.b]
            case _:
                print("Operation error!")
                    
print(vals["root"])

vals = { "humn": sympy.Symbol("x") }
root_idx = 0

for idx, monkey in enumerate(monkeys):
    if monkey.name == "root":
        root_idx = idx
    if monkey.a == None and monkey.name != "humn":
        vals[monkey.name] = sympy.Integer(monkey.val)

for monkey in monkeys:
    if monkey.name in vals:
        continue
    if monkey.a not in vals or monkey.b not in vals:
        monkeys.append(monkey)
    else:
        if monkey.name == "root":
            print(sympy.solve(vals[monkey.a] - vals[monkey.b]))
            break
        match monkey.operation:
            case "+":
                vals[monkey.name] = vals[monkey.a] + vals[monkey.b]
            case "-":
                vals[monkey.name] = vals[monkey.a] - vals[monkey.b]
            case "*":
                vals[monkey.name] = vals[monkey.a] * vals[monkey.b]
            case "/":
                vals[monkey.name] = vals[monkey.a] / vals[monkey.b]
            case _:
                print("Operation error!")
    
