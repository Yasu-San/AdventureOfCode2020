from functools import cache
from typing import List, Match
import re


def solve() -> None:
    with open("Input/Door_14.txt", 'r') as infile:
        content: List[str] = infile.read().splitlines()

    first(content)
    second(content)


def first(content: List[str]) -> None:
    line_number: int = 0

    memory: dict = {}
    regex = r"^mem\[([0-9]+)\] = ([0-9]+)$"

    while line_number < len(content):
        raw_mask: str = content[line_number][7:]
        mask: dict = {}

        for i in range(0, len(raw_mask)):
            if raw_mask[i] != "X":
                mask[i] = raw_mask[i]

        line_number += 1

        while line_number < len(content):
            match: Match = re.fullmatch(regex, content[line_number])

            if match is not None:
                index: int = int(match.group(1))
                value: List[str] = list('{0:036b}'.format(int(match.group(2))))

                for position, replacer in mask.items():
                    value[position] = replacer

                memory[index] = int("".join(value), 2)
                line_number += 1
            else:
                break

    solution: int = 0

    for index, element in memory.items():
        solution += element

    print("Door 14.1 | Solution: {0}".format(solution))


@cache
def apply_index_mask(index: str, mask: str) -> List[str]:
    addresses: List[str] = []
    address: List[str] = list(index)

    for i in range(0, len(index)):
        if mask[i] == "1":
            address[i] = "1"
        elif mask[i] == "X":
            if i < len(index) - 1:
                suffixes: List[str] = apply_index_mask("".join(address[i + 1:]), mask[i + 1:])
                for suffix in suffixes:
                    addresses.append("".join(address[:i]) + "0" + suffix)
                    addresses.append("".join(address[:i]) + "1" + suffix)
            else:
                addresses.append("".join(address[:i]) + "0")
                addresses.append("".join(address[:i]) + "1")
            break

    if len(addresses) == 0:
        addresses.append("".join(address))

    return addresses


def second(content: List[str]) -> None:
    line_number: int = 0

    memory: dict = {}
    regex = r"^mem\[([0-9]+)\] = ([0-9]+)$"

    while line_number < len(content):
        mask: str = content[line_number][7:]
        line_number += 1

        while line_number < len(content):
            match: Match = re.fullmatch(regex, content[line_number])

            if match is not None:
                index: str = '{0:036b}'.format(int(match.group(1)))
                value: int = int(match.group(2))

                addresses: List[str] = apply_index_mask(index, mask)

                for address in addresses:
                    memory[address] = value

                line_number += 1
            else:
                break

    solution: int = 0

    for index, element in memory.items():
        solution += element

    print("Door 14.2 | Solution: {0}".format(solution))
