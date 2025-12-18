import os

def part1(banks):
    total = 0
    for bank in banks:
        digits = [int(d) for d in bank if d.isdigit()]
        if len(digits) < 2:
            continue
        
        max_combined = 0
        # Try each position as the first digit
        for i in range(len(digits) - 1):
            first = digits[i]
            second = max(digits[i+1:])  # Max digit after position i
            combined = int(f"{first}{second}")
            max_combined = max(max_combined, combined)
        
        print(max_combined)
        total += max_combined
    return total

def main():
    banks = loadFile()
    result1 = part1(banks)
    
    print(f"Part 1: {result1}")


def loadFile():
    is_dev = False
    base = os.path.dirname(__file__)
    filename = "example.txt" if is_dev else "input.txt"
    file_path = os.path.join(base, filename)
    
    try:
        with open(file_path, "r") as f:
            banks = [line.rstrip('\n') for line in f]
        return banks
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []


main()
