def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [parse_line(line) for line in file.readlines()]

    return data

def parse_line(line):
    directions = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    hex_string = '0x'+line.strip().split(' ')[2][2:-1]
    hex = int(hex_string, 0)
    direction = directions[hex % 16]
    steps = hex // 16
    return direction, steps


def shoelace(vertices):
    area = 0
    for i in range(len(vertices)):
        area += (vertices[i][0] + vertices[i-1][0]) * (vertices[i][1] - vertices[i-1][1])

    return abs(area)


def find_vertices(data):
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    vertices = [(0, 0)]
    perimeter = 0

    for direction, steps in data:
        diff_x, diff_y = [int(steps) * x for x in directions[direction]]
        next_vertex = (vertices[-1][0] + diff_x, vertices[-1][1] + diff_y)
        vertices.append(next_vertex)
        perimeter += int(steps)

    return vertices, perimeter


file_path = 'data/day18.txt'
data = parse_data(file_path)
vertices, perimeter = find_vertices(data)
double_area = shoelace(vertices[0:-1])
print((shoelace(vertices[0:-1]) + perimeter) // 2 + 1)