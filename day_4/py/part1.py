INPUT: str = "day_4/input.txt"
EXAMPLE: str = "day_4/ex.txt"

def part_1(filepath: str):
    with open(filepath) as f:
        text = f.read()
    
    score: int = 0
     
    lines = text.split("\n")
    for line in lines:
        card_no, game = line.split(":")
        player_numbers, winning_numbers = game.split("|")
        player_numbers = set([x for x in player_numbers.split(" ") if x])
        winning_numbers = set([x for x in winning_numbers.split(" ") if x])
        common = player_numbers.intersection(winning_numbers)
        if len(common) == 0:
            continue
        elif len(common) == 1:
            score += 1
        else:
            curr_score: int = 1
            for _ in range(len(common)-1):
                curr_score = curr_score*2
            score += curr_score
    print(score)
    
def part_2(filepath: str):
    with open(filepath) as f:
        text = f.read()
    
    score: int = 0
    score_per_card = dict()
    lines = text.split("\n")
    
    number_of_cards = [1 for _ in range(len(lines))]
     
    for i, line in enumerate(lines):
        card_no, game = line.split(":")
        player_numbers, winning_numbers = game.split("|")
        player_numbers = set([x for x in player_numbers.split(" ") if x])
        winning_numbers = set([x for x in winning_numbers.split(" ") if x])
        common = player_numbers.intersection(winning_numbers)
        curr_score = len(common)
        if curr_score == 0:
            continue
        for j in range(1, 1+curr_score):
            number_of_cards[i+j] += number_of_cards[i]
    print(sum(number_of_cards))

if __name__ == "__main__":
    # part_1(INPUT)
    part_2(INPUT)