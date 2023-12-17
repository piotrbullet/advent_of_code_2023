import re

IN_FILEPATH: str = "day_3/input.txt"

def get_gears_coordinates(lines: list) -> tuple:
    gears_coo = list()
    for i, line in enumerate(lines):
        matches = [m.start(0) for m in re.finditer("\*", line)]
        for m in matches:
            gears_coo.append((i, m))
    return gears_coo

def get_coordinates_around_gears(c: tuple):
    coordinates = list()
    for i in range(c[0]-1, c[0]+2):
        for j in range(c[1]-1, c[1]+2):
            coordinates.append((i, j))
    return coordinates

def get_coo_of_numbers_around_gears(lines: list, g: tuple):
    num_coo = list()
    for x, y in g:
        if lines[x][y].isdigit():
            num_coo.append((x, y))
    return num_coo

def get_full_number(lines: list, c: tuple) -> int:
    x, y = c
    n = lines[x][y]
    for db in range(1,3):
        c = lines[x][y-db]
        if c.isdigit():
            n = f"{c}{n}"
        else:
            break
    for df in range(1,3):
        c = lines[x][y+df]
        if c.isdigit():
            n = f"{n}{c}"
        else:
            break
    return int(n)

if __name__ == "__main__":
    score = 0
    
    with open(IN_FILEPATH) as f:
        input = f.read()
    
    lines = input.split("\n")
    gears = get_gears_coordinates(lines)
    for g in gears:
        c = get_coordinates_around_gears(g)
        num_coos = get_coo_of_numbers_around_gears(lines, c)
        gear_ratios = []
        for co in num_coos:
            number = get_full_number(lines, co)
            gear_ratios.append(number)
        gear_ratios = list(set(gear_ratios))
        if len(gear_ratios) < 2:
            continue
        elif (len(gear_ratios)) > 2:
            raise ValueError("WTFFFFF")
        else:
            product = gear_ratios[0] * gear_ratios[1]
            score += product   
    print(score)