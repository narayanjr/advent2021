horizontal = 0
depth = 0
aim = 0


def forward(x):
    global horizontal, depth
    horizontal += x
    depth += aim * x


def up(x):
    global aim
    aim -= x


def down(x):
    global aim
    aim += x


directions = {
    "forward": forward,
    "up": up,
    "down": down,
}


with open("Day 2/data.txt") as f:
    lines = [line.split() for line in f.readlines()]

    for direction, amount in lines:
        directions[direction](int(amount))

print(f"depth: {depth}  Horizontal: {horizontal}")
print(f"Answer: {depth * horizontal}")
