from typing import List


def solve() -> None:
    with open("Input/Door_06.txt", 'r') as infile:
        answers: List[str] = infile.readlines()

    first(answers)
    second(answers)


def first(answers: List[str]) -> None:
    sum_questions: int = 0
    group_yes: List[str] = []

    for line in answers:
        if line == "\n":
            sum_questions += len(group_yes)
            group_yes = []
        else:
            for char in line:
                if char not in group_yes and char != "\n":
                    group_yes.append(char)

    sum_questions += len(group_yes)

    print("Door  6.1 | Sum of questions anyone answered yes in a group: {0}".format(sum_questions))


def second(answers: List[str]) -> None:
    sum_questions: int = 0
    group_yes: List[str] = []
    group_start: bool = True

    for line in answers:
        if line == "\n":
            sum_questions += len(group_yes)
            group_start = True
            group_yes = []
        else:
            if group_start:
                for char in line:
                    if char != "\n":
                        group_yes.append(char)

                group_start = False
            else:
                group_remove: List[str] = []
                for char in group_yes:
                    if char not in line:
                        group_remove.append(char)

                for char in group_remove:
                    group_yes.remove(char)

    sum_questions += len(group_yes)

    print("Door  6.2 | Sum of questions everyone answered yes in a group: {0}".format(sum_questions))
