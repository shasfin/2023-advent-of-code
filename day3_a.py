def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip()+'.' for line in file]
    return data + ['.'*len(data[0])]


file_path = 'data/day3.txt'
data = parse_data(file_path)
n = len(data)
m = len(data[0])
sum = 0

for i, line in enumerate(data):
    num_start = -1
    neighbor = False
    for j, c in enumerate(line):
        if c.isdigit():
            if num_start == -1:
                num_start = j
            for ii in range(max(i - 1, 0), min(i + 1, n)+1):
                for jj in range(max(j - 1, 0), min(j + 1, m)+1):
                    if data[ii][jj] != '.' and not data[ii][jj].isdigit():
                        neighbor = True
        else:
            if num_start >= 0 and neighbor:
                sum += int(line[num_start:j])
            num_start = -1
            neighbor = False


print(sum)


