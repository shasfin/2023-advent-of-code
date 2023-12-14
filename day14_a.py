def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = list(map(str.strip, file.readlines()))
    return data

def update(accumulator, row, character):
    (val, acc) = accumulator
    if character == '.':
        return val, acc
    elif character == '#':
        return row - 1, acc
    elif character == 'O':
        return val - 1, acc + val

def solve(data):
    data_len = len(data)
    accumulator = [(len(data), 0) for _ in data[0]]
    for index, stones in enumerate(data):
        accumulator = [update(acc, data_len - index, stone) for acc, stone in zip(accumulator, stones)]

    return sum(acc for val, acc in accumulator)

file_path = 'data/day14.txt'
data = parse_data(file_path)
print(solve(data))

