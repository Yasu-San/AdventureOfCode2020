from typing import List


def solve() -> None:
    tree_map: List[List[bool]] = []

    with open("Input/Door_03.txt", 'r') as content:
        for line in content:
            row: List[bool] = []
            for char in line:
                row.append(char == "#")
            tree_map.append(row)

    first(tree_map)
    second(tree_map)


def count_trees(tree_map: List[List[bool]], row_add: int, col_add: int) -> int:
    row: int = 0
    col: int = 0
    trees: int = 0

    while row < len(tree_map):
        col = col % (len(tree_map[row]) - 1)

        if tree_map[row][col]:
            trees += 1

        row += row_add
        col += col_add

    return trees


def first(tree_map: List[List[bool]]) -> None:
    print("Door  3.1 | {0} trees passed".format(count_trees(tree_map, 1, 3)))


def second(tree_map: List[List[bool]]) -> None:
    tree_mul: int = count_trees(tree_map, 1, 1)
    tree_mul *= count_trees(tree_map, 1, 3)
    tree_mul *= count_trees(tree_map, 1, 5)
    tree_mul *= count_trees(tree_map, 1, 7)
    tree_mul *= count_trees(tree_map, 2, 1)

    print("Door  3.2 | Solution is {0}".format(tree_mul))
