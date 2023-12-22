def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    return data


def find(c, data):
    for i, row in enumerate(data):
        try:
            j = row.index(c)
            return i, j
        except ValueError:
            pass
    return None


def transform(data, cycle):
    trans_dict = {
        '|': (-1,  0, -1,  0),
        '-': (-1, -1,  0,  0),
        'L': (-1, -1,  0,  0),
        'J': (-1,  0,  0,  0),
        '7': (-1,  0, -1,  0),
        'F': (-1, -1, -1,  0),
        'S': (-1,  0, -1,  0) # this information was visually obtained from the puzzle input
    }

    transformed = [[0, 0] * len(data[0]) for _ in range(2 * len(data))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            transformed[2*i][2*j] = 1

    for item in cycle:
        (i, j, dir) = item
        trans_vals = trans_dict[data[i][j]]
        transformed[2 * i][2 * j:2 * j + 2] = [trans_vals[0], trans_vals[1]]
        transformed[2 * i + 1][2 * j:2 * j + 2] = [trans_vals[2], trans_vals[3]]

    return transformed


def flood(transformed, start):
    queue = [start]
    count = 0

    while queue:
        i, j = queue.pop(0)

        for ii in range(max(0, i - 1), min(len(transformed), i + 2)):
            for jj in range(max(0, j - 1), min(len(transformed[0]), j + 2)):
                if transformed[ii][jj] != -1:
                    queue.append((ii, jj))
                    count += transformed[ii][jj]
                    transformed[ii][jj] = -1

    return count


def follow_cycle(start, data):
    next_dict = {
        ('|', 'a'): ( 1,  0, 'a'), ('|', 'b'): (-1,  0, 'b'),
        ('-', 'l'): ( 0,  1, 'l'), ('-', 'r'): ( 0, -1, 'r'),
        ('L', 'a'): ( 0,  1, 'l'), ('L', 'r'): (-1,  0, 'b'),
        ('J', 'a'): ( 0, -1, 'r'), ('J', 'l'): (-1,  0, 'b'),
        ('7', 'l'): ( 1,  0, 'a'), ('7', 'b'): ( 0, -1, 'r'),
        ('F', 'b'): ( 0,  1, 'l'), ('F', 'r'): ( 1,  0, 'a'),
        ('S', 'a'): ( 1,  0, 'a') # this information was visually obtained from the puzzle input
    }

    (s_i, s_j) = start
    cycle = [(s_i, s_j, 'a')]
    next = (s_i + 1, s_j, 'a')
    while next[0] != start[0] or next[1] != start[1]:
        cycle.append(next)
        (i, j, dir) = cycle[-1]
        next_differences = next_dict[(data[i][j], dir)]
        # Assuming pipes in the cycle never lead you outside the grid
        next = (i + next_differences[0], j + next_differences[1], next_differences[2])
    return cycle

file_path = 'data/day10.txt'
data = parse_data(file_path)
start = find('S', data)
cycle = follow_cycle(start, data)
transformed = transform(data, cycle)
print(flood(transformed, (start[0] + 1, start[1] - 1))) # this information was visually obtained from the puzzle input