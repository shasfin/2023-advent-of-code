def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    return data

def find(c, data):
    start = (0, 0)
    for i in range(len(data)):
        try:
            start = (i, data[i].index(c))
        except ValueError:
            pass
    return start

def follow_cycle(start, data):
    next_dict = {
        ('|', 'a'): ( 1,  0, 'a'), ('|', 'b'): (-1,  0, 'b'),
        ('-', 'l'): ( 0,  1, 'l'), ('-', 'r'): ( 0, -1, 'r'),
        ('L', 'a'): ( 0,  1, 'l'), ('L', 'r'): (-1,  0, 'b'),
        ('J', 'a'): ( 0, -1, 'r'), ('J', 'l'): (-1,  0, 'b'),
        ('7', 'l'): ( 1,  0, 'a'), ('7', 'b'): ( 0, -1, 'r'),
        ('F', 'b'): ( 0,  1, 'l'), ('F', 'r'): ( 1,  0, 'a'),
        ('S', 'a'): ( 1,  0, 'a')
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
print(len(follow_cycle(start, data)) // 2)