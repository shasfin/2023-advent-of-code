import heapq
from pprint import pprint

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.strip())) for line in file]
    return data


def get_neighbors(node, last_dirs, n, m):
    directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'U'), (-1, 0, 'D')]
    contr = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}
    i, j = node
    return [(i + ii, j+ jj, last_dirs[1:]+dir) for ii, jj, dir in directions if 0 <= i + ii < n and 0 <= j + jj < m and last_dirs != dir*3 and not last_dirs[-1] == contr[dir]]


def heuristic(node, n, m):
    i, j = node
    return n - 1 - i + m - 1 - j

def dijkstra(start, costs):
    n = len(costs)
    m = len(costs[0])
    heap = []
    visited = [[set() for _ in range(m)] for _ in costs]
    heapq.heappush(heap, (heuristic(start, n, m), 0, start, '000'))
    visited[start[0]][start[1]].add('000')
    while len(heap) > 0:
        h, cost, current, last_dirs = heapq.heappop(heap)
        # print(f"{cost=}, {current=}, {last_dirs=}")
        neighbors = get_neighbors(current, last_dirs, n, m)
        for neighbor in neighbors:
            # print(f"{neighbor=}")
            if neighbor[2] not in visited[neighbor[0]][neighbor[1]]:
                visited[neighbor[0]][neighbor[1]].add(neighbor[2])
                heapq.heappush(heap, (heuristic((neighbor[0],neighbor[1]), n, m) + cost + costs[neighbor[0]][neighbor[1]], cost + costs[neighbor[0]][neighbor[1]], neighbor[:-1], neighbor[2]))
                if neighbor[:-1] == (n-1, m-1):
                    return cost + costs[neighbor[0]][neighbor[1]]
    return 0



file_path = 'data/day17.txt'
data = parse_data(file_path)
print(dijkstra((0, 0), data))