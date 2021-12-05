directions = {
    "forward": 0,
    "up": 0,
    "down": 0,
}
with open("Day 2/data.txt") as f:
    lines = [line.split() for line in f.readlines()]

    for direction, amount in lines:
        directions[direction] += int(amount)

depth = directions["down"] - directions["up"]
print(f"depth: {depth}  Horizontal: {directions['forward']}")
print(f"Answer: {depth * directions['forward']}")
