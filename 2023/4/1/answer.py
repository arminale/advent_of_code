def main():
    with open("input.txt") as f:
        points = 0
        for game in f:
            winning_num_str, num_str = game.strip().split(":")[1].strip().split("|")

            winning_nums = set(winning_num_str.strip().split())
            nums = set(num_str.strip().split())

            hits = len(winning_nums & nums)
            if hits > 0:
                points += 2 ** (hits - 1)

        print(points)


if __name__ == "__main__":
    main()
