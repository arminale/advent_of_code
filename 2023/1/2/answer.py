from enum import Enum

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class ScanDirection(Enum):
    LEFT_TO_RIGHT, RIGHT_TO_LEFT = range(2)


def get_first_digit(s: str, scan_dir: ScanDirection) -> int:
    first_numerical_digit_index, first_numerical_digit = float("inf"), None
    first_spelled_digit_index, first_spelled_digit = float("inf"), None

    for index, c in enumerate(s):
        if c.isdigit():
            first_numerical_digit_index, first_numerical_digit = index, int(c)
            break

    for spelled_digit in DIGITS.keys():
        i = (
            s.find(spelled_digit)
            if scan_dir == ScanDirection.LEFT_TO_RIGHT
            else s.find(spelled_digit[::-1])
        )
        if i != -1:
            if first_spelled_digit_index > i:
                first_spelled_digit_index = i
                first_spelled_digit = DIGITS[spelled_digit]

    return (
        first_numerical_digit
        if first_numerical_digit_index < first_spelled_digit_index
        else first_spelled_digit
    )


def main():
    calibration_sum = 0
    with open("input.txt") as f:
        for line in f:
            calibration_sum += int(
                f"{get_first_digit(line, ScanDirection.LEFT_TO_RIGHT)}"
                f"{get_first_digit(line[::-1], ScanDirection.RIGHT_TO_LEFT)}"
            )

    print(calibration_sum)


if __name__ == "__main__":
    main()
