class RangesMap:
    def __init__(self):
        self.__source_ranges = []
        self.__dest_ranges = []

    def add_range(self, source_range, dest_range):
        self.__source_ranges.append(source_range)
        self.__dest_ranges.append(dest_range)

    def get_mapping(self, item):
        for i, r in enumerate(self.__source_ranges):
            if item in r:
                delta = item - r.start
                return self.__dest_ranges[i].start + delta

        return item


def get_next_map(f):
    header = f.readline()
    if header == "":
        raise EOFError

    print(f"Reading {header}")

    map = RangesMap()
    while True:
        row = f.readline()
        if row == "\n" or row == "":
            break

        dest_start, source_start, range_len = row.strip().split()
        source_range = range(int(source_start), int(source_start) + int(range_len))
        dest_range = range(int(dest_start), int(dest_start) + int(range_len))
        map.add_range(source_range, dest_range)

    return map


def main():
    with open("input.txt") as f:
        seeds = [int(x) for x in f.readline().split(":")[1].strip().split()]
        f.readline()

        while True:
            try:
                curr_map = get_next_map(f)
                seeds = [curr_map.get_mapping(seed) for seed in seeds]
            except EOFError:
                break

        print(min(seeds))


if __name__ == "__main__":
    main()
