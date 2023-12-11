def parse_line(line):
    card_number, numbers = line.split(":")
    current_card = [int(card_number.split()[1]), [], []]
    current_card[1] = list(map(int, numbers.split("|")[0].split()))
    current_card[2] = list(map(int, numbers.split("|")[1].split()))
    return current_card


def count_matches(winning, mine):
    num_intersect = 0
    for w in winning:
        if w in mine:
            num_intersect += 1
            print(w)
    return num_intersect


data = []

with open('data/day4.txt') as readfile:
    for line in readfile:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)

cards = [parse_line(s) for s in data]

print(cards)

counts = [1 for _ in cards]
for [number, winning, mine] in cards:
    matches = count_matches(winning, mine)
    print(f"{number=}, {winning=}, {mine=}, {matches=}")
    for i in range(matches): #card numbers start with 1, not with 0
        counts[number+i] += counts[number-1]

print(sum(counts))