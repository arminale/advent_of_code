def is_symbol(x: str) -> bool:
    return not (x.isalnum() or x == ".")


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


def is_adjacent_across_rows(num: tuple[int, int, int], symbols: set[int]) -> bool:
    num_start, num_end, _ = num
    for i in range(num_start - 1, num_end + 2):
        if i in symbols:
            return True

    return False


def is_adjacent_in_row(num: tuple[int, int, int], symbols: set[int]) -> bool:
    num_start, num_end, _ = num
    return num_start - 1 in symbols or num_end + 1 in symbols


def main():
    part_number_sum = 0
    with open("input.txt") as f:
        prev_symbols = set()
        prev_unresolved_nums = []
        for row in f:
            current_symbols = {
                i for i, char in enumerate(row.strip()) if is_symbol(char)
            }
            current_nums = extract_numbers(row.strip())

            part_number_sum += sum(
                num[2]
                for num in prev_unresolved_nums
                if is_adjacent_across_rows(num, current_symbols)
            )

            part_number_sum += sum(
                num[2]
                for num in current_nums
                if is_adjacent_across_rows(num, prev_symbols)
            )

            # Avoid double counting any already resolved numbers in the current row
            current_nums = [
                num
                for num in current_nums
                if not is_adjacent_across_rows(num, prev_symbols)
            ]
            prev_unresolved_nums.clear()
            prev_symbols.clear()

            for num in current_nums:
                if is_adjacent_in_row(num, current_symbols):
                    part_number_sum += num[2]
                else:
                    prev_unresolved_nums.append(num)

            prev_symbols = set(current_symbols)

    print(part_number_sum)


if __name__ == "__main__":
    main()
