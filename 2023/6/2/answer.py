import math


def main():
    t = 61709066
    d = 643118413621041

    lower = int(math.ceil((t - math.sqrt(t**2 - 4 * d)) / 2))
    upper = int(math.floor((t + math.sqrt(t**2 - 4 * d)) / 2))
    result = upper - lower + 1

    print(result)


if __name__ == "__main__":
    main()
