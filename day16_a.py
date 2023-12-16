def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = list(map(str.strip, file.readlines()))
    return data


def get_neighbors(val, i, j, c, n, m):
    neighbors = []
    if c == 'l':
        if (val == '.' or val == '-') and j + 1 < m:
            neighbors.append((i, j + 1, c))
        elif val == '|':
            if i + 1 < n:
                neighbors.append((i + 1, j, 'a'))
            if i - 1 >= 0:
                neighbors.append((i - 1, j, 'b'))
        elif val == '/' and i - 1 >= 0:
            neighbors.append((i - 1, j, 'b'))
        elif val == '\\' and i + 1 < n:
            neighbors.append((i + 1, j, 'a'))
    elif c == 'r':
        if (val == '.' or val == '-') and j - 1 >= 0:
            neighbors.append((i, j - 1, c))
        elif val == '|':
            if i + 1 < n:
                neighbors.append((i + 1, j, 'a'))
            if i - 1 >= 0:
                neighbors.append((i - 1, j, 'b'))
        elif val == '/' and i + 1 < n:
            neighbors.append((i + 1, j, 'a'))
        elif val == '\\' and i - 1 >= 0:
            neighbors.append((i - 1, j, 'b'))
    elif c == 'a':
        if (val == '.' or val == '|') and i + 1 < n:
            neighbors.append((i + 1, j, c))
        elif val == '-':
            if j + 1 < m:
                neighbors.append((i, j + 1, 'l'))
            if j - 1 >= 0:
                neighbors.append((i, j - 1, 'r'))
        elif val == '/' and j - 1 >= 0:
            neighbors.append((i, j - 1, 'r'))
        elif val == '\\' and j + 1 < m:
            neighbors.append((i, j + 1, 'l'))
    elif c == 'b':
        if (val == '.' or val == '|') and i - 1 >= 0:
            neighbors.append((i - 1, j, c))
        elif val == '-':
            if j + 1 < m:
                neighbors.append((i, j + 1, 'l'))
            if j - 1 >= 0:
                neighbors.append((i, j - 1, 'r'))
        elif val == '/' and j + 1 < m:
            neighbors.append((i, j + 1, 'l'))
        elif val == '\\' and j - 1 >= 0:
            neighbors.append((i, j - 1, 'r'))

    return neighbors


def is_visited(val, i, j, c, visited):
    if c in visited:
        return True
    if (c == 'l' or c == 'r') and data[i][j] == '|':
        return ('r' in visited) or ('l' in visited)
    if (c == 'a' or c == 'b') and data[i][j] == '-':
        return ('a' in visited) or ('b' in visited)
    else:
        return False


def bfs(data, config):
    n = len(data)
    m = len(data[0])
    queue = [config]
    # visited is a dictionary with tuples of indices as the key and a list of characters (l, r, a or b) as the value
    # visited from the left: l, visited from above: a, visited from the right: r, visited from below: b
    visited = {}
    while not queue == []:
        (i, j, c) = queue.pop(0)
        visited.setdefault((i, j), [])
        if not is_visited(data[i][j], i, j, c, visited[(i, j)]):
            visited[(i, j)].append(c)
            neighbors = get_neighbors(data[i][j], i, j, c, n, m)
            queue.extend(neighbors)
    return len(visited)


file_path = 'data/day16.txt'
data = parse_data(file_path)

n = len(data)
m = len(data[0])

initial_values = (
    [(0, j, 'a') for j in range(m)] +  # first row
    [(i, 0, 'l') for i in range(n)] +  # first column
    [(n - 1, j, 'b') for j in range(m)] +  # last row
    [(i, m - 1, 'l') for i in range(n)]     # last column
)

print(max(bfs(data, config) for config in initial_values))
