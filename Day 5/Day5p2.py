import re
from collections import defaultdict

ocean_map = defaultdict(lambda: 0)
with open("Day 5/data.txt") as f:
    rows = [list(map(int, re.split(",| -> ", line.strip()))) for line in f.readlines()]

    for row in rows:
        if row[0] == row[2]:
            for y in range(min(row[1], row[3]), max(row[1], row[3]) + 1):
                ocean_map[(row[0], y)] += 1  # type:ignore
        elif row[1] == row[3]:
            for x in range(min(row[0], row[2]), max(row[0], row[2]) + 1):
                ocean_map[(x, row[1])] += 1  # type:ignore
        else:
            for i in range(0, abs(row[0] - row[2]) + 1):
                x_diff = 1 if row[2] > row[0] else -1
                y_diff = 1 if row[3] > row[1] else -1

                ocean_map[
                    (row[0] + (i * x_diff), row[1] + (i * y_diff))
                ] += 1  # type:ignore

print(f"winning_answer: {len(dict(filter(lambda x: x[1] > 1, ocean_map.items())))}")
