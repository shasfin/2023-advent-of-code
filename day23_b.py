from pprint import pprint

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def get_neighbors(field, data):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = len(data)
    m = len(data[0])
    i, j = field
    neighbors = [(i + direction[0], j + direction[1]) for direction in dirs]

    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and data[neighbor[0]][neighbor[1]] != '#']


def get_graph_nodes(start, end, data):
    graph_nodes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '#' and len(get_neighbors((i, j), data)) > 2:
                graph_nodes.append((i, j))
    graph_nodes.append(start)
    graph_nodes.append(end)
    return graph_nodes


def summarize_graph(start, end, data):
    graph = {}
    n = len(data)
    m = len(data[0])
    graph_nodes = get_graph_nodes(start, end, data)
    for graph_node in graph_nodes:
        graph.setdefault(graph_node, find_graph_node_neighbors(graph_node, graph_nodes, data))
    return graph


def find_graph_node_neighbors(start, graph_nodes, data):
    n = len(data)
    m = len(data[0])
    graph_neighbors = []
    queue = [(start, 0)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    while queue != []:
        current, dist = queue.pop(0)
        neighbors = [neighbor for neighbor in get_neighbors(current, data) if not visited[neighbor[0]][neighbor[1]]]
        for neighbor in neighbors:
            visited[neighbor[0]][neighbor[1]] = True
            if neighbor in graph_nodes:
                graph_neighbors.append((neighbor, dist + 1))
            else:
                queue.append((neighbor, dist+1))
    return graph_neighbors


def longest_path(start, end, graph):
    steps = 0

    stack = [(start, 0, {start})]
    while stack != []:
        current, current_steps, visited = stack.pop()
        if current == end:
            steps = max(steps, current_steps)
        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbor)
                stack.append((neighbor, current_steps + distance, new_visited))
    return steps


file_path = 'data/day23.txt'
data = parse_data(file_path)
start = (0, 1)
end = (140, 139)
# end = (22, 21)
graph = summarize_graph(start, end, data)
pprint(graph)
print(longest_path(start, end, graph))