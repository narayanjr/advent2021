import math


def get_low_points(rows):
    low_points = {}

    for rdx, row in enumerate(rows):
        for cdx, col in enumerate(row):
            is_smallest = True
            mid_row = ""

            if rdx > 0:
                is_smallest = col < rows[rdx - 1][cdx]
            if is_smallest and cdx > 0:
                is_smallest = col < rows[rdx][cdx - 1]
            if is_smallest and cdx < len(row) - 1:
                is_smallest = col < rows[rdx][cdx + 1]
            if is_smallest and rdx < len(rows) - 1:
                is_smallest = col < rows[rdx + 1][cdx]
            if is_smallest:
                low_points[(rdx, cdx)] = int(col)

    return low_points


def search(rows, x, y, x_max, y_max, basin_positions):
    cur_val = int(rows[x][y])
    if cur_val == 9:
        return basin_positions
    else:
        basin_positions.add((x, y))

        if x > 0 and (x - 1, y) not in basin_positions:
            basin_positions.update(
                search(rows, x - 1, y, x_max, y_max, basin_positions)
            )
        if x < x_max and (x + 1, y) not in basin_positions:
            basin_positions.update(
                search(rows, x + 1, y, x_max, y_max, basin_positions)
            )
        if y > 0 and (x, y - 1) not in basin_positions:
            basin_positions.update(
                search(rows, x, y - 1, x_max, y_max, basin_positions)
            )
        if y < y_max and (x, y + 1) not in basin_positions:
            basin_positions.update(
                search(rows, x, y + 1, x_max, y_max, basin_positions)
            )

        return basin_positions


with open("Day 9/data.txt") as f:
    rows = [list(line.strip()) for line in f.readlines()]
    low_points = get_low_points(rows)

basins = {}

for position, height in low_points.items():
    basin_positions = set()
    basins[position] = search(
        rows, position[0], position[1], len(rows) - 1, len(rows[0]) - 1, basin_positions
    )

basin_counts = []
for start, basin in basins.items():
    basin_counts.append(len(basin))

basin_counts.sort(reverse=True)
print(f"winning_answer: {math.prod(basin_counts[:3])}")
