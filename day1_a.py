def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = list(map(str.strip, lines))

    return lines

def find_number(line):
    number = 0
    for i in range(len(line)):
        if line[i].isdigit():
            number = int(line[i]) * 10
            break
    for i in range(len(line) -1, -1, -1):
        if line[i].isdigit():
            number += int(line[i])
            break
    return number

file_path = 'data/day1.txt'

lines = parse_data(file_path)
count = sum(list(map(find_number, lines)))
print(count)
