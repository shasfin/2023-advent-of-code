def pprint(table):
    for row in table:
        print(" ".join("{:3d}".format(cell) for cell in row))
    print('-------------------------------------------')

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data

def find_S(data):
    for i in range(len(data)):
        j = data[i].find('S')
        if j != -1:
            return (i, j)


def bfs(start, max_steps, data):
    n = len(data)
    m = len(data[0])

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    count = 0
    visited = [[-1 if data[i][j] == '#' else 0 for j in range(m)] for i in range(n)]
    queue = [start]
    while queue != []:
        i, j = queue.pop(0)
        if visited[i][j] == max_steps:
            break
        for neighbor in neighbors:
            ii, jj = i + neighbor[0], j + neighbor[1]
            if 0 <= ii < n and 0 <= jj < m:
                if -1 < visited[ii][jj] < visited[i][j] + 1:
                    if visited[i][j] + 1 == max_steps:
                        count += 1
                    queue.append((ii, jj))
                    visited[ii][jj] = visited[i][j] + 1
    return count


file_path = 'data/day21.txt'
data = parse_data(file_path)
S_coordinates = find_S(data)
print(bfs(S_coordinates, 64, data))