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


def get_column(data, j):
    return ''.join(row[j] for row in data)


def find_new_symmetry_column(field, old_symmetry_column):
    candidate_symmetry_columns = [] # list of tuples (row, smudge_used)
    for j in range(len(field[0]) - 1):
        if j+1 != old_symmetry_column:
            allBut, smudge_Used = equalButOne(get_column(field, j), get_column(field, j + 1))
            if allBut:
                candidate_symmetry_columns.append((j, smudge_Used))

    for symmetry_column, smudge_Used in candidate_symmetry_columns:
        all_ok = True
        for offset in range(1, symmetry_column + 1):
            if 0 <= symmetry_column - offset and symmetry_column + 1 + offset < len(field[0]):
                allButOffset, smudgeUsedOffset = equalButOne(get_column(field, symmetry_column - offset), get_column(field, symmetry_column + 1 + offset))
                if allButOffset and smudge_Used + smudgeUsedOffset < 2:
                    all_ok = all_ok and True
                else:
                    all_ok = False
        if all_ok:
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


def equalButOne(str1, str2):
    equal_chars = [c1 == c2 for c1, c2 in zip(str1, str2)]
    all_equal = all(equal_chars)
    one_different = equal_chars.count(False) == 1
    return (all_equal or one_different, one_different)


def find_new_symmetry_row(field, old_symmetry_row):
    candidate_symmetry_rows = [] # list of tuples (row, smudge_used)
    for i in range(len(field) - 1):
        if i+1 != old_symmetry_row:
            allBut, smudge_Used = equalButOne(field[i], field[i+1])
            if allBut:
                candidate_symmetry_rows.append((i, smudge_Used))
    # print(f"{candidate_symmetry_rows=}")
    for symmetry_row, smudge_Used in candidate_symmetry_rows:
        all_ok = True
        for offset in range(1, symmetry_row + 1):
            if 0 <= symmetry_row - offset and symmetry_row + 1 + offset < len(field):
                # print(f"{offset=}, {symmetry_row - offset=}, {symmetry_row + 1 + offset=}")
                # print(f"{field[symmetry_row - offset]=}, {field[symmetry_row + 1 + offset]=}")
                allButOffset, smudgeUsedOffset = equalButOne(field[symmetry_row - offset], field[symmetry_row + 1 + offset])
                # print(f"{allButOffset=}, {smudgeUsedOffset=}")
                if allButOffset and smudge_Used + smudgeUsedOffset < 2:
                    all_ok = all_ok and True
                else:
                    all_ok = False
        if all_ok:
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
    new_col = find_new_symmetry_column(field, col)
    print(f"New symmetry column: {new_col}")
    new_row = find_new_symmetry_row(field, row)
    print(f"New symmetry row: {new_row}")
    syms += new_col + new_row * 100
print(syms)



