with open("Day 8/data.txt") as f:
    rows = [
        [line.split(" | ")[0].split(), line.split(" | ")[1].split()]
        for line in f.readlines()
    ]
# row[0] = input
# row[1] = output

output_segment_lens = [len(segment) for row in rows for segment in row[1]]
filtered = list(filter(lambda x: x in [2, 3, 4, 7], output_segment_lens))

print(f"winning_answer: {len(filtered)}")
