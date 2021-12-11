scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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

total_error_score = 0

for row in rows:
    characters = list(row)
    stack = []
    row_error_score = 0
    for character in characters:
        if character in openers:
            stack.append(symbol_dict[character])
        else:
            popped = stack.pop()
            if character != popped:
                row_error_score = scores[character]
                break

    total_error_score += row_error_score


print(f"winning_answer: {total_error_score}")
