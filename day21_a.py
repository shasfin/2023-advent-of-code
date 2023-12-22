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
    count = 0
    n = len(data)
    m = len(data[0])
    queue = [(start[0], start[1], 0)]
    visited = [[0]*m for _ in range(n)]
    while queue != []:
        i, j, steps = queue.pop(0)
        if steps % 5 == 0:
            print(f"{i=}, {j=}, {steps=}")
        if steps == max_steps:
            count += 1
        if steps > max_steps:
            break
        for ii in range(max(i - 1, 0), min(i + 1, n - 1) + 1):
            for jj in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                if data[ii][jj] == '.':
                    if not visited[ii][jj] == steps + 1:
                    #     count += 1
                        visited[ii][jj] = steps + 1
                        queue.append((ii, jj, steps + 1))
    return count



file_path = 'data/day21.txt'
data = parse_data(file_path)
S_coordinates = find_S(data)
print(bfs(S_coordinates, 64, data))