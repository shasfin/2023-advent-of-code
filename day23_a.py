def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def get_neighbors(field, data):
    dirs = {'>': [(0, 1)], '<': [(0, -1)], '^': [(-1, 0)], 'v': [(1, 0)], '.': [(1, 0), (0, 1), (-1, 0), (0, -1)], '#': []}
    n = len(data)
    m = len(data[0])
    i, j = field
    neighbors = [(i + direction[0], j + direction[1]) for direction in dirs[data[i][j]]]

    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m]


def longest_path(start, end, data):
    steps = 0

    stack = [(start, [start])]
    while stack != []:
        current, visited = stack.pop()
        if current == end:
            steps = max(steps, len(visited))
        for neighbor in get_neighbors(current, data):
            if neighbor not in visited:
                new_visited = visited.copy()
                new_visited.append(neighbor)
                stack.append((neighbor, new_visited))
    return steps

file_path = 'data/day23.txt'
data = parse_data(file_path)
print(longest_path((0, 1), (140, 139), data)-1)