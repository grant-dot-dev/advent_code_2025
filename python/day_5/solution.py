import os
def get_file_path(is_dev=True):
    base = os.path.dirname(os.path.abspath(__file__))
    filename = "example.txt" if is_dev else "input.txt"
    file_path = os.path.join(base, filename)
    return file_path


file_path = get_file_path(False)

def read_file():
    try:
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]
            fresh_ranges = []
            ids = []
            split_index = lines.index('') if '' in lines else len(lines)
            for line in lines[:split_index]:
                start, end = map(int, line.split('-'))
                fresh_ranges.append((start, end))
            for line in lines[split_index+1:]:
                if line:    
                    ids.append(int(line))
            return fresh_ranges, ids
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    
def part_1(fresh_ranges, ids):    
    fresh_ingredients = 0
    for id in ids:
        if any(start <= id <= end for start, end in fresh_ranges):
            fresh_ingredients += 1
    
    return fresh_ingredients

def part_2(fresh_ranges):
    # Sort ranges by start position
    sorted_ranges = sorted(fresh_ranges)
    
    # Merge overlapping ranges
    merged = []
    for start, end in sorted_ranges:
        print(merged)
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge with last range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # No overlap - add new range
            merged.append((start, end))
    
    # Calculate total count from merged ranges
    total_count = sum(end - start + 1 for start, end in merged)
    return total_count
    
def main():
    fresh_ranges, ids = read_file()
    result_1 = part_1(fresh_ranges, ids)
    result_2 = part_2(fresh_ranges)
    
    print(f'Part 1: {result_1}')
    print(f'Part 2: {result_2}')

if __name__ == '__main__':
    main()