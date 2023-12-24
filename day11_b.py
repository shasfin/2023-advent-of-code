from bisect import bisect

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def find_columns_to_expand(data):
    return [col for col in range(len(data[0])) if all([data[row][col] == '.' for row in range(len(data))])]


def find_rows_to_expand(data):
    return [row for row in range(len(data)) if all([c == '.' for c in data[row]])]


def find_galaxies(data, rows_to_expand, columns_to_expand, factor):
    galaxies = []
    index_row_expand = 0
    for i in range(len(data)):
        if index_row_expand < len(rows_to_expand) and i == rows_to_expand[index_row_expand]:
            index_row_expand += 1
        offset = -1
        while True:
            try:
                offset = data[i].index('#', offset + 1)
            except ValueError:
                break
            index_col_expand = bisect(columns_to_expand, offset)
            galaxies.append((i + index_row_expand * (factor-1), offset + index_col_expand * (factor-1)))
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
columns_to_expand = find_columns_to_expand(data)
rows_to_expand = find_rows_to_expand(data)
print(columns_to_expand, rows_to_expand)
galaxy_coordinates = find_galaxies(data, rows_to_expand, columns_to_expand, 1000000)
print(galaxy_coordinates)
print(sum_shortest_paths(galaxy_coordinates))
