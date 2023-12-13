def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))

    data = [tuple([line.split(" ")[0], list(map(int, line.split(" ")[1].split(",")))]) for line in lines]
    return data


def is_compatible(sol, desc):
    return all(s == d or d == "?" for s, d in zip(sol, desc))


def compute_possibilities(desc, numbers):
    desc_len = len(desc)
    numbers_len = len(numbers)
    desc += "."

    possibilities = [[0] * (desc_len + 1) for _ in range(numbers_len + 1)]

    # initialize last row with 1 if it's compatible with '.......', otherwise with 0
    possibilities[-1][-1] = 1
    for s in range(desc_len-1, -1, -1):
        possibilities[-1][s] = 0 if desc[s] == '#' else possibilities[-1][s+1]

    # compute the values row by row starting from the second-to-last from right to left
    sum_numbers = 0
    for n in range(numbers_len-1, -1, -1):
        sum_numbers += numbers[n]
        for s in range(desc_len, -1, -1):
            if desc_len - s >= sum_numbers + numbers_len - n - 1:
                # There is space for all remaining numbers with their separators
                if desc[s] == '.' or desc[s] == '?':
                    possibilities[n][s] += possibilities[n][s+1]
                if desc[s] == '#' or desc[s] == '?':
                    val = numbers[n]
                    if s + val <= desc_len and is_compatible('#'*val+'.', desc[s:s+val+1]):
                        if desc[s+val] == '.':
                            possibilities[n][s] += possibilities[n+1][s+val]
                        else:
                            possibilities[n][s] += possibilities[n + 1][s + val + 1]

    # pprint(possibilities)

    # print(f"For {desc=}, {numbers=} there are {possibilities[0][0]} possibilities.")
    return possibilities[0][0]


def quintuply(data):
    return [("?".join([desc] * 5), numbers * 5) for desc, numbers in data]


file_path = 'data/day12.txt'
data = parse_data(file_path)
data = quintuply(data)
possibilities = sum(compute_possibilities(desc, numbers) for (desc, numbers) in data)
print(possibilities)
