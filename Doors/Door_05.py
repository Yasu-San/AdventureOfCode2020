from typing import List


def solve() -> None:
    seats: List[int] = []

    with open("Input/Door_05.txt", 'r') as infile:
        for line in infile:
            min_row: int = 0
            max_row: int = 127
            min_col: int = 0
            max_col: int = 7
            for char in line:
                if char == "F":
                    max_row -= (max_row - min_row + 1) / 2
                elif char == "B":
                    min_row += (max_row - min_row + 1) / 2
                elif char == "L":
                    max_col -= (max_col - min_col + 1) / 2
                elif char == "R":
                    min_col += (max_col - min_col + 1) / 2

            seats.append(min_row * 8 + min_col)

    first(seats)
    second(seats)


def first(seats: List[int]) -> None:
    max_seat: int = 0

    for seat in seats:
        if seat > max_seat:
            max_seat = seat

    print("Door  5.1 | Max Seat-Number is {0}".format(max_seat))


def second(seats: List[int]) -> None:
    seats.sort()

    for i in range(1, len(seats) - 1):
        if seats[i - 1] + 2 == seats[i]:
            print("Door  5.2 | Own Seat-Number is {0}".format(seats[i] - 1))
            return

    print("Door  5.2 | Own Seat-Number is unknown")
