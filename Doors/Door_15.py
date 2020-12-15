from typing import List


def solve() -> None:
    numbers: List[int] = []

    with open("Input/Door_15.txt", 'r') as infile:
        shards: List[str] = infile.read().split(",")

    for shard in shards:
        numbers.append(int(shard))

    calculate(numbers, 2020)
    calculate(numbers, 30000000)


def calculate(numbers: List[int], turns: int) -> None:
    turn: int = len(numbers)
    indices: dict = {}

    for i in range(0, len(numbers)):
        if numbers[i] in indices:
            indices[numbers[i]].append(i)
        else:
            indices[numbers[i]] = [i]

    while turn < turns:
        last_number: int = numbers[turn - 1]
        next_number: int = 0

        if len(indices[last_number]) > 1:
            next_number: int = indices[last_number][len(indices[last_number]) - 1] - indices[last_number][len(indices[last_number]) - 2]

        numbers.append(next_number)

        if next_number in indices:
            indices[next_number].append(turn)
        else:
            indices[next_number] = [turn]

        turn += 1

    print("Door 15   | {0}th number is {1}".format(turns, numbers[len(numbers) - 1]))

