from functools import reduce
from typing import List


def solve() -> None:

    with open("Input/Door_13.txt", 'r') as infile:
        content: List[str] = infile.read().splitlines()
        current_timestamp: int = int(content[0])
        bus_lines: List[str] = content[1].split(",")

    first(current_timestamp, bus_lines)
    second(bus_lines)


def first(current_timestamp: int, bus_lines: List[str]) -> None:
    test_timestamp: int = current_timestamp - 1
    use_line: int = -1

    while use_line == -1:
        test_timestamp += 1
        for line in bus_lines:
            if line != "x":
                if test_timestamp % int(line) == 0:
                    use_line = int(line)

    print("Door 13.1 | Use Line {0} in {1} minute(s) | Solution: {2}".format(use_line, (test_timestamp - current_timestamp),
                                                                             use_line * (test_timestamp - current_timestamp)))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def second(bus_lines: List[str]) -> None:
    lines: List[int] = []
    timings: List[int] = []

    index: int = 0

    for bus_line in bus_lines:
        if bus_line != "x":
            lines.append(int(bus_line))
            timings.append(-index % int(bus_line) + int(bus_line))
        index += 1

    print("Door 13.2 | Solution: {0}".format(chinese_remainder(lines, timings)))
