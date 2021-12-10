with open("Day 9/data.txt") as f:
    rows = [list(line.strip()) for line in f.readlines()]

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

print(f"winning_answer: {sum(low_points.values()) + len(low_points)}")
