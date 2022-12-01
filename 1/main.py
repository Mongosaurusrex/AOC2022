def day_one():
    elfs = []
    def setup():
        nonlocal elfs
        elfs = []
        with open("./input.txt") as f:
            lines = f.readlines()
            temp = []
            for line in lines:
                if line == "\n":
                    elfs.append(temp)
                    temp = []
                    continue

                temp.append(int(line.replace("\n","")))

    def solution():
        calories = []
        nonlocal elfs
        for elf in elfs:
            total_calories = 0
            for entry in elf:
                total_calories += entry
            calories.append(total_calories)

        calories.sort()
        top_calories = calories[::-1]

        print(f"\tFirst solution: {top_calories[0]}")
        print(f"\tSecond solution: {top_calories[0] + top_calories[1] + top_calories[2]}")

    setup()
    print("Day one")
    solution()

if __name__ == "__main__":
    day_one()
