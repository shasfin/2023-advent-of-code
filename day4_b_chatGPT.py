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
            current_card[1] = set(map(int, numbers.split("|")[0].split()))
            current_card[2] = set(map(int, numbers.split("|")[1].split()))

    # Append the last card after the loop
    if current_card is not None:
        parsed_data.append(current_card)

    return parsed_data


def calculate_scratchcards(cards):
    card_count = [1] * len(cards)  # Count of each original card

    for i, original in enumerate(cards):
        matching_numbers = len(original[1].intersection(original[2]))

        if matching_numbers > 0:
            card_count[i + 1:i + 1 + matching_numbers] = [count + card_count[i] for count in card_count[i + 1:i + 1 + matching_numbers]]

    return card_count

def solve_exercise():
    file_path = 'data/day4.txt'
    original_cards = parse_data(file_path)
    card_count = calculate_scratchcards(original_cards)

    total_scratchcards = sum(card_count)

    print(f"Total Scratchcards: {total_scratchcards}")
    for index, count in enumerate(card_count):
        print(f"Card {index + 1}: {count} instances")

solve_exercise()