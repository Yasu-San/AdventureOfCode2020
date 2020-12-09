from typing import List


def solve() -> None:
    preamble_length: int = 25
    stream: List[int] = []

    with open("Input/Door_09.txt", 'r') as infile:
        for line in infile:
            stream.append(int(line))

    weakness: int = first(stream, preamble_length)
    second(stream, weakness)


def test_nums(preamble: List[int], should_equal: int) -> bool:
    for num1 in preamble:
        for num2 in preamble:
            if num1 != num2 and num1 + num2 == should_equal:
                return True

    return False


def first(stream: List[int], preamble_length: int) -> int:
    next_num: int = preamble_length

    while test_nums(stream[next_num - preamble_length:next_num], stream[next_num]):
        next_num += 1

    print("Door  9.1 | Broken at pos {0} with value {1}".format(next_num, stream[next_num]))
    return stream[next_num]


def second(stream: List[int], should_equal: int) -> None:
    start_index: int = 0
    end_index: int = 1
    list_sum: int = sum(stream[start_index:end_index])

    while list_sum != should_equal:
        if list_sum < should_equal:
            end_index += 1
        else:
            start_index += 1

        list_sum = sum(stream[start_index:end_index])

    print("Door  9.2 | Weakness is {0}".format(min(stream[start_index:end_index]) + max(stream[start_index:end_index])))
