def day_four():
    section_pairs = []
    print("Day four")

    def setup():
        nonlocal section_pairs
        with open("./4/input.txt") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                first, second = line.split(",")
                section_pairs.append((first, second))

    def part_one():
        total_overlaps = 0
        for l, r in section_pairs:
            l1, l2 = l.split("-")
            r1, r2 = r.split("-")

            if int(l1) <= int(r1) and int(l2) >= int(r2):
                total_overlaps += 1
            elif int(r1) <= int(l1) and int(r2) >= int(l2):
                total_overlaps += 1

        print(f"\tFirst solution: {total_overlaps}")

    def part_two():
        total_overlaps = 0
        for l, r in section_pairs:
            l1, l2 = l.split("-")
            r1, r2 = r.split("-")

            l_set = set([*range(int(l1), int(l2) + 1)])
            r_set = set([*range(int(r1), int(r2) + 1)])

            total_overlaps += 1 if (l_set & r_set) else 0

        print(f"\tSecond solution: {total_overlaps}")

    setup()
    part_one()
    part_two()


if __name__ == "__main__":
    day_four()
