def brute(inputs, outputs):
    patterns = {
        0: frozenset(),
        1: frozenset(),
        2: frozenset(),
        3: frozenset(),
        4: frozenset(),
        5: frozenset(),
        6: frozenset(),
        7: frozenset(),
        8: frozenset(),
        9: frozenset(),
    }
    # figure out what we can know
    for signal in filter(lambda x: len(x) in [2, 3, 4, 7], inputs + outputs):
        if len(signal) == 2:  # 1
            patterns[1] = frozenset(list(signal))
        elif len(signal) == 3:  # 7
            patterns[7] = frozenset(list(signal))
        elif len(signal) == 4:  # 4
            patterns[4] = frozenset(list(signal))
        elif len(signal) == 7:  # 8
            patterns[8] = frozenset(list(signal))

    # deduce what we can now
    for signal in filter(lambda x: len(x) in [0, 1, 5, 6, 8], inputs + outputs):
        if len(signal) == 5:  # 2/3/5
            if len(patterns[1].difference(set(list(signal)))) == 0:  # 3
                patterns[3] = frozenset(list(signal))
            elif len(patterns[4].difference(set(list(signal)))) == 1:  # 5
                patterns[5] = frozenset(list(signal))
            else:
                patterns[2] = frozenset(list(signal))  # 2
        elif len(signal) == 6:  # 0/6/9
            if len(patterns[4].difference(set(list(signal)))) == 0:  # 9
                patterns[9] = frozenset(list(signal))
            elif len(patterns[7].difference(set(list(signal)))) == 0:  # 0
                patterns[0] = frozenset(list(signal))
            else:
                patterns[6] = frozenset(list(signal))  # 6

    r_patterns = {v: k for k, v in patterns.items()}
    return int(
        "".join(map(str, [r_patterns[frozenset(list(digit))] for digit in outputs]))
    )


with open("Day 8/data.txt") as f:
    rows = [
        [line.split(" | ")[0].split(), line.split(" | ")[1].split()]
        for line in f.readlines()
    ]
# row[0] = input
# row[1] = output

outputs = [brute(row[0], row[1]) for row in rows]

print(f"winning_answer: {sum(outputs)}")
