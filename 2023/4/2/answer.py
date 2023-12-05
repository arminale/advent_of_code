from collections import defaultdict


def main():
    with open("input.txt") as f:
        total_cards = 0
        cards_copies = defaultdict(lambda: 1)
        for card in f:
            card_id = int(card[4 : card.find(":")].strip())
            winning_num_str, num_str = card.strip().split(":")[1].strip().split("|")

            winning_nums = set(winning_num_str.strip().split())
            nums = set(num_str.strip().split())
            hits = len(winning_nums & nums)

            curr_card_copies = cards_copies[card_id]
            total_cards += cards_copies[card_id]
            if hits > 0:
                for i in range(1, 1 + hits):
                    cards_copies[card_id + i] += curr_card_copies

        print(total_cards)


if __name__ == "__main__":
    main()
