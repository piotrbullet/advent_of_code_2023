import re

DIGITS_SPELLED: dict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

if __name__ == "__main__":
    with open("F:/Projects/advent_of_code_2023/day_1/input.txt") as f:
        text = f.read()
    
    total_score: int = 0
    
    for line in text.split("\n"):
        digits = re.findall("\d", line)
        total_score += int(f"{digits[0]}{digits[-1]}")
    
    print(f"PART 1 score: {total_score}")
    
    text_p2 = text
    
    for key in DIGITS_SPELLED:
        text_p2 = text_p2.replace(key, str(DIGITS_SPELLED[key]))
    
    total_score: int = 0
    
    for line in text_p2.split("\n"):
        digits = re.findall("\d", line)
        total_score += int(f"{digits[0]}{digits[-1]}")
    
    print(f"PART 2 score: {total_score}")
    