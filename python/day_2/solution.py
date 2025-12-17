import os
import time


def load_input(file_path):
    with open(file_path, "r") as file:
        text = file.read().strip()
    if not text:
        return []
    # split by comma or newline, strip each entry, ignore empties
    parts = []
    for token in text.replace("\\n", ",").split(","):
        token = token.strip()
        if token:
            parts.append(token)
    return parts


def is_invalid_part1(s):
    """Check if string is a sequence repeated exactly twice."""
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return s[:mid] == s[mid:]
    return False


def is_invalid_part2(s):
    """Check if string is a sequence repeated at least twice."""
    n = len(s)
    # Try all possible pattern lengths that divide n evenly
    for pattern_len in range(1, n):
        if n % pattern_len == 0:  # Pattern must divide evenly
            repeats = n // pattern_len
            if repeats >= 2:  # Must repeat at least twice
                pattern = s[:pattern_len]
                if pattern * repeats == s:
                    return True
    return False


def parse_input(idRange, part=1):
    first = idRange.split("-")[0]
    last = idRange.split("-")[1]
    total = 0
    start = int(first)
    end = int(last)

    check_fn = is_invalid_part1 if part == 1 else is_invalid_part2

    for num in range(start, end + 1):
        s = str(num)
        if check_fn(s):
            total += num
    return total


def main():
    is_development = False
    base = os.path.dirname(__file__)
    file_path = (
        os.path.join(base, "input.txt")
        if not is_development
        else os.path.join(base, "example.txt")
    )
    
    ranges = load_input(file_path)
    
    # Part 1
    total1 = 0
    for r in ranges:
        result = parse_input(r, part=1)
        total1 += result
    print(f"Part 1: Sum of invalid IDs: {total1}")
    
    # Part 2
    total2 = 0
    for r in ranges:
        result = parse_input(r, part=2)
        total2 += result
    print(f"Part 2: Sum of invalid IDs: {total2}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
