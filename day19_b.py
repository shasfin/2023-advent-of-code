import math


def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    index_empty_line = data.index('')
    workflows= data[:index_empty_line]
    return parse_workflows(workflows)


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


def update_values(values, attribute, operator, value, old_conditions):
    if operator == '<':
        if values[attribute][0] >= value:
            values[attribute] = (0, -1)
        elif values[attribute][1] >= value:
            values[attribute] = (values[attribute][0], value - 1)
    elif operator == '>':
        if values[attribute][1] <= value:
            values[attribute] = (0, -1)
        elif values[attribute][0] <= value:
            values[attribute] = (value + 1, values[attribute][1])
    for old_attribute, old_operator, old_value in old_conditions:
        if old_operator == '<':
            if values[old_attribute][1] <= old_value:
                values[old_attribute] = (0, -1)
            elif values[old_attribute][0] <= old_value:
                values[old_attribute] = (old_value, values[old_attribute][1])
        elif old_operator == '>':
            if values[old_attribute][0] >= old_value:
                values[old_attribute] = (0, -1)
            elif values[old_attribute][1] >= old_value:
                values[old_attribute] = (values[old_attribute][0], old_value)


def bfs(workflows):
    queue = [('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})]
    result = 0
    while queue:
        state, values = queue.pop(0)
        if state == 'A':
            result += math.prod(val[1] - val[0] + 1 for val in values.values())
        else:
            old_conditions = []
            for attribute, operator, value, next in workflows[state]:
                values_copy = values.copy()
                update_values(values_copy, attribute, operator, value, old_conditions)
                old_conditions.append((attribute, operator, value))
                if next != 'R':
                    queue.append((next, values_copy))

    return result


file_path = 'data/day19.txt'
workflows = parse_data(file_path)
print(f"The total number of accepted combinations for the input workflow is {bfs(workflows)}.")

#-------------------------------------------------------------------------------
# Compute 'manually' for the given example
violet = {'x': (1, 1415), 'm': (1, 4000), 'a': (1, 2005), 's': (1, 1350)}
cyan = {'x': (2663, 4000), 'm': (1, 4000), 'a': (1, 2005), 's': (1, 1350)}
rosa = {'x': (1, 4000), 'm': (2091, 4000), 'a': (2006, 4000), 's': (1, 1350)}
orange = {'x': (1, 2440), 'm': (1, 2090), 'a': (2006, 4000), 's': (537, 1350)}
yellow = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (3449, 4000)}
green = {'x': (1, 4000), 'm': (1549, 4000), 'a': (1, 4000), 's': (2771, 3448)}
light_blue = {'x': (1, 4000), 'm': (1, 1548), 'a': (1, 4000), 's': (2771, 3448)}
pink = {'x': (1, 4000), 'm': (839, 1800), 'a': (1, 4000), 's': (1351, 2770)}
forest = {'x': (1, 4000), 'm': (1, 838), 'a': (1, 1716), 's': (1351, 2770)}

result = 0
for color in [violet, cyan, rosa, orange, yellow, green, light_blue, pink, forest]:
    result += math.prod(val[1] - val[0] + 1 for val in color.values())

print(result)
print(4000*4000*4000*4000) # Compare to the number of all possible combinations
print(result - 167409079868000) # Compare with the given correct result
#-------------------------------------------------------------------------------
