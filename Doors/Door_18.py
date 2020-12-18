from typing import List, Tuple, Union


def solve() -> None:
    with open("Input/Door_18.txt", 'r') as infile:
        calculations: List[str] = infile.read().splitlines()

    first(calculations)
    second(calculations)


def apply(num1: int, operation: str, num2: str) -> int:
    if num2 != "":
        if operation == "+":
            num1 += int(num2)
        elif operation == "*":
            num1 *= int(num2)
        elif operation == "":
            num1 = int(num2)

    return num1


def calculate(calculation: str, index: int = 0) -> Union[int, Tuple[int, int]]:
    current_num: int = 0
    next_operation: str = ""
    next_num: str = ""

    while index < len(calculation):
        if calculation[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            next_num += calculation[index]
        elif calculation[index] in ["+", "*"]:
            current_num = apply(current_num, next_operation, next_num)
            next_operation = calculation[index]
            next_num = ""
        elif calculation[index] == "(":
            inner_calc, index = calculate(calculation, index + 1)
            current_num = apply(current_num, next_operation, inner_calc)
        elif calculation[index] == ")":
            current_num = apply(current_num, next_operation, next_num)
            return current_num, index

        index += 1

    return apply(current_num, next_operation, next_num)


def enqueued_calculate(calculation: str, index: int = 0) -> Union[int, Tuple[int, int]]:
    enqueued_calculation: str = ""
    current_num: int = 0
    next_operation: str = ""
    next_num: str = ""

    while index < len(calculation):
        if calculation[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            next_num += calculation[index]
        elif calculation[index] == "+":
            current_num = apply(current_num, next_operation, next_num)
            next_operation = "+"
            next_num = ""
        elif calculation[index] == "*":
            current_num = apply(current_num, next_operation, next_num)
            next_num = ""
            enqueued_calculation += "{0} * ".format(current_num)
            current_num = 0
        elif calculation[index] == "(":
            inner_calc, index = enqueued_calculate(calculation, index + 1)
            current_num = apply(current_num, next_operation, inner_calc)
        elif calculation[index] == ")":
            if next_operation == "+":
                current_num = apply(current_num, next_operation, next_num)
                next_num = ""

            if next_num != "":
                enqueued_calculation += next_num
            else:
                enqueued_calculation += "{0}".format(current_num)

            return calculate(enqueued_calculation), index

        index += 1

    if next_operation == "+":
        current_num = apply(current_num, next_operation, next_num)
        next_num = ""

    if next_num != "":
        enqueued_calculation += next_num
    else:
        enqueued_calculation += "{0}".format(current_num)

    return calculate(enqueued_calculation)


def first(calculations: List[str]) -> None:
    solution: int = 0

    for calculation in calculations:
        solution += calculate(calculation)

    print("Door 18.1 | The sum of all solutions is {0}".format(solution))


def second(calculations: List[str]) -> None:
    solution: int = 0

    for calculation in calculations:
        solution += enqueued_calculate(calculation)

    print("Door 18.2 | The sum of all solutions is {0}".format(solution))
