def day_eight():
    forest = []

    def setup():
        nonlocal forest
        with open("./8/input.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                forest.append([int(v) for v in line.strip()])

    def count_top_trees():
        nonlocal forest
        height, width = len(forest), len(forest[0])

        no_of_top_trees = 0
        for x in range(width):
            col = [forest[i][x] for i in range(height)]
            for y in range(height):
                row = forest[y]
                this = forest[y][x]
                no_of_top_trees += (
                    all(t < this for t in row[:x])
                    or all(t < this for t in row[x + 1:])
                    or all(t < this for t in col[:y])
                    or all(t < this for t in col[y + 1:])
                )

        return no_of_top_trees

    def high_score_tree():
        nonlocal forest
        height, width = len(forest), len(forest[0])

        high_score = 0
        for x in range(width):
            col = [forest[i][x] for i in range(height)]
            for y in range(height):
                row = forest[y]
                this = row[x]
                dist_l = next(
                    (d for d in range(1, x) if row[x - d] >= this), x)
                dist_r = next((d for d in range(1, width - x)
                              if row[x + d] >= this), width - x - 1)
                dist_u = next(
                    (d for d in range(1, y) if col[y - d] >= this), y)
                dist_d = next((d for d in range(1, height - y)
                               if col[y + d] >= this), height - y - 1)
                high_score = max(high_score, dist_l * dist_r * dist_u * dist_d)

        return high_score

    setup()
    print(f"\tFirst solution: {count_top_trees()}")
    print(f"\tSecond solution: {high_score_tree()}")


if __name__ == "__main__":
    day_eight()
