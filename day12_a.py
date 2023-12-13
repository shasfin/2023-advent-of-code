import itertools


def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))

    data = [tuple([line.split(" ")[0], list(map(int, line.split(" ")[1].split(",")))]) for line in lines]
    return data


def check_desc(desc, numbers):
    if desc.count('?') > 0:
        return False
    lengths_splitted = list(map(len, desc.split(".")))
    return numbers == lengths_splitted


def max_occurrences(my_str, character):
    my_list = [len(list(y)) for (c, y) in itertools.groupby(my_str) if c == character]
    return 0 if my_list == [] else max(my_list)


# def possibilities(desc, numbers):
#     print(f"{desc=}, {numbers=}")
#     if len(desc) < sum(numbers) + len(numbers) - 1:
#         return 0
#     elif max_occurrences(desc, '#') > (0 if numbers == [] else max(numbers)):
#         return 0
#     elif desc.count("#") > sum(numbers):
#         return 0
#     elif sum(numbers) == 0:
#         return 1
#     elif len(numbers) == 1:
#         if len(desc) == sum(numbers):
#             return 1
#         elif desc.count("?") == len(desc):
#             if sum(numbers) == 0:
#                 return 1
#             else:
#                 return len(desc) - numbers[0] + 1
#         elif len(list(filter(lambda x: x != '', desc.split("?")))) == 1:
#             # print(f"{desc=}, {numbers=}")
#             return min(numbers[0] - len(list(filter(lambda x: x != '', desc.split("?")))[0]) + 1, desc.find("#") + 1, len(desc) - desc.rfind("#"))
#         elif desc.count("#") == sum(numbers):
#             return 1
#         else:
#             idx_first = desc.find("#")
#             idx_last = desc.rfind("#")
#             if idx_last - idx_first + 1 > numbers[0]:
#                 return 0
#             else:
#                 return min(numbers[0] - idx_last + idx_first, idx_first + 1, len(desc) - idx_last)
#     else:
#         products = [0]*len(numbers)
#         for i in range(len(desc)):
#
#             if desc[i] == "?":
#                 # desc_copy = desc[:i] + ["."] + desc[i+1:]
#                 for j in range(len(products)):
#                     products[j] = max(products[j], possibilities(desc[:i], numbers[:j])*possibilities(desc[i+1:], numbers[j:]))
#                     print(f"{products=}")
#         return sum(products)

def is_compatible(sol, desc):
    if len(sol) != len(desc):
        return False
    for i in range(len(sol)):
        if sol[i] != desc[i] and desc[i] != "?":
            return False
    # print(f"{sol=} and {desc=} are compatible")
    return True

def construct_desc(offset, numbers, filling, rest):
    sol = "."*offset
    for i in range(len(filling)):
        sol += "#"*numbers[i] + "."*filling[i]
    sol += "#"*numbers[-1] + "."*rest
    return sol

def generate(n, numbers, filling):
    generated = []
    for a1 in range(1, n - sum(numbers) - len(numbers) + 3):
        if len(numbers) < 2:
            break
        if len(numbers) < 3:
            generated.append((n, numbers, [a1]))
        for a2 in range(1, n - sum(numbers) - len(numbers) - a1 + 4):
            if len(numbers) < 3:
                break
            if len(numbers) < 4:
                generated.append((n, numbers, [a1, a2]))
            for a3 in range(1, n - sum(numbers) - len(numbers) - a1 - a2 + 5):
                if len(numbers) < 4:
                    break
                if len(numbers) < 5:
                    generated.append((n, numbers, [a1, a2, a3]))
                for a4 in range(1, n - sum(numbers) - len(numbers) - a1 - a2 - a3 + 6):
                    if len(numbers) < 5:
                        break
                    if len(numbers) < 6:
                        generated.append((n, numbers, [a1, a2, a3, a4]))
                    for a5 in range(1, n - sum(numbers) - len(numbers) - a1 - a2 - a3 - a4 + 7):
                        if len(numbers) < 6:
                            break
                        if len(numbers) < 7:
                            generated.append((n, numbers, [a1, a2, a3, a4, a5]))
                        for a6 in range(1, n - sum(numbers) - len(numbers) - a1 - a2 - a3 - a4 - a5 + 8):
                            if len(numbers) < 7:
                                break
                            if len(numbers) < 8:
                                generated.append((n, numbers, [a1, a2, a3, a4, a5, a6]))
    return generated

def solve(desc, numbers):
    # print(f"Solving for {desc=} and {numbers=}")
    possibilities = 0
    n = len(desc)
    filling = [1] * (len(numbers) - 1)
    for offset in range(n - sum(numbers) - len(numbers) + 2):
        generated = generate(n - offset, numbers, filling)
        for _, numbers, filling in generated:
            rest = n - sum(numbers) - sum(filling) - offset
            if is_compatible(construct_desc(offset, numbers, filling, rest), desc):
                possibilities += 1
    # print(f"There are {possibilities} possibilities for {desc=} and {numbers=}")
    return possibilities


# print(generate(20, [1,2,1,4,5],[1, 1]))
# print(solve("?.?.??.?", [1,2]))
# print(construct_desc(5,[1,2,3],[2,4],1))
# print(is_compatible(construct_desc(5,[1,2,3],[2,4],1), "..???????#??..?##."))
# print(list(filter(lambda x: x != '', "???#????".split("?"))))

file_path = 'data/day12.txt'
data = parse_data(file_path)
possibilities = 0
for (desc, numbers) in data:
    possibilities += solve(desc, numbers)
print(possibilities)

