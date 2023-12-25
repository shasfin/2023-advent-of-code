def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(',') for line in file]
    return data[0]


def compute_hash(s):
    acc = 0
    for c in s:
        acc += ord(c)
        acc *= 17
        acc %= 256
    return acc


# Box: (counter, {dictionary label -> [position, focal length]})
def run_hashmap_alg(operations):
    boxes = [[0, {}] for _ in range(256)]
    for op, label, focal_length in operations:
        box_number = compute_hash(label)
        if op == '-':
            if label in boxes[box_number][1]:
                boxes[box_number][1][label] = [None, None]
        else:
            if label in boxes[box_number][1] and boxes[box_number][1][label][0] != None:
                boxes[box_number][1][label][1] = focal_length
            else:
                boxes[box_number][1][label] = [boxes[box_number][0], focal_length]
                boxes[box_number][0] += 1
    return boxes


def compute_focusing_power(boxes):
    total_power = 0
    for k, box in enumerate(boxes):
        sorted_lenses = [(position, focal_length) for (label, [position, focal_length]) in box[1].items() if position != None]
        sorted_lenses.sort()
        # print(f"Box {k:3}: {sorted_lenses}")
        total_power += sum((k+1) * (i+1) * focal_length for i, (position, focal_length) in enumerate(sorted_lenses))
    return total_power


def parse_operations(s):
    focal_length = None
    if '=' in s:
        label, focal_length = s.split('=')
        focal_length = int(focal_length)
        op = '='
    else:
        label = s[:-1]
        op = '-'
    return op, label, focal_length

file_path = 'data/day15.txt'
data = parse_data(file_path)
ops = list(map(parse_operations, data))
boxes = run_hashmap_alg(ops)
# print(boxes)
result = compute_focusing_power(boxes)
print(result)