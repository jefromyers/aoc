from math import floor
from string import ascii_lowercase, ascii_uppercase

LOWER = {l: i for i, l in enumerate(ascii_lowercase, start=1)}
UPPER = {l: i for i, l in enumerate(ascii_uppercase, start=27)}

if __name__ == "__main__":
    print("woop")
    fn = "example.txt"
    fn = "live.txt"

    score = 0
    sacks = [line.strip() for line in open(fn, "rt").readlines()]
    current = 0
    while current < len(sacks):
        bags = sacks[current : current + 3]
        print(f"{ bags }")
        current += 3

        common = (set(bags[0]) & set(bags[1]) & set(bags[2])).pop()
        print(f"Common: { common }")
        score += LOWER[common] if common.islower() else UPPER[common]

    print(f"Score: {score}")
