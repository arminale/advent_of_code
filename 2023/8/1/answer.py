def read_graph(f):
    graph = {}
    for line in f:
        source, dests = line.strip().split("=")
        graph[source.strip()] = (dests.strip()[1:4], dests.strip()[6:9])

    return graph


def parse_instruction(line: str) -> list[int]:
    instructions = {"L": 0, "R": 1}
    return [instructions[char] for char in line.strip()]


def main():
    with open("input.txt") as f:
        instructions = parse_instruction(f.readline())
        f.readline()
        graph = read_graph(f)

    curr_node = "AAA"
    step_count = 0
    i = 0
    while curr_node != "ZZZ":
        curr_node = graph[curr_node][instructions[i]]
        step_count += 1
        i = (i + 1) % len(instructions)

    print(step_count)


if __name__ == "__main__":
    main()
