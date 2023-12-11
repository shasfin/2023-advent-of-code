data = []

with open('data/day4.txt') as readfile:
    for line in readfile:
        if line[-1] == '\n':
            data.append(line[:-1])
        else:
            data.append(line)

cards = [s.split(':') for s in data]
cards = [c[1] for c in cards]
cards = [s.split('|') for s in cards]
cards = [[s.strip(' ').replace('  ', ' ').split(' ') for s in c] for c in cards]
cards = [[[int(i) for i in s] for s in c] for c in cards]

# print(cards)

total_sum = 0
for [winning, mine] in cards:
    print(f"{winning=}")
    print(f"{mine=}")
    num_intersect = 0
    for w in winning:
        if w in mine:
            num_intersect += 1
    print(num_intersect)
    if num_intersect > 0:
        total_sum += 2**(num_intersect-1)
    print(total_sum)

print(total_sum)