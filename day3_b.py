def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip()+'.' for line in file]
    return data + ['.'*len(data[0])]


def find_numbers(data):
    numbers = {}
    for i, line in enumerate(data):
        num_start = -1
        for j, c in enumerate(line):
            if c.isdigit():
                if num_start == -1:
                    num_start = j
            else:
                if num_start >= 0:
                    numbers.setdefault(i, [])
                    numbers[i].append((num_start, j, int(line[num_start:j])))
                num_start = -1
    return numbers


file_path = 'data/day3.txt'
data = parse_data(file_path)
numbers = find_numbers(data)
n = len(data)
m = len(data[0])
sum = 0

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == '*':
            neighbors = 0
            gear_ratio = 1
            for ii in range(max(i - 1, 0), min(i + 1, n)+1):
                numbers_in_neighbor_lines = numbers.get(ii, [])
                for num_start, num_end, num in numbers_in_neighbor_lines:
                    if num_start-1 <= j < num_end + 1:
                        neighbors += 1
                        gear_ratio *= num
            if neighbors == 2:
                sum += gear_ratio


print(sum)


