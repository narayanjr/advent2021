increases = 0

with open("Day1p1Data.txt") as f:
    line = f.readline()
    c_val = int(line)

    while line:
        line = f.readline()

        if line != "":
            if int(line) > c_val:
                increases += 1
                print(f"C: {c_val}  Inc: {increases}  Line: {line}")
            c_val = int(line)

print(increases)
