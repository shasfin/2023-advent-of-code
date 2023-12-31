def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    index_empty_line = data.index('')
    workflows, machines = data[:index_empty_line], data[index_empty_line+1:]
    return parse_workflows(workflows), parse_machines(machines)


def parse_workflows(workflows):
    workflow_dict = {}
    for workflow in workflows:
        key, conditions = workflow.split('{')
        conditions = conditions[:-1].split(',')
        for i in range(len(conditions) - 1):
            rest, next = conditions[i].split(':')
            attribute, operator, value = rest[0], rest[1], rest[2:]
            conditions[i] = (attribute, operator, int(value), next)
        conditions[-1] = ('x', '>', 0, conditions[-1])
        workflow_dict.setdefault(key, conditions)
    return workflow_dict


def parse_machines(machines):
    machine_list = []
    for machine in machines:
        attributes = machine[1:-1].split(',')
        machine_list.append({attr[0]: int(attr[2:]) for attr in attributes})
    return machine_list


def compare(val1, op, val2):
    if op == '<':
        return val1 < val2
    elif op == '>':
        return val1 > val2


def run_for_one_machine(machine, workflows):
    next = 'in'
    while next != 'A' and next != 'R':
        for attribute, operator, value, state in workflows[next]:
            if compare(machine[attribute], operator, value):
                next = state
                break

    return next


def run(machines, workflows):
    total = 0
    for machine in machines:
        if run_for_one_machine(machine, workflows) == 'A':
            total += sum(machine.values())
    return total

file_path = 'data/day19.txt'
workflows, machines = parse_data(file_path)
print(run(machines, workflows))