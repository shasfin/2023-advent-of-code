def parse_data(file_path):
    with open(file_path, 'r') as file:
        return [parse_line(line) for line in file]


def parse_line(line):
    color_to_index = {'red': 0, 'green': 1, 'blue': 2}
    parts = line.strip().split(': ')
    game_id = int(parts[0].split(' ')[1])
    raw_games = parts[1].split('; ')
    parsed_games = [[0]*3 for _ in raw_games]
    for i, raw_game in enumerate(raw_games):
        cubes = raw_game.split(', ')
        for cube in cubes:
            cube = cube.split(' ')
            parsed_games[i][color_to_index[cube[1]]] = int(cube[0])

    return game_id, parsed_games


def is_game_possible(game):
    master_pattern = [12, 13, 14]
    return all(cubes[0] <= master_pattern[0] and cubes[1] <= master_pattern[1] and cubes[2] <= master_pattern[2] for cubes in game)


def power(game):
    red = max(cubes[0] for cubes in game)
    green = max(cubes[1] for cubes in game)
    blue = max(cubes[2] for cubes in game)

    return red * green * blue

file_path = 'data/day2.txt'
data = parse_data(file_path)
print(data)
print(sum(power(game) for id, game in data))