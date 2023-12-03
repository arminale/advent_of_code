CUBES = {"blue": 14, "green": 13, "red": 12}


def get_game_id(game):
    return int(game[5 : game.find(":")])


def is_possible(game):
    hands = game[game.find(":") + 1 :]
    for hand in hands.strip().split(";"):
        for num_colour in hand.strip().split(","):
            num, colour = num_colour.strip().split(" ")
            if int(num) > CUBES[colour]:
                return False

    return True


def main():
    with open("input.txt") as f:
        sum_ids = sum([get_game_id(game) for game in f if is_possible(game)])
    print(sum_ids)


if __name__ == "__main__":
    main()
