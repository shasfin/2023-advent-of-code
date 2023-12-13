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

def generate_combinations(n, numbers, filling):
    generated = []

    def generate_recursive(numbers, curr_filling, idx):
        if idx == len(numbers) - 1:
            generated.append((n, numbers, curr_filling))
            return

        for ai in range(1, n - sum(numbers) - sum(curr_filling) + 1):
            generate_recursive(numbers, curr_filling + [ai], idx + 1)

    generate_recursive(numbers, [], 0)
    return generated


def solve(desc, numbers):
    possibilities = 0
    n = len(desc)
    for offset in range(n - sum(numbers) - len(numbers) + 2):
        generated = generate_combinations(n - offset, numbers, [1] * (len(numbers) - 1))
        for _, numbers, filling in generated:
            rest = n - sum(numbers) - sum(filling) - offset
            if is_compatible(construct_desc(offset, numbers, filling, rest), desc):
                possibilities += 1
    return possibilities

file_path = 'data/day12.txt'
data = parse_data(file_path)
possibilities = sum(solve(desc, numbers) for (desc, numbers) in data)
print(possibilities)
