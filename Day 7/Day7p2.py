import statistics
from collections import Counter, defaultdict


# Its like factorial but addition
def triangle(i):
    return (i ** 2 + i) // 2


with open("Day 7/data.txt") as f:
    crabs = list(map(int, [line.split(",") for line in f.readlines()][0]))

counts = Counter(crabs)
sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

min_crab = min(crabs)
max_crab = max(crabs)

fuel_to_start = defaultdict(lambda: 0)

for x in range(min_crab, max_crab):
    fuel_to_start[x] = sum(  # type:ignore
        [triangle(abs(x - key)) * value for key, value in counts.items()]
    )
target_position = min(fuel_to_start, key=fuel_to_start.get)  # type:ignore
print(f"winning_answer: {fuel_to_start[target_position]} {target_position}")
