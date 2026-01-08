import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(is_dev: bool) -> list:
    file_name = "input.txt" if not is_dev else "example.txt"
    with open(file_name, "r") as file:
        return file.read().strip().split('\n')

def get_terminal_size():
    """Get terminal height."""
    try:
        import shutil
        cols, rows = shutil.get_terminal_size()
        return rows, cols
    except:
        return 24, 80  # Default

def visualize_with_window(grid:  list, delay: float = 0.3):
    start_col = grid[0].index('S')
    active_beams = {start_col}
    beam_history = set()
    split_count = 0
    
    term_height, term_width = get_terminal_size()
    window_size = term_height - 8  # Leave room for header/footer
    
    for row_idx in range(len(grid)):
        clear_screen()
        
        # Calculate visible window
        window_start = max(0, row_idx - window_size // 2)
        window_end = min(len(grid), window_start + window_size)
        
        # Adjust if near end
        if window_end == len(grid):
            window_start = max(0, len(grid) - window_size)
        
        # Header
        print("=" * 60)
        print("  TACHYON BEAM SPLITTER SIMULATOR")
        print("=" * 60)
        print(f"Showing rows {window_start}-{window_end} of {len(grid)}")
        print()
        
        # Draw visible window
        for r in range(window_start, window_end):
            row_display = f"{r: 3d}:  "
            
            for c in range(len(grid[r])):
                char = grid[r][c]
                
                if r == row_idx and c in active_beams: 
                    if char == '^': 
                        row_display += '\033[1;91m█\033[0m'
                    else:
                        row_display += '\033[1;92m█\033[0m'
                elif (r, c) in beam_history:
                    row_display += '\033[2;36m·\033[0m'
                elif char == '^': 
                    row_display += '\033[33m^\033[0m'
                elif char == 'S':
                    row_display += '\033[1;35mS\033[0m'
                else:
                    row_display += char
            
            # Highlight current row
            if r == row_idx:
                row_display += "  ← ACTIVE"
            
            print(row_display)
        
        # Footer
        print()
        print("=" * 60)
        print(f"Row: {row_idx}/{len(grid)-1}  |  Beams: {sorted(active_beams)}  |  Splits: {split_count}")
        print("=" * 60)
        
        time.sleep(delay)
        
        # Update beams
        for col in active_beams: 
            beam_history.add((row_idx, col))
        
        if row_idx < len(grid) - 1:
            next_beams = set()
            for col in active_beams:
                if 0 <= col < len(grid[row_idx]):
                    cell = grid[row_idx][col]
                    if cell in '.S': 
                        next_beams. add(col)
                    elif cell == '^':
                        split_count += 1
                        if col - 1 >= 0:
                            next_beams.add(col - 1)
                        if col + 1 < len(grid[row_idx]):
                            next_beams.add(col + 1)
            active_beams = next_beams
            
            if not active_beams:
                break
    
    print(f"\n\033[1;92m✓ COMPLETE!  Total splits: {split_count}\033[0m\n")
    return split_count

if __name__ == "__main__": 
    grid = read_file(False)
    visualize_with_window(grid, delay=0.4)