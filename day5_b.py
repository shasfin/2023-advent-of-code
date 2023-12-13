def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))

    seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
    seed_ranges = []
    for j in range(0, len(seeds)-1, 2):
        seed_ranges.append(tuple([seeds[j], seeds[j+1]]))

    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    i = 3
    while lines[i] != "":
        seed_to_soil_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2 # +2 to skip the empty line and the line with the map name.
    while lines[i] != "":
        soil_to_fertilizer_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2
    while lines[i] != "":
        fertilizer_to_water_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2
    while lines[i] != "":
        water_to_light_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2
    while lines[i] != "":
        light_to_temperature_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2
    while lines[i] != "":
        temperature_to_humidity_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    i += 2
    while lines[i] != "":
        humidity_to_location_map.append(list(map(int, lines[i].split(" "))))
        i += 1

    seed_ranges.sort(key=lambda x: x[0])
    seed_to_soil_map.sort(key=lambda x: x[0])
    soil_to_fertilizer_map.sort(key=lambda x: x[0])
    fertilizer_to_water_map.sort(key=lambda x: x[0])
    water_to_light_map.sort(key=lambda x: x[0])
    light_to_temperature_map.sort(key=lambda x: x[0])
    temperature_to_humidity_map.sort(key=lambda x: x[0])
    humidity_to_location_map.sort(key=lambda x: x[0])

    return seed_ranges, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map


def apply_reverse_function(func, y_s):
    [destination, source, range] = func
    if destination <= y_s < destination + range:
        return y_s + (source - destination)
    else:
        return y_s


def apply_right_reverse_function(functions, y_s):
    smaller_functions = [function for function in functions if function[0] <= y_s]
    if smaller_functions:
        func = smaller_functions[-1]
    else:
        func = functions[0]

    return apply_reverse_function(func, y_s)

def is_in_seeds_range(seed_ranges, seed):
    smaller_seeds = [s for s in seed_ranges if s[0] <= seed]
    if not smaller_seeds:
        return False
    else:
        (x, r) = max(smaller_seeds, key=lambda s: s[0])
        return x <= seed < x + r

def compute_seed_for_location(location, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map):
    humidity = apply_right_reverse_function(humidity_to_location_map, location)
    temperature = apply_right_reverse_function(temperature_to_humidity_map, humidity)
    light = apply_right_reverse_function(light_to_temperature_map, temperature)
    water = apply_right_reverse_function(water_to_light_map, light)
    fertilizer = apply_right_reverse_function(fertilizer_to_water_map, water)
    soil = apply_right_reverse_function(soil_to_fertilizer_map, fertilizer)
    seed = apply_right_reverse_function(seed_to_soil_map, soil)

    return seed


file_path = "data/day5.txt"

seed_ranges, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map = parse_data(file_path)

for location in range(0, humidity_to_location_map[-1][0] + humidity_to_location_map[-1][2]):
    seed = compute_seed_for_location(location, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)
    if is_in_seeds_range(seed_ranges, seed):
        print(location)
        break
