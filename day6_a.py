from math import prod


def ways_to_win(race):
    ways = 0
    (time, distance) = race
    for speed in range(time):
        my_dist = speed * (time - speed)
        if my_dist > distance:
            ways += 1
    return ways

races = [(47, 400), (98, 1213), (66, 1011), (98, 1540)]
print(prod(list(map(ways_to_win, races))))

