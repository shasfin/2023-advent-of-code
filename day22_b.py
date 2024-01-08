import numpy as np

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [parse_line(line.strip()) for line in file]
    return data


def parse_line(line):
    point1, point2 = line.split('~')
    point1 = list(map(int, point1.split(',')))
    point2 = list(map(int, point2.split(',')))
    return point1, point2


def min_z(brick):
    p1, p2 = brick
    return min(p1[2], p2[2])


def is_supporting(brick1, brick2):
    print(f'Is {brick1} supporting {brick2}?')
    (p11, p12) = brick1
    (p21, p22) = brick2
    if max(p11[2], p12[2]) + 1 == min(p21[2], p22[2]): # z-coordinates should be adjacent
        print(f'z-coordinates are adjacent! Brick1: ({p11[2]}, { p12[2]}), Brick2: ({p21[2]}, {p22[2]}).')
        return overlaps(brick1, brick2)
    return False


def overlaps(brick1, brick2):
    # Check whether x- and y-coordinates overlap
    (p11, p12) = brick1
    (p21, p22) = brick2
    if min(p11[0], p12[0]) <= p21[0] <= max(p11[0], p12[0]) or min(p11[0], p12[0]) <= p22[0] <= max(p11[0], p12[0]):
        # x-coordinates should overlap
        return min(p11[1], p12[1]) <= p21[1] <= max(p11[1], p12[1]) or min(p11[1], p12[1]) <= p22[1] <= max(p11[1], p12[1])
        # y-coordinates should also overlap
    return False


def solve(data):
    grid = np.ones((10, 10), dtype=int) * -1
    heights = np.zeros((10, 10), dtype=int)
    status = [True for _ in range(len(data))] # is it disintegratable?
    for (index, brick) in enumerate(data):
        p1, p2 = brick
        supporting_z = np.max(heights[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1])
        supporting_blocks = set()
        for i in range(p1[0], p2[0] + 1):
            for j in range(p1[1], p2[1]+1):
                if heights[i, j] == supporting_z and grid[i, j] != -1:
                    supporting_blocks.add(grid[i, j])
        if len(supporting_blocks) == 1:
            for s in supporting_blocks:
                status[s] = False
        grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] = index
        heights[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] = supporting_z + max(p1[2], p2[2]) - min(p1[2], p2[2]) + 1


    return sum(status)


file_path = 'data/day22.txt'
data = parse_data(file_path)
data.sort(key=min_z)
print(data)
print(solve(data))

