import time
import os


def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def rotate_dial(current: int, rotation: str):
    dir_change = str(rotation[0]).upper()
    amount = int(rotation[1:])
    delta: int = amount if dir_change == 'R' else -amount
    return (current + delta) % 100


def rotate_and_count_passes(current: int, rotation: str):
    dir_change = str(rotation[0]).upper()
    amount = int(rotation[1:])
    delta = amount if dir_change == 'R' else -amount

    # new position by modulo
    new_pos = (current + delta) % 100

    if delta == 0:
        return new_pos, 0

    if delta > 0:
        passes = (current + delta) // 100
    else:
        abs = -delta
        if current == 0:
            passes = abs // 100
        else:
            if abs < current:
                passes = 0
            else:
                passes = ((abs - current) // 100) + 1

    return new_pos, passes


def part2(start: int, moves) -> int:
    pos = start
    total = 0
    for m in moves:
        pos, passes = rotate_and_count_passes(pos, m)
        total += passes
    return total


def part1(start, moves):
    counter = 0
    pos = start
    for m in moves:
        pos = rotate_dial(pos, m)
        if pos == 0:
            counter += 1
    return counter


def main():
    is_development = False
    base = os.path.dirname(__file__)
    file_path = os.path.join(
        base, "input.txt") if not is_development else os.path.join(base, "example.txt")

    coordinates = load_input(file_path) if os.path.exists(file_path) else []

    # part 1 = count the times lands on zero
    result = part1(50, coordinates)

    # part 2 - count the number of times it passes 0
    passes = part2(50, coordinates)

    print(f"Times hit 0 (landings): {result}")
    print(f"Times passing through 0 (including wraps): {passes}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
