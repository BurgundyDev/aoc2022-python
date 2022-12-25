import numpy as np

# reqs = get_input(24).strip().split("\n")
reqs = open("25t.txt").read().strip().splitlines()

snafu = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

num_reqs = []

for req in reqs:
    reversed = req[::-1]
    num = 0
    for i, char in enumerate(reversed):
        num += snafu[char] * (5**i)
    print(num)
    num_reqs.append(num)
    
dec_sum = np.sum(num_reqs)
print(dec_sum)

snafu_trans = ["0", "1", "2", "=", "-"]

ans = ""
while dec_sum > 0:
    num = ((dec_sum + 2) % 5) - 2
    dec_sum -= num
    dec_sum //= 5
    ans += snafu_trans[num]
    
ans = ans[::-1]
print(ans)