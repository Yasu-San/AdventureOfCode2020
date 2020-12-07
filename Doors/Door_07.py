from typing import List, Iterator, Match, AnyStr, Tuple
import re


def solve() -> None:
    rules: dict = {}
    regex: str = r"^([a-z ]+) bags contain (([0-9]+ [a-z ]+ bags?(, )?)+|no other bags).$"

    with open("Input/Door_07.txt", 'r') as infile:
        matches: Iterator[Match[AnyStr]] = re.finditer(regex, infile.read(), re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            content: List[Tuple] = list(tuple())
            rule: str = match.group(2)
            if rule != "no other bags":
                bags: List[str] = rule.split(", ")
                inner_regex: str = r"^([0-9]+) ([a-z ]+) bags?$"

                for bag in bags:
                    inner_matches: Iterator[Match[AnyStr]] = re.finditer(inner_regex, bag)

                    for inner_matchNum, inner_match in enumerate(inner_matches, start=1):
                        content.append((int(inner_match.group(1)), inner_match.group(2)))

            rules[match.group(1)] = content

    first(rules)
    second(rules)


def first(rules: dict) -> None:
    can_contain: List[str] = []
    lookout: List[str] = ["shiny gold"]

    while len(lookout) > 0:
        look_for: str = lookout.pop(0)
        for outer_color in rules:
            for bag in rules[outer_color]:
                if look_for == bag[1]:
                    if outer_color not in can_contain:
                        lookout.append(outer_color)
                        can_contain.append(outer_color)
    print("Door  7.1 | Could be in {0} different colored bags.".format(len(can_contain)))


def second(rules: dict) -> None:
    print("Door  7.2 | There are {0} bags inside one shiny gold bag.".format(nested_bags(rules, "shiny gold") - 1))


def nested_bags(rules: dict, outer_bag: str) -> int:
    bags: int = 1

    for bag in rules[outer_bag]:
        bags += bag[0] * nested_bags(rules, bag[1])

    return bags
