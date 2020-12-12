from enum import Enum
from typing import List

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def solve() -> None:
    with open("Input/Door_12.txt", 'r') as infile:
        instructions: List[str] = infile.read().splitlines()

    first(instructions)
    second(instructions)


def first(instructions: List[str]) -> None:
    east: int = 0
    south: int = 0

    facing: Direction = Direction.EAST

    for instruction in instructions:
        if instruction.startswith("N") or (instruction.startswith("F") and facing == Direction.NORTH):
            south -= int(instruction[1:])
        elif instruction.startswith("S") or (instruction.startswith("F") and facing == Direction.SOUTH):
            south += int(instruction[1:])
        elif instruction.startswith("E") or (instruction.startswith("F") and facing == Direction.EAST):
            east += int(instruction[1:])
        elif instruction.startswith("W") or (instruction.startswith("F") and facing == Direction.WEST):
            east -= int(instruction[1:])
        else:
            degree: int = int(instruction[1:])
            degree %= 360

            if (degree == 90 and instruction.startswith("L")) or (degree == 270 and instruction.startswith("R")):
                facing = Direction((facing.value + 3) % 4)
            elif degree == 180:
                facing = Direction((facing.value + 2) % 4)
            elif (degree == 270 and instruction.startswith("L")) or (degree == 90 and instruction.startswith("R")):
                facing = Direction((facing.value + 1) % 4)

    print("Door 12.1 | Manhattan Distance: {0}".format(abs(east) + abs(south)))


def second(instructions: List[str]) -> None:
    waypoint_east: int = 10
    waypoint_south: int = -1

    ship_east: int = 0
    ship_south: int = 0

    for instruction in instructions:
        if instruction.startswith("N"):
            waypoint_south -= int(instruction[1:])
        elif instruction.startswith("S"):
            waypoint_south += int(instruction[1:])
        elif instruction.startswith("E"):
            waypoint_east += int(instruction[1:])
        elif instruction.startswith("W"):
            waypoint_east -= int(instruction[1:])
        elif instruction.startswith("F"):
            multiply: int = int(instruction[1:])
            ship_east += waypoint_east * multiply
            ship_south += waypoint_south * multiply
        else:
            degree: int = int(instruction[1:])
            degree %= 360

            if (degree == 90 and instruction.startswith("L")) or (degree == 270 and instruction.startswith("R")):
                waypoint_east, waypoint_south = waypoint_south, -waypoint_east
            elif degree == 180:
                waypoint_east, waypoint_south = -waypoint_east, -waypoint_south
            elif (degree == 270 and instruction.startswith("L")) or (degree == 90 and instruction.startswith("R")):
                waypoint_east, waypoint_south = -waypoint_south, waypoint_east

    print("Door 12.2 | Manhattan Distance: {0}".format(abs(ship_east) + abs(ship_south)))
