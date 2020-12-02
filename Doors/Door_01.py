from typing import List


def solve():
    numbers: List[int] = []

    with open("Input/Door_01.txt", 'r') as infile:
        for line in infile:
            numbers.append(int(line))

    first(numbers)
    second(numbers)


def first(numbers: List[int]):
    for num in numbers:
        for num2 in numbers:
            if num + num2 == 2020:
                print("Door  1.1 | {0} * {1} = {2}".format(num, num2, num * num2))
                return


def second(numbers: List[int]):
    for num in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num + num2 + num3 == 2020:
                    print("Door  1.2 | {0} * {1} * {2} = {3}".format(num, num2, num3, num * num2 * num3))
                    return
