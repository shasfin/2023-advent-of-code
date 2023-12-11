def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = list(map(str.strip, lines))

    return lines

def find_number(line, values):
    min, min_val = len(line), 0
    max, max_val = 0, 0
    for num in values.keys():
        idx = line.find(num)
        ridx = line.rfind(num)
        if idx != -1 and idx <= min:
            min = idx
            min_val = values[num]
        if ridx != -1 and ridx >= max:
            max = ridx
            max_val = values[num]
    return min_val * 10 + max_val

file_path = 'data/day1.txt'

values = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
          "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

lines = parse_data(file_path)
count = sum(list(map(lambda line: find_number(line, values), lines)))
print(count)
