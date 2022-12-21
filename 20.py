from tqdm import tqdm

class Element:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
nums = [Element(int(x)) for x in open("20.txt")]

for i in range(len(nums)):
    nums[i].right = nums[(i + 1) % len(nums)]
    nums[i].left = nums[(i - 1) % len(nums)]
     
mod = len(nums) - 1

for elem in nums:
    if elem.val == 0:
        zero = elem
        continue
    ref = elem
    if elem.val > 0:
        for _ in range(elem.val % mod):
            ref = ref.right
        if elem == ref:
            continue
        # dereferencing the neighbouring nodes and moving the reference
        elem.right.left = elem.left
        elem.left.right = elem.right
        ref.right.left = elem
        elem.right = ref.right
        ref.right = elem
        elem.left = ref
    else:
        for _ in range(-elem.val % mod):
            ref = ref.left
        if elem == ref:
            continue
        elem.left.right = elem.right
        elem.right.left = elem.left
        ref.left.right = elem
        elem.left = ref.left
        ref.left = elem
        elem.right = ref
        
ans1 = 0

for _ in range(3):
    for _ in range(1000):
        zero = zero.right
    ans1 += zero.val

print(ans1)

nums = [Element(int(x) * 811589153) for x in open("20.txt")]

for i in range(len(nums)):
    nums[i].right = nums[(i + 1) % len(nums)]
    nums[i].left = nums[(i - 1) % len(nums)]
     
mod = len(nums) - 1
for _ in tqdm(range(10)):
    for elem in nums:
        if elem.val == 0:
            zero = elem
            continue
        ref = elem
        if elem.val > 0:
            for _ in range(elem.val % mod):
                ref = ref.right
            if elem == ref:
                continue
            # dereferencing the neighbouring nodes and moving the reference
            elem.right.left = elem.left
            elem.left.right = elem.right
            ref.right.left = elem
            elem.right = ref.right
            ref.right = elem
            elem.left = ref
        else:
            for _ in range(-elem.val % mod):
                ref = ref.left
            if elem == ref:
                continue
            elem.left.right = elem.right
            elem.right.left = elem.left
            ref.left.right = elem
            elem.left = ref.left
            ref.left = elem
            elem.right = ref
        
ans2 = 0

for _ in range(3):
    for _ in range(1000):
        zero = zero.right
    ans2 += zero.val
    
print(ans2)