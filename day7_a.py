from functools import cmp_to_key

order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
powers = [len(order) ** i for i in range(5 - 1, -1, -1)]

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(' ') for line in file]
        data = [(cards, int(bid)) for (cards, bid) in data]
    return data


def get_kind(cards):
    # 0: High card
    # 1: One pair
    # 2: Two pair
    # 3: Three of a kind
    # 4: Full house
    # 5: Four of a kind
    # 6: Five of a kind
    counts = {}
    for card in cards:
        counts.setdefault(card, 0)
        counts[card] += 1
    n = len(counts.keys())
    if n == 1:
        return 6 # Five of a kind
    if n == 2:
        if 4 in counts.values():
            return 5 # Four of a kind
        else:
            return 4 # Full house
    if n == 3:
        if 3 in counts.values():
            return 3 # Three of a kind
        else:
            return 2 # Two pair
    if n == 4:
        return 1 # One pair
    return 0 # High card


def val(cards):

    dict = {c: o for (o, c) in enumerate(order)}
    return sum(dict[card] * pow for (card, pow) in zip(cards, powers))


def weaker(hand1, hand2):
    kind1, cards1, bid1 = hand1
    kind2, cards2, bid2 = hand2
    if kind1 == kind2 and cards1 == cards2:
        return 0
    if kind1 < kind2:
        return -1
    if kind1 == kind2:
        return val(cards1) - val(cards2)
    return 1


file_path = 'data/day7.txt'
data = parse_data(file_path)
data = [(get_kind(cards), cards, bid) for cards, bid in data]
data.sort(key=cmp_to_key(weaker))
print(data)
# for i in range(len(data) - 1):
#     print(f"weaker({data[i]}, {data[i+1]}) = {weaker(data[i], data[i+1])}; Values: {val(data[i][1])=}, {val(data[i+1][1])=}")
# print(list(enumerate(data)))
print(sum((rank + 1) * bid for rank, (kind, cards, bid) in enumerate(data)))
# print(1*765 + 2 * 220 + 3 * 28 + 4 * 684 + 5 * 483)