from collections import defaultdict


def most_common_bit(count, total):
    return "1" if count / total >= 0.5 else "0"


def least_common_bit(count, total):
    return "1" if count / total <= 0.5 else "0"


b1s = defaultdict(lambda: 0)

total = 0
with open("Day 3/data.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    total = len(lines)

    for line in lines:
        for idx, b in enumerate(line):
            b1s[idx] = b1s[idx] + int(b)  # type: ignore

gamma = int("".join([most_common_bit(value, total) for key, value in b1s.items()]), 2)
epsilon = int(
    "".join([least_common_bit(value, total) for key, value in b1s.items()]), 2
)


print(f"Answer: {gamma * epsilon}")
