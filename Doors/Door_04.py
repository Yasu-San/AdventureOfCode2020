from typing import List, Pattern
import re


def solve() -> None:
    with open("Input/Door_04.txt", 'r') as content:
        passports: str = content.read()

    first(passports)
    second(passports)


def first(passports: str) -> None:
    byr: bool = False
    iyr: bool = False
    eyr: bool = False
    hgt: bool = False
    hcl: bool = False
    ecl: bool = False
    pid: bool = False
    valid: int = 0
    lines: List[str] = passports.split("\n")

    for line in lines:
        if line == "":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                valid += 1
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
            elements: List[str] = line.split(" ")
            for element in elements:
                field: str = element.split(":")[0]
                if field == "byr":
                    byr = True
                elif field == "iyr":
                    iyr = True
                elif field == "eyr":
                    eyr = True
                elif field == "hgt":
                    hgt = True
                elif field == "hcl":
                    hcl = True
                elif field == "ecl":
                    ecl = True
                elif field == "pid":
                    pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1

    print("Door  4.1 | {0} Passports are valid (excluding cid)".format(valid))


def second(passports: str) -> None:
    hcl_pattern: Pattern = re.compile("^#[0-9a-f]{6}$")
    pid_pattern: Pattern = re.compile("^[0-9]{9}$")
    byr: bool = False
    iyr: bool = False
    eyr: bool = False
    hgt: bool = False
    hcl: bool = False
    ecl: bool = False
    pid: bool = False
    valid: int = 0
    lines: List[str] = passports.split("\n")

    for line in lines:
        if line == "":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                valid += 1
            byr = False
            iyr = False
            eyr = False
            hgt = False
            hcl = False
            ecl = False
            pid = False
        else:
            elements: List[str] = line.split(" ")
            for element in elements:
                field: List[str] = element.split(":")
                if field[0] == "byr" and 1920 <= int(field[1]) <= 2002:
                    byr = True
                elif field[0] == "iyr" and 2010 <= int(field[1]) <= 2020:
                    iyr = True
                elif field[0] == "eyr" and 2020 <= int(field[1]) <= 2030:
                    eyr = True
                elif field[0] == "hgt":
                    if field[1].endswith("cm"):
                        if 150 <= int(field[1].replace("cm", "")) <= 193:
                            hgt = True
                    elif field[1].endswith("in"):
                        if 59 <= int(field[1].replace("in", "")) <= 76:
                            hgt = True
                elif field[0] == "hcl" and hcl_pattern.match(field[1]):
                    hcl = True
                elif field[0] == "ecl" and field[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    ecl = True
                elif field[0] == "pid" and pid_pattern.match(field[1]):
                    pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1

    print("Door  4.2 | {0} Passports are valid (excluding cid)".format(valid))
