import math

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

symbol_dict = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}

openers = {"[", "{", "(", "<"}

with open("Day 10/data.txt") as f:
    rows = [list(line.strip()) for line in f.readlines()]

error_scores = []

for row in rows:
    characters = list(row)
    stack = []
    row_error_score = 0
    is_corrupt = False
    for character in characters:
        if character in openers:
            stack.append(symbol_dict[character])
        else:
            popped = stack.pop()
            if character != popped:
                is_corrupt = True
                break

    if not is_corrupt:
        while stack:
            row_error_score = row_error_score * 5 + scores[stack.pop()]
        error_scores.append(row_error_score)

error_scores.sort()

print(f"winning_answer: {error_scores[math.floor(len(error_scores)/2)]}")
