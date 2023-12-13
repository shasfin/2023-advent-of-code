def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = list(map(str.strip, file.readlines()))

    seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
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

    return seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map


def apply_function(func, x_s):
    [destination, source, range] = func
    if source <= x_s < source + range:
        return x_s + (destination - source)
    else:
        return x_s


def apply_right_function(functions, x_s):
    smaller_functions = [function for function in functions if function[1] <= x_s]
    if smaller_functions != []:
        func = max(smaller_functions, key = lambda x: x[1])
    else:
        func = functions[0]

    return apply_function(func, x_s)


file_path = "data/day5.txt"

seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map = parse_data(file_path)
soils = list(map(lambda x: apply_right_function(seed_to_soil_map, x), seeds))
fertilizers = list(map(lambda x: apply_right_function(soil_to_fertilizer_map, x), soils))
waters = list(map(lambda x: apply_right_function(fertilizer_to_water_map, x), fertilizers))
lights = list(map(lambda x: apply_right_function(water_to_light_map, x), waters))
temperatures = list(map(lambda x: apply_right_function(light_to_temperature_map, x), lights))
humidities = list(map(lambda x: apply_right_function(temperature_to_humidity_map, x), temperatures))
locations = list(map(lambda x: apply_right_function(humidity_to_location_map, x), humidities))

print(min(locations))
