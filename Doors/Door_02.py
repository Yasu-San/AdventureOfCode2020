from typing import List
import re


class PasswordWithPolicy:
    first_num: int
    second_num: int
    character: str
    password: str

    def __init__(self, first_num: int, second_num: int, character: str, password: str):
        self.first_num = first_num
        self.second_num = second_num
        self.character = character
        self.password = password


def solve():
    passwords: List[PasswordWithPolicy] = []
    regex: str = r"^([0-9]+)-([0-9]+) (.*?): (.*)$"

    with open("Input/Door_02.txt", 'r') as content:
        matches = re.finditer(regex, content.read(), re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            passwords.append(PasswordWithPolicy(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)))

    first(passwords)
    second(passwords)


def first(passwords: List[PasswordWithPolicy]):
    accepted: int = 0

    for entry in passwords:
        occurrences = entry.password.count(entry.character)
        if entry.first_num <= occurrences <= entry.second_num:
            accepted += 1

    print("Door  2.1 | {0} passwords accepted".format(accepted))


def second(passwords: List[PasswordWithPolicy]):
    accepted: int = 0

    for entry in passwords:
        try:
            if (entry.password[entry.first_num - 1] == entry.character and entry.password[entry.second_num - 1] != entry.character) or \
                    (entry.password[entry.first_num - 1] != entry.character and entry.password[entry.second_num - 1] == entry.character):
                accepted += 1
        except IndexError:
            print("ERROR | {0}-{1} {2}: {3}".format(entry.first_num, entry.second_num, entry.character, entry.password))

    print("Door  2.2 | {0} passwords accepted".format(accepted))
