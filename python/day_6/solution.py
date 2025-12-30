import os
from typing import List
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
            
            # Separate numeric lines from operator lines
            numeric_lines = []
            operator_lines = []
            
            for line in lines:
                if any(char.isdigit() for char in line):
                    numeric_lines.append(line)
                else:
                    operator_lines.append(line)
            
            # Parse columns from numeric lines
            columns = [list(map(int, col)) for col in zip(*(line.split() for line in numeric_lines))]
            
            operators = operator_lines[0].split() if operator_lines else []
            
            return columns, operators
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return [], []
    except ValueError as e:
        print(f"Error parsing file: {e}")
        return [], []
 
columns, operators = read_file()

def apply_operator(grand_total, op:str, column:List[int]):
    if op == '+':
        grand_total += sum(column)
    elif op == '-':
        grand_total += column[0] - sum(column[1:])
    elif op == '*':
        prod = 1
        for num in column:
            prod *= num
        grand_total += prod
    elif op == '/':
        result = column[0]
        for num in column[1:]:
            if num == 0:
                print("Division by zero encountered.")
                result = 0
                break
            result /= num
        grand_total += result
    
    return grand_total  # Add this!

def part_1():
    grand_total = 0
    for idx, column in enumerate(columns):
        new_total = apply_operator(grand_total, operators[idx],column)
        grand_total = new_total
    return grand_total

print(part_1())