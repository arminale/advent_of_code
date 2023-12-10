import math


def read_graph(f):
    graph = {}
    for line in f:
        source, dests = line.strip().split("=")
        graph[source.strip()] = (dests.strip()[1:4], dests.strip()[6:9])

    return graph


def parse_instruction(line: str) -> list[int]:
    instructions = {"L": 0, "R": 1}
    return [instructions[char] for char in line.strip()]


def all_end_with(char: str, nodes: list[str]) -> bool:
    for node in nodes:
        if not node.endswith(char):
            return False
    return True


def main():
    with open("input.txt") as f:
        instructions = parse_instruction(f.readline())
        f.readline()
        graph = read_graph(f)

    curr_nodes = [node for node in graph.keys() if node.endswith("A")]
    steps_to_end = []
    step_count = 0
    i = 0
    while curr_nodes != []:
        new_nodes = [graph[node][instructions[i]] for node in curr_nodes]
        step_count += 1
        i = (i + 1) % len(instructions)

        curr_nodes = [node for node in new_nodes if not node.endswith("Z")]
        if len(curr_nodes) != len(new_nodes):
            steps_to_end.append(step_count)

    print(math.lcm(*steps_to_end))


if __name__ == "__main__":
    main()
