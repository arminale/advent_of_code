def get_first_digit(line: str) -> int:
    for c in line:
        if c.isdigit():
            return int(c)


def main():
    calibration_sum = 0
    with open("input.txt") as f:
        for line in f:
            calibration_sum += int(
                f"{get_first_digit(line)}{get_first_digit(reversed(line))}"
            )

    print(calibration_sum)


if __name__ == "__main__":
    main()
