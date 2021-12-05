increases = 0

with open("Day1p1Data.txt") as f:
    lines = [int(line) for line in f.readlines()]

    for x in range(0, len(lines) - 3):
        if (
            lines[x] + lines[x + 1] + lines[x + 2]
            < lines[x + 1] + lines[x + 2] + lines[x + 3]
        ):
            increases += 1

print(increases)
