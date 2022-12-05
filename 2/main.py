import pdb


def day_two():
    history = []
    print("Day two")

    def setup():
        nonlocal history
        with open("./2/input.txt") as f:
            lines = f.readlines()
            for line in lines:
                history.append(line.replace("\n", ""))

    def solution_1():
        nonlocal history

        shape_point = {
            "X": 1,  # Rock
            "Y": 2,  # Paper
            "Z": 3,  # Scissors
        }

        victory_shape = {
            "X": "C",  # Scissors
            "Y": "A",  # Rock
            "Z": "B",  # Paper
        }

        draw_shape = {
            "X": "A",
            "Y": "B",
            "Z": "C",
        }

        score = 0
        for game in history:
            opponent, player = tuple(game.split(" "))

            victory_score = 0

            if victory_shape[player] == opponent:
                victory_score = 6
            if draw_shape[player] == opponent:
                victory_score = 3

            score += shape_point[player] + victory_score

        print(f"\tFirst solution: {score}")

    def solution_2():
        nonlocal history

        victory_shape = {
            "C": 1,
            "A": 2,
            "B": 3,
        }

        draw_shape = {
            "A": 1,
            "B": 2,
            "C": 3,
        }

        loose_shape = {
            "A": 3,
            "B": 1,
            "C": 2,
        }

        def shape_response(shape, opponent):
            resolver = {
                "X": (0, loose_shape),  # Must loose
                "Y": (3, draw_shape),  # Must draw
                "Z": (6, victory_shape),  # Must win
            }

            point, shape_resolver = resolver[shape]

            return point + shape_resolver[opponent]

        score = 0
        for game in history:
            opponent, player = tuple(game.split(" "))
            score += shape_response(player, opponent)

        print(f"\tSecond solution: {score}")

    setup()
    solution_1()
    solution_2()


if __name__ == "__main__":
    day_two()
