from functools import cmp_to_key

order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
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
    js = 0
    for card in cards:
        if card != 'J':
            counts.setdefault(card, 0)
            counts[card] += 1
        else:
            js += 1
    max_count = max(counts.values()) if len(counts.values()) > 0 else 0
    print(f"For {cards=} there are {js=} and {max_count=}")
    if max_count + js == 5:
        return 6 # Five of a kind
    if max_count + js == 4:
        return 5 # Four of a kind
    if max_count + js == 3:
        if len(counts.keys()) == 2:
            return 4 # Full house
        else:
            return 3 # Three of a kind
    if max_count + js == 2:
        if len(counts.keys()) == 3:
            return 2 # Two pair
        else:
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