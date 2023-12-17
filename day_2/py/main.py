import re

IN_FILEPATH = "F:\\Projects\\advent_of_code_2023\\day_2\\input.txt"

if __name__ == "__main__":
    ids = list()
    powers = list()
    
    with open(IN_FILEPATH) as f:
        input = f.read()
    
    for i, line in enumerate(input.split("\n")):
        reds = [int(x) for x in re.findall("(\d{1,2}) red", line)]
        green = [int(x) for x in re.findall("(\d{1,2}) green", line)]
        blue = [int(x) for x in re.findall("(\d{1,2}) blue", line)]
        
        game_power = max(reds) * max(green) * max(blue)
        powers.append(game_power)
        
        if any([x > 12 for x in reds]) or any([x > 13 for x in green]) or any([x > 14 for x in blue]):
            continue
        else:
            ids.append(i+1)
    
    print(powers)
    print(f"SUM PART 1: {sum(ids)}")
    print(f"SUM PART 2: {sum(powers)}")