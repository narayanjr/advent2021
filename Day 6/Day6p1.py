def tick_fish(time: int):
    if time == 0:
        return 6, 8
    else:
        return time - 1, None


with open("Day 6/data.txt") as f:
    fishes = [line.split(",") for line in f.readlines()][0]
    fishes = list(map(int, fishes))

    for day in range(80):
        for index in range(len(fishes)):
            fishes[index], new_fish = tick_fish(fishes[index])
            if new_fish is not None:
                fishes.append(8)


print(f"winning_answer: {len(fishes)}")
