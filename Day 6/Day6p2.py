fish_counts = {
    8: 0,
    7: 0,
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0,
}

with open("Day 6/data.txt") as f:
    fishes = [line.split(",") for line in f.readlines()][0]
    fishes = list(map(int, fishes))

    for fish in fishes:
        fish_counts[fish] += 1

    for day in range(256):
        fucked_fish = fish_counts[0]
        fish_counts[0] = fish_counts[1]
        fish_counts[1] = fish_counts[2]
        fish_counts[2] = fish_counts[3]
        fish_counts[3] = fish_counts[4]
        fish_counts[4] = fish_counts[5]
        fish_counts[5] = fish_counts[6]
        fish_counts[6] = fish_counts[7] + fucked_fish
        fish_counts[7] = fish_counts[8]
        fish_counts[8] = fucked_fish

    print(f"Aswner: {sum(fish_counts.values())}")
