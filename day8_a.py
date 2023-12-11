def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))
        instructions = lines[0]
        network = {line.split(" = ")[0]: (line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")) for line in lines[2:]}
        return instructions, network

file_path = "data/day8.txt"
instructions, network = parse_data(file_path)

steps = 0
current = 'AAA'
while current != 'ZZZ':
    for instruction in instructions:
        if instruction == 'L':
            current = network[current][0]
        elif instruction == 'R':
            current = network[current][1]
        steps += 1

print(steps)

