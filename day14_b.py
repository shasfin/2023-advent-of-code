def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = list(map(lambda x: list(x.strip()), file.readlines()))
    return data


def go_north(data):
    rows = [0] * len(data[0])
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '.':
                pass
            elif data[i][j] == '#':
                rows[j] = i + 1
            elif data[i][j] == 'O':
                data[i][j] = '.'
                data[rows[j]][j] = 'O'
                rows[j] += 1
    return data


def go_west(data):
    cols = [0] * len(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '.':
                pass
            elif data[i][j] == '#':
                cols[i] = j + 1
            elif data[i][j] == 'O':
                data[i][j] = '.'
                data[i][cols[i]] = 'O'
                cols[i] += 1
    return data


def go_south(data):
    n = len(data) - 1
    rows = [n] * len(data[0])
    for i in range(len(data) - 1, -1, -1):
        for j in range(len(data[0]) - 1, -1, -1):
            if data[i][j] == '.':
                pass
            elif data[i][j] == '#':
                rows[j] = i - 1
            elif data[i][j] == 'O':
                data[i][j] = '.'
                data[rows[j]][j] = 'O'
                rows[j] -= 1
    return data


def go_east(data):
    n = len(data[0]) - 1
    cols = [n] * len(data)
    for i in range(len(data)):
        for j in range(len(data[0]) - 1, -1, -1):
            if data[i][j] == '.':
                pass
            elif data[i][j] == '#':
                cols[i] = j - 1
            elif data[i][j] == 'O':
                data[i][j] = '.'
                data[i][cols[i]] = 'O'
                cols[i] -= 1
    return data


def solve(data, N):
    memo = []
    data_hash = "".join("".join(row) for row in data)
    while data_hash not in memo:
        memo.append(data_hash)
        data = go_east(go_south(go_west(go_north(data))))
        data_hash = "".join("".join(row) for row in data)
    offset = memo.index(data_hash)
    cycle = len(memo) - offset
    index = offset + ((N - offset) % cycle)
    result = memo[index]
    n = len(data)
    return [result[i:i + n] for i in range(0, len(result), n)]


def compute_load(data):
    val = len(data)
    load = 0
    for row in data:
        load += sum(x.count('O')*val for x in row)
        val -= 1
    return load

file_path = 'data/day14.txt'
data = parse_data(file_path)
print(compute_load(solve(data, 1000000000)))
