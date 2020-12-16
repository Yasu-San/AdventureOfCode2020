import re
from typing import List, Iterable


def solve() -> None:
    rules: dict = {}
    own: List[int] = []
    other: List[List[int]] = []

    with open("Input/Door_16.txt", 'r') as infile:
        content: str = infile.read()

    rule_exp: str = r"^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$"
    rule_matches = re.finditer(rule_exp, content, re.MULTILINE)

    for rule_num, rule_match in enumerate(rule_matches, start=1):
        rules[rule_match.group(1)] = [
            {"min": int(rule_match.group(2)), "max": int(rule_match.group(3))},
            {"min": int(rule_match.group(4)), "max": int(rule_match.group(5))}
        ]

    own_exp: str = r"^your ticket:\n((?:[0-9]+,?)+)$"
    own_matches = re.finditer(own_exp, content, re.MULTILINE)

    for own_num, own_match in enumerate(own_matches, start=1):
        for part in own_match.group(1).split(","):
            own.append(int(part))

    other_exp: str = r"^nearby tickets:\n((?:(?:[0-9]+,?)+\n?)+)$"
    other_matches = re.finditer(other_exp, content, re.MULTILINE)

    for other_num, other_match in enumerate(other_matches, start=1):
        for ticket in other_match.group(1).splitlines():
            other_ticket: List[int] = []

            for part in ticket.split(","):
                other_ticket.append(int(part))

            other.append(other_ticket)

    validated: List[List[int]] = first(rules, other)
    second(rules, validated, own)


def first(rules: dict, other: List[List[int]]) -> List[List[int]]:
    error_rate: int = 0
    validated: List[List[int]] = []

    for ticket in other:
        ticket_success: bool = True

        for part in ticket:
            for rule in rules:
                if rules[rule][0]["min"] <= part <= rules[rule][0]["max"] or rules[rule][1]["min"] <= part <= rules[rule][1]["max"]:
                    break
            else:
                error_rate += part
                ticket_success = False

        if ticket_success:
            validated.append(ticket)

    print("Door 16.1 | Scanning Error Rate: {0}".format(error_rate))

    return validated


def second(rules: dict, other: List[List[int]], own: List[int]) -> None:
    possible: dict = {}

    for rule in rules:
        possible[rule] = list(range(len(own)))

    for ticket in other:
        for i in range(len(ticket)):
            for rule in rules:
                if i in possible[rule]:
                    if not (rules[rule][0]["min"] <= ticket[i] <= rules[rule][0]["max"] or rules[rule][1]["min"] <= ticket[i] <= rules[rule][1]["max"]):
                        possible[rule].remove(i)

    while not max_len_of_items(possible, 1):
        for rule in possible:
            if len(possible[rule]) == 1:
                for i in possible:
                    if rule != i:
                        if possible[rule][0] in possible[i]:
                            possible[i].remove(possible[rule][0])

    solution: int = 1

    for item in possible:
        if item.startswith("departure"):
            solution *= own[possible[item][0]]

    print("Door 16.2 | Solution is {0}".format(solution))


def max_len_of_items(iter: dict, max_len: int) -> bool:
    for item in iter:
        if len(iter[item]) > max_len:
            return False

    return True
