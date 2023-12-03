def is_gear(x: str) -> bool:
    return x == "*"


def extract_numbers(row: str) -> list[tuple[int, int, int]]:
    numbers = []
    i = 0
    while i < len(row):
        if row[i].isdigit():
            start = i
            i += 1
            while i < len(row) and row[i].isdigit():
                i += 1
            end = i
            numbers.append((start, end - 1, int(row[start:end])))

        i += 1

    return numbers


def get_adjacent_nums_across_rows(
    gear: int, nums: list[tuple[int, int, int]]
) -> list[int]:
    return [val for start, end, val in nums if start - 1 <= gear <= end + 1]


def get_adjacent_nums_in_row(gear: int, nums: list[tuple[int, int, int]]) -> list[int]:
    return [val for start, end, val in nums if start - 1 == gear or end + 1 == gear]


def main():
    gears = {}
    with open("input.txt") as f:
        prev_nums = []
        for line, row in enumerate(f):
            gears[line] = {i: [] for i, char in enumerate(row.strip()) if is_gear(char)}
            current_nums = extract_numbers(row.strip())

            for gear in gears[line].keys():
                # numbers from line n-1 with gears in row n
                gears[line][gear] += get_adjacent_nums_across_rows(gear, prev_nums)

                # numbers from line n with gears in row n
                gears[line][gear] += get_adjacent_nums_in_row(gear, current_nums)

            # numbers from line n with gears in row n-1
            if line > 0:
                for gear in gears[line - 1].keys():
                    gears[line - 1][gear] += get_adjacent_nums_across_rows(
                        gear, current_nums
                    )

            prev_nums = list(current_nums)

    gear_ratio_sum = 0
    for gear in gears.values():
        for adjacent_nums in gear.values():
            if len(adjacent_nums) == 2:
                gear_ratio_sum += adjacent_nums[0] * adjacent_nums[1]

    print(gear_ratio_sum)


if __name__ == "__main__":
    main()
