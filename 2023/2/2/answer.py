from functools import reduce
from operator import mul


def get_min_cubes(game):
    min_cubes = {"blue": 0, "green": 0, "red": 0}
    hands = game[game.find(":") + 1 :]

    for hand in hands.strip().split(";"):
        for num_colour in hand.strip().split(","):
            num, colour = num_colour.strip().split(" ")
            min_cubes[colour] = max(min_cubes[colour], int(num))

    return min_cubes


def main():
    with open("input.txt") as f:
        sum_ids = sum([reduce(mul, get_min_cubes(game).values()) for game in f])
    print(sum_ids)


if __name__ == "__main__":
    main()
