# Advent of Code 2022 in Python

This repo contains my answers for Days 16 and up of AoC 2022. This is a result of my complete failure to do them on time in Rust and needing something I know more intimately.

[My answers in Rust.](https://github.com/BurgundyDev/aoc2022-rust)

[My answers in Kotlin.](https://github.com/BurgundyDev/aoc2022-kotlin)


# Helper functions
## Initialize:

When cd:ed into this repo, run;

```bash
$ python -m aoc
```

This will ask you for your session cookie (which can be found in the application tab in most browsers devtools when on adventofcode.com).

## Usage: 

In `[day_nr].py`:
```python
from aoc import get_input

# get_input(x) returns a string of the complete input for day x of year specified in year.txt
data = get_input(1).splitlines()

for line in data:
    print(line)
```

