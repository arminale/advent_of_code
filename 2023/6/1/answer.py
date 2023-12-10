import math


def main():
    result = 1
    for t, d in [(61, 643), (70, 1184), (90, 1362), (66, 1041)]:
        lower = int(math.ceil((t - math.sqrt(t**2 - 4 * d)) / 2))
        upper = int(math.floor((t + math.sqrt(t**2 - 4 * d)) / 2))
        result *= upper - lower + 1

    print(result)


if __name__ == "__main__":
    main()
