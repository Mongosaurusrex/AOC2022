import re
from itertools import zip_longest

def day_five():
    print("Day five")
    with open("./5/input.txt", "r") as f:
        crates, moves = f.read().split("\n\n")

        crates = crates.splitlines()[:-1]
        crates = [crate[1::4] for crate in crates]
        crates = [*zip_longest(*crates[::-1], fillvalue=" ")]
        crates = [[e for e in crate if not e.isspace()] for crate in crates]

        moves = re.findall(r"move (\d+) from (\d+) to (\d+)", moves)
        moves = [map(int, move) for move in moves]
        moves = [[amt, from_ - 1, to - 1] for amt, from_, to in moves]

    crate_mover_9000 = [crate[:] for crate in crates]
    crate_mover_9001 = [crate[:] for crate in crates]

    
    for amt, from_, to in moves:
        crate_mover_9000[to] += crate_mover_9000[from_][:-amt - 1:-1]
        del crate_mover_9000[from_][-amt:]

        crate_mover_9001[to] += crate_mover_9001[from_][-amt:]
        del crate_mover_9001[from_][-amt:]

    print("\tFirst solution: " + "".join(crate[-1] for crate in crate_mover_9000))
    print("\tSecond solution: " + "".join(crate[-1] for crate in crate_mover_9001))

if __name__ == "__main__":
    day_five()
