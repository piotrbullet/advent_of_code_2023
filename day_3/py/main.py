import re

def get_indexes_to_check(line_index, m_start, m_end):
    indexes_to_check = list()
    if not m_start < 0:
        indexes_to_check.append((line_index, m_start-1))
    if not m_end > 139:
        indexes_to_check.append((line_index, m_end))
    for j in range(m_start-1, m_end+1):
        if j < 0 or j > 139:
            continue
        indexes_to_check.append((line_index-1, j))
        indexes_to_check.append((line_index+1, j))
    return indexes_to_check

if __name__ == "__main__":
    
    total: int = 0
    
    with open("day_3/input.txt") as f:
        input = f.read()
    
    lines = input.split("\n")
    
    for i, line in enumerate(lines):
        matches = [(m.start(0), m.end(0)) for m in re.finditer("\d+", line)]
        for m_start, m_end in matches:
            indexes_to_check = get_indexes_to_check(i, m_start, m_end)
            adjacent_chars = list()
            for ind in indexes_to_check:
                try:
                    adjacent_chars.append(lines[ind[0]][ind[1]])
                except:
                    pass
            
            if all([a=="." or a.isdigit() for a in adjacent_chars]):
                continue
            else:
                match_number = int(lines[i][m_start:m_end])
                total += match_number
    
    print(f"PART ONE: {total}")
