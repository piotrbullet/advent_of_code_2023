import re

INPUT: str = "day_5/input.txt"
EXAMPLE: str = "day_5/example.txt"

def part_1(filepath: str):
    with open(filepath) as f:
        text = f.read()
    
    score: int = 0
    
    parts = text.split("\n\n")
    [print(f"--\n{part}--\n") for part in parts]
    
if __name__ == "__main__":
    part_1(EXAMPLE)