import copy
from typing import List


def solve() -> None:
    original_seats: List[List[str]] = []

    with open("Input/Door_11.txt", 'r') as infile:
        for line in infile:
            seat_row: List[str] = []

            for char in line:
                if char in ['.', '#', 'L']:
                    seat_row.append(char)

            original_seats.append(seat_row)

    first(copy.deepcopy(original_seats))
    second(copy.deepcopy(original_seats))


def test_seat(seats: List[List[str]], x: int, y: int) -> int:
    occupied: int = 0

    for cx in range(x - 1, x + 2):
        for cy in range(y - 1, y + 2):
            if (cx != x or cy != y) and 0 <= cx < len(seats) and 0 <= cy < len(seats[0]):
                if seats[cx][cy] == "#":
                    occupied += 1

    return occupied


def test_advanced_seat(seats: List[List[str]], x: int, y: int) -> int:
    occupied: int = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                cx: int = x + dx
                cy: int = y + dy

                while 0 <= cx < len(seats) and 0 <= cy < len(seats[0]):
                    if seats[cx][cy] == "#":
                        occupied += 1

                    if seats[cx][cy] != ".":
                        break

                    cx += dx
                    cy += dy

    return occupied


def apply_rules(seats: List[List[str]]) -> List[List[str]]:
    new_seats = copy.deepcopy(seats)

    for x in range(0, len(seats)):
        for y in range(0, len(seats[x])):
            occupied: int = test_seat(seats, x, y)

            if seats[x][y] == "L" and occupied == 0:
                new_seats[x][y] = "#"
            elif seats[x][y] == "#" and occupied >= 4:
                new_seats[x][y] = "L"

    return new_seats


def apply_advanced_rules(seats: List[List[str]]) -> List[List[str]]:
    new_seats = copy.deepcopy(seats)

    for x in range(0, len(seats)):
        for y in range(0, len(seats[x])):
            occupied: int = test_advanced_seat(seats, x, y)

            if seats[x][y] == "L" and occupied == 0:
                new_seats[x][y] = "#"
            elif seats[x][y] == "#" and occupied >= 5:
                new_seats[x][y] = "L"

    return new_seats


def count_occupied(seats: List[List[str]]) -> int:
    occupied: int = 0

    for x in seats:
        for y in x:
            if y == "#":
                occupied += 1

    return occupied


def first(seats: List[List[str]]) -> None:
    new_seats: List[List[str]] = copy.deepcopy(seats)
    first_loop: bool = True

    while seats != new_seats or first_loop:
        first_loop = False
        seats = copy.deepcopy(new_seats)
        new_seats = apply_rules(seats)

    print("Door 11.1 | {0} Seats are occupied".format(count_occupied(seats)))


def second(seats: List[List[str]]) -> None:
    new_seats: List[List[str]] = copy.deepcopy(seats)
    first_loop: bool = True

    while seats != new_seats or first_loop:
        first_loop = False
        seats = copy.deepcopy(new_seats)
        new_seats = apply_advanced_rules(seats)

    print("Door 11.2 | {0} Seats are occupied".format(count_occupied(seats)))
