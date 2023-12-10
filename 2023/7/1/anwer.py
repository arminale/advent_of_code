from collections import Counter
from functools import cmp_to_key


def get_type(hand: str) -> int:
    counter = Counter(hand)
    first = counter.most_common(1)[0]
    if first[1] == 5:
        return 7

    second = counter.most_common(2)[1]
    if first[1] == 4:
        return 6
    elif first[1] == 3 and second[1] == 2:
        return 5
    elif first[1] == 3:
        return 4
    elif first[1] == second[1] == 2:
        return 3
    elif first[1] == 2:
        return 2

    return 1


def get_hand_value(hand: str) -> int:
    card_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_values = card_values | {str(x): x for x in range(2, 10)}
    value = 0
    for card in hand:
        value += card_values[card]
        value *= 100
    return value


def compare_hands(hand1: tuple[str, int], hand2: tuple[str, int]) -> int:
    type1 = get_type(hand1[0])
    type2 = get_type(hand2[0])
    if type1 == type2:
        val1 = get_hand_value(hand1[0])
        val2 = get_hand_value(hand2[0])
        return val1 - val2
    else:
        return type1 - type2


def read_games() -> list[tuple[str, int]]:
    with open("input.txt") as f:
        return [
            (line.strip().split()[0], int(line.strip().split()[1]))
            for line in f.readlines()
        ]


def main():
    hands = read_games()
    hands.sort(key=cmp_to_key(compare_hands))

    print(sum([x[1] * (i + 1) for i, x in enumerate(hands)]))


if __name__ == "__main__":
    main()
