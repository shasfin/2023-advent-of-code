def parse_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_number(line):
    numbers = [int(char) for char in line if char.isdigit()]
    return 10 * numbers[0] + numbers[-1]

file_path = 'data/day1.txt'

lines = parse_data(file_path)
count = sum(map(find_number, lines))
print(count)
