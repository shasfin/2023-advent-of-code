def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data


def get_node_to_output(data):
    node_to_output = {}
    node_to_type = {}
    for connection in data:
        node_from, nodes_to = connection.split(' -> ')
        if node_from == 'broadcaster':
            node_to_type[node_from] = 'broadcaster'
        elif node_from[0] == '%' or node_from[0] == '&':
            node_to_type[node_from[1:]] = node_from[0]
            node_from = node_from[1:]
        else:
            node_to_type[node_from] = 'general'
        node_to_output[node_from] = nodes_to.split(', ')

    return node_to_output, node_to_type


def get_conj_node_to_input(node_to_type, node_to_output):
    conj_node_to_input = {}
    for node_from, nodes_to in node_to_output.items():
        for node_to in nodes_to:
            if node_to_type.get(node_to, 'general') == '&':
                conj_node_to_input.setdefault(node_to, [])
                conj_node_to_input[node_to].append(node_from)
    return conj_node_to_input


def push_button(node_to_output, node_to_type, and_states, percent_states):
    # percent_states: dictionary node -> ON/OFF for nodes of type '%'
    # and_states: dictionary node -> {'a': False, 'b': True, 'c': False...] for nodes of type '&' (False = 'low', True = 'high')
    counts = {False: 0, True: 0}

    queue = [('button', False, 'broadcaster')]
    counts[False] += 1

    while queue != []:
        node_from, pulse, node_to = queue.pop(0)
        node_type = node_to_type.get(node_to, 'general')
        if node_type == 'button':
            queue.append((node_to, False, 'broadcaster'))
            counts[False] += 1
        elif node_type == 'broadcaster':
            for node in node_to_output[node_to]:
                queue.append((node_to, False, node))
                counts[False] += 1
        elif node_type == '&':
            and_states[node_to][node_from] = pulse
            output = not all(and_states[node_to].values())
            for node in node_to_output[node_to]:
                queue.append((node_to, output, node))
                counts[output] += 1
        elif node_type == '%':
            if pulse == False:
                percent_states[node_to] = not percent_states[node_to]
                for node in node_to_output[node_to]:
                    queue.append((node_to, percent_states[node_to], node))
                    counts[percent_states[node_to]] += 1

    return and_states, percent_states, counts

file_path = 'data/day20.txt'
data = parse_data(file_path)
node_to_output, node_to_type = get_node_to_output(data)
node_to_output['button'] = ['broadcaster']
node_to_type['button'] = ['button']
conj_node_to_input = get_conj_node_to_input(node_to_type, node_to_output)

# Initial states
percent_states = {node: False for node in node_to_type.keys() if node_to_type[node] == '%'}
and_states = {node: {input_node: False for input_node in conj_node_to_input[node]} for node in node_to_type.keys() if node_to_type[node] == '&'}

count_low = 0
count_high = 0
for _ in range(1000):
    and_states, percent_states, counts = push_button(node_to_output, node_to_type, and_states, percent_states)
    count_low += counts[False]
    count_high += counts[True]

print(f"{count_low=}, {count_high=}")
print(count_low * count_high)

