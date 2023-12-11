def parse_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    current_card = None

    for line in lines:
        if line.startswith("Card"):
            if current_card is not None:
                parsed_data.append(current_card)

            card_number, numbers = line.split(":")
            current_card = [int(card_number.split()[1]), [], []]
            current_card[1] = list(map(int, numbers.split("|")[0].split()))
            current_card[2] = list(map(int, numbers.split("|")[1].split()))

    # Append the last card after the loop
    if current_card is not None:
        parsed_data.append(current_card)

    return parsed_data

file_path = 'data/day4.txt'
result = parse_data(file_path)
print(result)