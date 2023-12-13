def ways_to_win(race):
    ways = 0
    (time, distance) = race
    for speed in range(time):
        my_dist = speed * (time - speed)
        if my_dist > distance:
            ways += 1
    return ways

race = (47986698, 400121310111540)
print(ways_to_win(race))

