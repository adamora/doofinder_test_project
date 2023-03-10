# BOAT structure. Every list is called 'position', and every element inside a position is a 'box'
from typing import List

BOAT: List[List[str]] = [
    ['S', 'L', 'W'],
    ['J', 'T', 'N', 'Q'],
    ['S', 'C', 'H', 'F', 'J'],
    ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
    ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
    ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
    ['D', 'W', 'R', 'N', 'J', 'M'],
    ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
    ['H', 'L', 'Q', 'N', 'B', 'F', 'T'],
]


def move(box_num: int, position_1: int, position_2: int) -> None:
    """Move elements in BOAT. This will work at memory level (no need returns)"""
    for i in range(box_num):
        val = BOAT[position_1].pop(-1)
        BOAT[position_2].append(val)


def normalize_position(value: int) -> int:
    """Normalize position values"""
    return value - 1


def read_input(file_name: str = 'prueba_hiring_input.txt') -> List[str]:
    """Parse file content into list"""
    with open(file_name) as file_in:
        lines = [line for line in file_in]
    return lines


def process_input(lines: List[str]) -> List[List[int]]:
    """Will process text lines into list of values (box, original position and destiny position respectively)"""
    result = []
    for line in lines:
        words = line.split()
        origin_pos = normalize_position(int(words[3]))
        destiny_pos = normalize_position(int(words[5]))
        box = int(words[1])
        result.append([box, origin_pos, destiny_pos])
    return result


def move_boxes(processed_input: List[List[int]]) -> None:
    """Move boxes based on input values"""
    for box, origin_pos, destiny_pos in processed_input:
        move(box, origin_pos, destiny_pos)


if __name__ == '__main__':
    """Main method to get expected word"""

    print(f'ORIGINAL WORD: {"".join([i[-1] for i in BOAT])}')

    input_lines = read_input('prueba_hiring_input.txt')
    processed_input = process_input(input_lines)
    move_boxes(processed_input)

    print(f'FINAL WORD: {"".join([i[-1] for i in BOAT])}')
