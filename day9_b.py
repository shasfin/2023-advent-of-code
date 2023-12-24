def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.strip().split(' '))) for line in file]
    return data


def predict(values):
    values.reverse()
    sequences = [values.copy()]
    while not all(map(lambda x: x == 0, sequences[-1])):
        last_sequence = sequences[-1]
        sequences.append(list(last_sequence[i+1] - last_sequence[i] for i in range(len(last_sequence) - 1)))

    last_sequence = sequences[-1]
    last_sequence.append(0)
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])
    return sequences[0][-1]

file_path = 'data/day9.txt'
data = parse_data(file_path)
print(sum(predict(values) for values in data))