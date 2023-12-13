def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))

    data = [tuple([line.split(" ")[0], list(map(int, line.split(" ")[1].split(",")))]) for line in lines]
    return data

def is_compatible(sol, desc):
    return all(s == d or d == "?" for s, d in zip(sol, desc))

def construct_desc(offset, numbers, filling, rest):
    sol = "." * offset + "".join(f"{'#' * n}{'.' * f}" for n, f in zip(numbers, filling)) + "#" * numbers[-1] + "." * rest
    return sol

def compute_possibilities(desc, numbers):
    # print(f"Possibilities for {desc=} (len = {len(desc)}), {numbers=} (len = {len(numbers)})")
    memo = {} # usage: memo[(s, index)]
    desc_len = len(desc)
    desc = desc + '.'
    numbers_len = len(numbers)

    def compute_possibilities_recursive(s, index):
        # print(f"Computing possibilities for {s=}, {index=}, {val=}")
        if memo.get((s, index), -1) != -1:
            # print(f"A.There are {memo[(s, index)]} possibilities for {s=}, {index=}")
            return memo[(s, index)]
        if index >= numbers_len and (s >= desc_len or is_compatible('.'*(desc_len-s), desc[s:])):
            memo[(s, index)] = 1
            # print(f"B.There are {memo[(s, index)]} possibilities for {s=}, {index=}")
            return 1
        if index >= numbers_len:
            memo[(s, index)] = 0
            # print(f"C.There are {memo[(s, index)]} possibilities for {s=}, {index=}")
            return 0
        if s >= desc_len and index < numbers_len:
            memo[(s, index)] = 0
            # print(f"D.There are {memo[(s, index)]} possibilities for {s=}, {index=}")
            return 0
        val = numbers[index]
        if desc_len - s < sum(numbers[index:]) + numbers_len - index - 1:
            memo[(s, index, val)] = 0
            # print(f"E.There are {memo[(s, index, val)]} possibilities for {s=}, {index=}, {val=}")
            return 0
        else:
            possibilities = 0
            if desc[s] == '#' or desc[s] == '?':
                if index < numbers_len and s+val <= desc_len and is_compatible('#'*val+'.', desc[s:s+val+1]):
                    possibilities += compute_possibilities_recursive(s+val+1, index+1)
            if desc[s] == "." or desc[s] == '?':
                possibilities += compute_possibilities_recursive(s+1, index)
            memo[(s, index, val)] = possibilities
            # print(f"F.There are {memo[(s, index, val)]} possibilities for {s=}, {index=}, {val=}")
            return possibilities

    result = compute_possibilities_recursive(0, 0)
    # print(f"There are {result} possibilities for {desc=} and {numbers=}")
    return result


def quintuply(data):
    quintuplied = []
    for desc, numbers in data:
        new_numbers = numbers * 5
        new_desc = "?".join([desc]*5)
        quintuplied.append((new_desc, new_numbers))
    return quintuplied


file_path = 'data/day12.txt'
data = parse_data(file_path)



# data = quintuply(data)
possibilities = sum(compute_possibilities(desc, numbers) for (desc, numbers) in data)
print(possibilities)
