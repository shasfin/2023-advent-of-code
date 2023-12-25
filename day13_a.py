from pprint import pprint

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    fields = [[]]
    for line in data:
        if line != '':
            fields[-1].append(line)
        else:
            fields.append([])

    return fields


def find_symmetry_column(field):
    candidate_symmetry_columns = []
    for j in range(len(field[0])-1):
        if all(field[i][j] == field[i][j+1] for i in range(len(field))):
            candidate_symmetry_columns.append(j)

    for symmetry_column in candidate_symmetry_columns:
        all_equal = True
        for offset in range(symmetry_column+1):
            if any(field[i][symmetry_column-offset] != field[i][symmetry_column+1+offset] for i in range(len(field)) if 0 <= symmetry_column-offset and symmetry_column+1+offset < len(field[0])):
                all_equal = False
        if all_equal:
            return symmetry_column + 1

    return 0


def find_symmetry_row(field):
    candidate_symmetry_rows = []
    for i in range(len(field) - 1):
        if field[i] == field[i + 1]:
            candidate_symmetry_rows.append((i))

    for symmetry_row in candidate_symmetry_rows:
        if all(field[symmetry_row - offset] == field[symmetry_row + 1 + offset] for offset in range(symmetry_row + 1) if
               0 <= symmetry_row - offset and symmetry_row + 1 + offset < len(field)):
            return symmetry_row + 1

    return 0


file_path = 'data/day13.txt'
fields = parse_data(file_path)
syms = 0
for field in fields:
    pprint(field)
    col = find_symmetry_column(field)
    print(f"Symmetry column: {col}")
    row = find_symmetry_row(field)
    print(f"Symmetry row: {row}")
    syms += col + row * 100
print(syms)