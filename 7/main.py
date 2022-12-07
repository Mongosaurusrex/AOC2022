def day_seven():
    file_system = { "/": dict() }
    pwd = []

    def setup():
        nonlocal file_system, pwd
        def get_directory(file_system, pwd):
            if not pwd:
                return file_system
            return get_directory(file_system[pwd[0]], pwd[1:])
            

        with open("./7/input.txt") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "$ ls":
                    continue
                working_directory = get_directory(file_system, pwd)
                if line[:3] == "dir":
                    working_directory[line[4:]] = dict()
                elif ".." in line:
                    pwd = pwd[:-1]
                elif "$ cd" in line:
                    pwd.append(line[5:])
                else:
                    size, name = line.split()
                    working_directory [name] = int(size)
    sizes = []
    def du(d):
        if type(d) == int: return d
        size = sum([du(d[k]) for k in d])
        sizes.append(size)
        return size

    setup()

    req = 30000000 - (70000000 - du(file_system))
    r1 = 0
    r2 = 70000000
    for size in sizes:
        if size < 100000: r1 += size
        if size > req: r2 = min(r2, size)

    print(f"\tSolution one: {r1}")
    print(f"\tSolution two: {r2}")


if __name__ == "__main__":
    day_seven()
