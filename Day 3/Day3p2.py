from collections import defaultdict


def most_common_bit(count, total):
    return "1" if count / total >= 0.5 else "0"


def least_common_bit(count, total):
    return "1" if count / total < 0.5 else "0"


def i_dont_know(lines, bit_num, common_bit_function) -> int:
    total = len(lines)
    one_bit_count = 0

    for line in lines:
        one_bit_count = one_bit_count + int(line[bit_num])

    common_bit = common_bit_function(one_bit_count, total)

    filtered = [line for line in lines if line[bit_num] == common_bit]
    if len(filtered) != 1:
        bit_num += 1
        return i_dont_know(filtered, bit_num, common_bit_function)
    else:
        return int("".join(filtered[0]), 2)


total = 0
with open("Day 3/data.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    o2_rating = i_dont_know(lines, 0, most_common_bit)
    scrub_rating = i_dont_know(lines, 0, least_common_bit)

    print(f"o2_rating: {o2_rating}")
    print(f"scrub_rating: {scrub_rating}")

    print(f"Answer: {o2_rating * scrub_rating}")
