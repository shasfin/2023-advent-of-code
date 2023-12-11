from math import lcm

def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))
        instructions = lines[0]
        network = {line.split(" = ")[0]: (line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")) for line in lines[2:]}
        return instructions, network

file_path = "data/day8.txt"
instructions, network = parse_data(file_path)


periods = []
for node in network.keys():
    if node.endswith('A'):
        period = 0
        while not node.endswith('Z'):
            for instruction in instructions:
                node = network[node][0] if instruction == 'L' else network[node][1]
                period += 1
        periods.append(period)
        print(f"{node=}, period = {period}")

print(lcm(*periods))

