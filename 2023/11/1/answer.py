import itertools
import functools


def main():
    galaxies = []
    rows_with_galaxies, cols_with_galaxies = set(), set()

    with open("input.txt") as f:
        for x, line in enumerate(f):
            for y, char in enumerate(line):
                if char == "#":
                    galaxies.append((x, y))
                    rows_with_galaxies.add(x)
                    cols_with_galaxies.add(y)

    empty_rows = set(range(galaxies[-1][0])).difference(rows_with_galaxies)
    empty_cols = set(range(max(x[1] for x in galaxies))).difference(cols_with_galaxies)

    @functools.lru_cache(maxsize=2048)
    def get_row_adjustment(x):
        adjust = 1 if x in empty_rows else 0
        if x > 0:
            adjust += get_row_adjustment(x - 1)
        return adjust

    @functools.lru_cache(maxsize=2048)
    def get_col_adjustment(y):
        adjust = 1 if y in empty_cols else 0
        if y > 0:
            adjust += get_col_adjustment(y - 1)
        return adjust

    sum_lengths = 0
    for dim, adj_func in zip(range(2), [get_row_adjustment, get_col_adjustment]):
        for g1, g2 in itertools.combinations(galaxies, 2):
            sum_lengths += abs(
                g1[dim] + adj_func(g1[dim]) - g2[dim] - adj_func(g2[dim])
            )

    print(sum_lengths)


if __name__ == "__main__":
    main()
