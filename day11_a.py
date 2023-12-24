def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def expand(data):
    expanded_columns = [[] for _ in range(len(data))]
    for col in range(len(data[0])):
        for row in range(len(data)):
            expanded_columns[row].append(data[row][col])
        if all([data[row][col] == '.' for row in range(len(data))]):
            for row in range(len(data)):
                expanded_columns[row].append('.')

    expanded_rows = []
    for line in expanded_columns:
        expanded_rows.append(line)
        if  all([c == '.' for c in line]):
            expanded_rows.append(line)

    return expanded_rows


def find_galaxies(data):
    galaxies = []
    for i in range(len(data)):
        offset = -1
        while True:
            try:
                offset = data[i].index('#', offset + 1)
                galaxies.append((i, offset))
            except ValueError:
                break
    return galaxies


def sum_shortest_paths(galaxies):
    sums = 0
    for i in range(len(galaxies)- 1):
        for j in range(i+1, len(galaxies)):
            # Just use Manhattan distance
            shortest_path = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            sums += shortest_path
    return sums


file_path = 'data/day11.txt'
data = parse_data(file_path)
data = expand(data)
galaxy_coordinates = find_galaxies(data)
print(galaxy_coordinates)
print(sum_shortest_paths(galaxy_coordinates))
