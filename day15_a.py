def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(',') for line in file]
    return data[0]


def run_hash_alg(s):
    acc = 0
    for c in s:
        acc += ord(c)
        acc *= 17
        acc %= 256
    return acc


file_path = 'data/day15.txt'
data = parse_data(file_path)
result = sum(run_hash_alg(s) for s in data)
print(result)