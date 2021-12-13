def tick(octopi):
    return [[octopus + 1 for octopus in row] for row in octopi]


def reset_flashed(octopi):
    return [[octopus if octopus <= 9 else 0 for octopus in row] for row in octopi]


def flash_neighbors(octopi, r, c):
    if r > 0:
        octopi[r - 1][c] += 1  # 2

    if c > 0:
        octopi[r][c - 1] += 1  # 4

    if r > 0 and c > 0:
        octopi[r - 1][c - 1] += 1  # 1

    if r > 0 and c < 9:
        octopi[r - 1][c + 1] += 1  # 3

    if r < 9:
        octopi[r + 1][c] += 1  # 8
    if c < 9:
        octopi[r][c + 1] += 1  # 6

    if r < 9 and c < 9:
        octopi[r + 1][c + 1] += 1  # 9

    if r < 9 and c > 0:
        octopi[r + 1][c - 1] += 1  # 7

    return octopi


def flash(octopi, flashed_octopi):
    did_flash = False

    for r in range(0, 10):
        for c in range(0, 10):
            if octopi[r][c] > 9 and (r, c) not in flashed_octopi:
                flashed_octopi.add((r, c))
                octopi = flash_neighbors(octopi, r, c)
                did_flash = True

    if did_flash:
        octopi, flashed_octopi = flash(octopi, flashed_octopi)

    return octopi, flashed_octopi


with open("Day 11/data.txt") as f:
    octopi = [list(map(int, list(line.strip()))) for line in f.readlines()]


total_flashed = 0
for step in range(0, 100):
    octopi = tick(octopi)
    octopi, flashed_octopi = flash(octopi, set())
    total_flashed += len(flashed_octopi)
    octopi = reset_flashed(octopi)


print(f"winning_answer: {total_flashed}")
