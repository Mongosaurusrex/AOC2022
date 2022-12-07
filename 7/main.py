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

    def size_calculation():
        nonlocal file_system
        test = file_system["/"]
        import pdb
        pdb.set_trace()
        return 0
        # sum(file_system.values())

    setup()
    size_calculation()


if __name__ == "__main__":
    day_seven()
