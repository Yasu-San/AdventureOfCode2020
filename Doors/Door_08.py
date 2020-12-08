from typing import List, Tuple


def solve() -> None:
    with open("Input/Door_08.txt", 'r') as infile:
        code: List[str] = infile.read().splitlines()

    first(code)
    second(code)


def first(code: List[str]) -> None:
    print("Door  8.1 | The Accumulator is at {0}".format(execute(code, [], 0, 0)[0]))


def second(code: List[str]) -> None:
    print("Door  8.2 | The Accumulator is at {0}".format(self_modifying_exex(code, [], 0, 0)))


def execute(code: List[str], already_executed: List[int], next_command: int, accumulator: int) -> Tuple[int, bool]:
    while next_command not in already_executed:
        already_executed.append(next_command)

        if next_command == len(code):
            return accumulator, True

        if code[next_command].startswith("nop"):
            next_command += 1
        elif code[next_command].startswith("acc +"):
            accumulator += int(code[next_command][5:])
            next_command += 1
        elif code[next_command].startswith("acc -"):
            accumulator -= int(code[next_command][5:])
            next_command += 1
        elif code[next_command].startswith("jmp +"):
            next_command += int(code[next_command][5:])
        elif code[next_command].startswith("jmp -"):
            next_command -= int(code[next_command][5:])

    return accumulator, False


def self_modifying_exex(code: List[str], already_executed: List[int], next_command: int, accumulator: int) -> Tuple[int, bool]:
    while next_command not in already_executed:
        already_executed.append(next_command)

        if next_command == len(code):
            return accumulator, True

        if code[next_command].startswith("nop +"):
            # Try as jmp
            alt_accumulator, success = execute(code, already_executed.copy(), next_command + int(code[next_command][5:]), accumulator)
            if success:
                return alt_accumulator, True

            # If failed continue as nop
            next_command += 1
        elif code[next_command].startswith("nop -"):
            # Try as jmp
            alt_accumulator, success = execute(code, already_executed.copy(), next_command - int(code[next_command][5:]), accumulator)
            if success:
                return alt_accumulator, True

            # If failed continue as nop
            next_command += 1
        elif code[next_command].startswith("acc +"):
            accumulator += int(code[next_command][5:])
            next_command += 1
        elif code[next_command].startswith("acc -"):
            accumulator -= int(code[next_command][5:])
            next_command += 1
        elif code[next_command].startswith("jmp +"):
            # Try as nop
            alt_accumulator, success = execute(code, already_executed.copy(), next_command + 1, accumulator)
            if success:
                return alt_accumulator, True

            # If failed continue as jmp
            next_command += int(code[next_command][5:])
        elif code[next_command].startswith("jmp -"):
            # Try as nop
            alt_accumulator, success = execute(code, already_executed.copy(), next_command + 1, accumulator)
            if success:
                return alt_accumulator, True

            # If failed continue as jmp
            next_command -= int(code[next_command][5:])

    return accumulator, False
