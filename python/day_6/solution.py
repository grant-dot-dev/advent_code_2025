import time

def read_file() -> list:
    """Read input file and parse into a table structure."""
    table = []
    
    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            data = line.strip().split()
            
            for j, element in enumerate(data):
                if i == 0:
                    table.append([])
                
                # Convert to int if not an operator
                value = element if element in ["+", "*"] else int(element)
                table[j].append(value)
    
    return table

def part1_func(table: list) -> int:
    """Calculate sum based on column operations."""
    total = 0
    
    for column in table: 
        operator = column[-1]
        numbers = [x for x in column if x not in ["+", "*"]]
        
        if operator == "*":
            product = 1
            for num in numbers:
                product *= num
            total += product
        else:   # operator == "+"
            total += sum(numbers)
    
    return total

def part2_func() -> int:
    """Calculate sum with character-by-character processing."""
    total = 0
    table = []
    
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
        # Build the table (all lines except the last)
        for line in lines[:-1]:
            for i, char in enumerate(line):
                if len(table) <= i:
                    table.append([])
                table[i]. append(char)
        
        # Process the final line
        operator_line = lines[-1]
        is_add = True
        product = 0
        
        for i, char in enumerate(operator_line):
            if char == "+":
                if not is_add:
                    total += product
                is_add = True
            elif char == "*":
                if not is_add:
                    total += product
                is_add = False
                product = 1
            
            if is_add and char != "\n":
                # Extract number from column
                num_str = "".join(digit for digit in table[i] if digit != " ")
                if num_str:
                    total += int(num_str)
            elif char != "\n":
                # Extract number from column
                num_str = "".join(digit for digit in table[i] if digit != " ")
                if num_str: 
                    product *= int(num_str)
        
        # Add final product if we were multiplying
        if not is_add:
            total += product
    
    return total

def main():
    start_time = time.perf_counter()
    
    table = read_file()
    part1 = part1_func(table)
    part2 = part2_func()
    
    end_time = time.perf_counter()
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    print(f"Solution time:  {end_time - start_time}")

if __name__ == "__main__":
    main()