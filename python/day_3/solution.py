import os

def solve(banks, num_digits=12):
    total = 0
    for bank in banks:
        digits = [int(d) for d in bank if d.isdigit()]
        if len(digits) < num_digits:
            continue
        result = []
        start_idx = 0
        
        for pos in range(num_digits):
            # How many more digits do we need after this one?
            remaining_needed = num_digits - pos - 1
            
            # Latest index we can pick from while leaving enough digits
            search_until = len(digits) - remaining_needed
            
            # Find the maximum digit in the valid range
            max_digit = -1
            max_idx = -1
            for i in range(start_idx, search_until):
                if digits[i] > max_digit:
                    max_digit = digits[i]
                    max_idx = i
            
            result.append(max_digit)
            start_idx = max_idx + 1  # Next search starts after this digit
        
        number = int(''.join(map(str, result)))
        total += number
    return total

def main():
    banks = loadFile()
    result1 = solve(banks, 2)
    result2 = solve(banks, 12)
    
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


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
