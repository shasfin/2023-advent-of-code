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


def get_node_to_input(node_to_output):
    node_to_input = {}
    for node_from, nodes_to in node_to_output.items():
        for node_to in nodes_to:
            node_to_input.setdefault(node_to, [])
            node_to_input[node_to].append(node_from)
    return node_to_input


def traverse_backwards(node_from, expected_pulse, node_to_input, node_to_type):
    and_states = {} # dictionary node -> (dictionary parent -> high/low)
    percent_states = {} # dictionary node -> ON/OFF
    children_of_broadcaster = ['kt', 'pd', 'xv', 'rg']
    inputs = node_to_input[node_from]
    queue = [(parent, expected_pulse, node_from) for parent in inputs]
    i = 0
    break_from_while = False

    while queue != [] and not break_from_while and children_of_broadcaster != []:
        i += 1
        print(f"\n{len(queue)=}")
        parent, pulse, current = queue.pop(0)
        parent_type = node_to_type.get(parent, 'general')

        if parent_type == 'broadcaster' and not pulse:
            children_of_broadcaster.remove(current)
        elif parent_type == '%':
            if parent not in percent_states.keys():
                percent_states[parent] = pulse
            for input_node in node_to_input[parent]:
                print((input_node, False, parent))
                queue.append((input_node, False, parent))
                if input_node == 'button':
                    break_from_while = True
        elif parent_type == '&':
            if not pulse: # if an and-node sends a low pulse, then all inputs were high
                and_states[parent] = {input_node: True for input_node in node_to_input[parent]}
                for input_node in node_to_input[parent]:
                    print((input_node, True, parent))
                    queue.append((input_node, True, parent))
                    if input_node == 'button':
                        break_from_while = True
            elif len(node_to_input[parent]) == 1: # if an and-node sends a high pulse and has only one input, then the input was low.
                print((node_to_input[parent][0], False, parent))
                queue.append((node_to_input[parent][0], False, parent))
                if node_to_input[parent][0] == 'button':
                    break_from_while = True
            else:
                # Let's hope that it never happens, otherwise we have a problem
                print(f'Houston, we have a problem. Node {parent_type}{parent} must send a high pulse but I have no idea which of the inputs must be low')
    return and_states, percent_states


def push_button(node_to_output, node_to_type, and_states, percent_states):
    # percent_states: dictionary node -> ON/OFF for nodes of type '%'
    # and_states: dictionary node -> {'a': False, 'b': True, 'c': False...} for nodes of type '&' (False = 'low', True = 'high')

    queue = [('button', False, 'broadcaster')]

    while queue != []:
        node_from, pulse, node_to = queue.pop(0)
        node_type = node_to_type.get(node_to, 'general')
        if node_to == 'rx':
            print(f"Found rx with {pulse=}")
        if node_type == 'button':
            queue.append((node_to, False, 'broadcaster'))
        elif node_type == 'broadcaster':
            for node in node_to_output[node_to]:
                queue.append((node_to, False, node))
        elif node_type == '&':
            and_states[node_to][node_from] = pulse
            output = not all(and_states[node_to].values())
            for node in node_to_output[node_to]:
                queue.append((node_to, output, node))
        elif node_type == '%':
            if pulse == False:
                percent_states[node_to] = not percent_states[node_to]
                for node in node_to_output[node_to]:
                    queue.append((node_to, percent_states[node_to], node))

    return and_states, percent_states

file_path = 'data/day20.txt'
data = parse_data(file_path)
node_to_output, node_to_type = get_node_to_output(data)
node_to_output['button'] = ['broadcaster']
node_to_type['button'] = ['button']
conj_node_to_input = get_conj_node_to_input(node_to_type, node_to_output)
node_to_input = get_node_to_input(node_to_output)


# Initial states
percent_states = {node: False for node in node_to_type.keys() if node_to_type[node] == '%'}
and_states = {node: {input_node: False for input_node in conj_node_to_input[node]} for node in node_to_type.keys() if node_to_type[node] == '&'}

and_states_rx, percent_states_rx = traverse_backwards('rx', False, node_to_input, node_to_type)

for node1 in and_states_rx.keys():
    for node2 in and_states_rx[node1]:
        and_states[node1][node2] = and_states_rx[node1][node2]

for node1 in percent_states_rx.keys():
    percent_states[node1] = percent_states_rx[node1]

push_button(node_to_output, node_to_type, and_states, percent_states)

