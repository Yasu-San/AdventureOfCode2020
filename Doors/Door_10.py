from functools import cache
from typing import List

adapters: List[int] = []


def solve() -> None:
    with open("Input/Door_10.txt", 'r') as infile:
        for line in infile:
            adapters.append(int(line))

    adapters.sort()

    first()
    second()


def first() -> None:
    last_rating: int = 0
    ones: int = 0
    threes: int = 0

    for adapter in adapters:
        if adapter == last_rating + 1:
            ones += 1
            last_rating = adapter
        elif adapter == last_rating + 2:
            last_rating = adapter
        elif adapter == last_rating + 3:
            threes += 1
            last_rating = adapter
        else:
            break

    # Devices internal difference
    threes += 1
    print("Door 10.1 | Solution {0}".format(ones * threes))


@cache
def traverse(index: int, rating: int, goal: int) -> int:
    possibilities: int = 0

    if rating == goal:
        return 1
    else:
        while index < len(adapters) and adapters[index] <= rating + 3:
            possibilities += traverse(index + 1, adapters[index], goal)
            index += 1

        return possibilities


def second() -> None:
    print("Door 10.2 | There are {0} possibilities".format(traverse(0, 0, adapters[len(adapters) - 1])))
