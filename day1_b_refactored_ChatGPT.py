def parse_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_number(line, values):
    occurrences = [(line.find(num), line.rfind(num), values[num]) for num in values.keys() if line.find(num) != -1]
    min_idx, max_idx, value = min(occurrences, key=lambda x: x[0])
    return value * 10 + max(occurrences, key=lambda x: x[1])[2]

file_path = 'data/day1.txt'

values = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9
}

lines = parse_data(file_path)
count = sum(find_number(line, values) for line in lines)
print(count)
