import os

def solve_part2(lines):
    # Convert strings to mutable lists
    lines = [list(line) for line in lines]
    total_rolls = 0
    
    # Keep removing rolls until no more can be removed
    while True:
        removed_this_round = []
        
        # Find all rolls that can be removed (have < 4 adjacent '@' neighbors)
        for line_idx, line in enumerate(lines):
            for char_idx, char in enumerate(line):
                if char != "@":
                    continue

                # Count adjacent '@' in all 8 directions
                directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1),
                ]
                count = 0
                for dx, dy in directions:
                    x, y = char_idx + dx, line_idx + dy
                    if 0 <= y < len(lines) and 0 <= x < len(lines[y]):
                        if lines[y][x] == "@":
                            count += 1
                
                # If less than 4 neighbors, this roll can be removed
                if count < 4:
                    removed_this_round.append((line_idx, char_idx))
        
        # If nothing was removed this round, we're done
        if not removed_this_round:
            break
        
        # Remove all the rolls found in this iteration
        for line_idx, char_idx in removed_this_round:
            lines[line_idx][char_idx] = "."
            total_rolls += 1

    return total_rolls


def main():
    lines = loadFile()
    # Make copies so each part has fresh data
    part2_result = solve_part2(lines.copy())
    print(f"Result Part 2: {part2_result}")


def loadFile():
    is_dev = True
    base = os.path.dirname(__file__)
    filename = "example.txt" if is_dev else "input.txt"
    file_path = os.path.join(base, filename)

    try:
        with open(file_path, "r") as f:
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


main()
