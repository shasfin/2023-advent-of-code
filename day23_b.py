def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def get_neighbors(field, data):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = len(data)
    m = len(data[0])
    i, j = field
    neighbors = [(i + direction[0], j + direction[1]) for direction in dirs]

    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and data[neighbor[0]][neighbor[1]] != '#']


def bfs(start, data):
    n = len(data)
    m = len(data[0])
    visited = [[-2 if data[i][j] == '#' else -1 for j in range(m)] for i in range(n)]
    visited[start[0]][start[1]] = 0
    queue = [start]

    while queue != []:
        current = queue.pop(0)
        neighbors = get_neighbors(current, data)
        for neighbor in neighbors:
            if visited[neighbor[0]][neighbor[1]] == -1:
                queue.append(neighbor)
                visited[neighbor[0]][neighbor[1]] = visited[current[0]][current[1]] + 1
        if len(neighbors) > 2:
            print(f"There were {len(neighbors)} neighbors for {current}: {neighbors}")

    return visited


def longest_path(start, end, data):
    steps = 0

    stack = [(start, {start})]
    while stack != []:
        current, visited = stack.pop()
        if current == end:
            steps = max(steps, len(visited))
        for neighbor in get_neighbors(current, data):
            if neighbor not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbor)
                stack.append((neighbor, new_visited))
    return steps

file_path = 'data/day23.txt'
data = parse_data(file_path)
# print(longest_path((0, 1), (7, 5), data) - 1)
print(longest_path((0, 1), (140, 139), data) - 1)
# print(longest_path((0, 1), (22, 21), data) - 1)
# print(bfs((0,1), data)[140][139])