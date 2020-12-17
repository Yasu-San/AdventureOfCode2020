import copy


def solve() -> None:
    with open("Input/Door_17.txt", 'r') as infile:
        content: str = infile.read()

    first(content)
    second(content)


def boundary_range(listing: dict, increase: int = 0) -> range:
    maximum: int = 0
    minimum: int = 0

    for key in listing:
        if key > maximum:
            maximum = key
        elif key < minimum:
            minimum = key

    return range(minimum - increase, maximum + 1 + increase)


def test_cube(cubes: dict, x: int, y: int, z: int) -> int:
    active: int = 0

    for cx in range(x - 1, x + 2):
        for cy in range(y - 1, y + 2):
            for cz in range(z - 1, z + 2):
                if (cx != x or cy != y or cz != z) and cx in cubes and cy in cubes[cx] and cz in cubes[cx][cy]:
                    if cubes[cx][cy][cz]:
                        active += 1

    return active


def apply_rules(cubes: dict) -> dict:
    new_cubes: dict = copy.deepcopy(cubes)
    x_range: range = boundary_range(cubes, 1)
    y_range: range = boundary_range(cubes[0], 1)
    z_range: range = boundary_range(cubes[0][0], 1)

    for x in x_range:
        for y in y_range:
            for z in z_range:
                active: int = test_cube(cubes, x, y, z)

                if x in cubes:
                    if y in cubes[x]:
                        if z in cubes[x][y]:
                            if cubes[x][y][z] and (active < 2 or active > 3):
                                new_cubes[x][y][z] = False
                            elif not cubes[x][y][z] and active == 3:
                                new_cubes[x][y][z] = True
                        else:
                            new_cubes[x][y] = new_cubes[x][y] | {z: active == 3}
                    else:
                        if y in new_cubes[x]:
                            new_cubes[x][y] = new_cubes[x][y] | {z: active == 3}
                        else:
                            new_cubes[x] = new_cubes[x] | {y: {z: active == 3}}
                else:
                    if x in new_cubes:
                        if y in new_cubes[x]:
                            new_cubes[x][y] = new_cubes[x][y] | {z: active == 3}
                        else:
                            new_cubes[x] = new_cubes[x] | {y: {z: active == 3}}
                    else:
                        new_cubes = new_cubes | {x: {y: {z: active == 3}}}

    return new_cubes


def count_active_cubes(cubes: dict) -> int:
    counter: int = 0

    for x in cubes:
        for y in cubes[x]:
            for z in cubes[x][y]:
                if cubes[x][y][z]:
                    counter += 1

    return counter


def first(initial: str) -> None:
    cubes: dict = {}
    x: int = 0
    y: int = 0

    for line in initial.splitlines():
        for char in line:
            if char == '.':
                if x in cubes:
                    cubes[x] = cubes[x] | {y: {0: False}}
                else:
                    cubes = cubes | {x: {y: {0: False}}}
            elif char == '#':
                if x in cubes:
                    cubes[x] = cubes[x] | {y: {0: True}}
                else:
                    cubes = cubes | {x: {y: {0: True}}}

            x += 1
        y += 1
        x = 0

    for i in range(6):
        cubes = apply_rules(cubes)

    print("Door 17.1 | Active Cubes: {0}".format(count_active_cubes(cubes)))


def test_cube_4(cubes: dict, x: int, y: int, z: int, w: int) -> int:
    active: int = 0

    for cx in range(x - 1, x + 2):
        for cy in range(y - 1, y + 2):
            for cz in range(z - 1, z + 2):
                for cw in range(w - 1, w + 2):
                    if (cx != x or cy != y or cz != z or cw != w) and cx in cubes and cy in cubes[cx] and cz in cubes[cx][cy] and cw in cubes[cx][cy][cz]:
                        if cubes[cx][cy][cz][cw]:
                            active += 1

    return active


def apply_rules_4(cubes: dict) -> dict:
    new_cubes: dict = copy.deepcopy(cubes)
    x_range: range = boundary_range(cubes, 1)
    y_range: range = boundary_range(cubes[0], 1)
    z_range: range = boundary_range(cubes[0][0], 1)
    w_range: range = boundary_range(cubes[0][0][0], 1)

    for x in x_range:
        for y in y_range:
            for z in z_range:
                for w in w_range:
                    active: int = test_cube_4(cubes, x, y, z, w)

                    if x in cubes:
                        if y in cubes[x]:
                            if z in cubes[x][y]:
                                if w in cubes[x][y][z]:
                                    if cubes[x][y][z][w] and (active < 2 or active > 3):
                                        new_cubes[x][y][z][w] = False
                                    elif not cubes[x][y][z][w] and active == 3:
                                        new_cubes[x][y][z][w] = True
                                else:
                                    new_cubes[x][y][z] = new_cubes[x][y][z] | {w: active == 3}
                            else:
                                if z in new_cubes[x][y]:
                                    new_cubes[x][y][z] = new_cubes[x][y][z] | {w: active == 3}
                                else:
                                    new_cubes[x][y] = new_cubes[x][y] | {z: {w: active == 3}}
                        else:
                            if y in new_cubes[x]:
                                if z in new_cubes[x][y]:
                                    new_cubes[x][y][z] = new_cubes[x][y][z] | {w: active == 3}
                                else:
                                    new_cubes[x][y] = new_cubes[x][y] | {z: {w: active == 3}}
                            else:
                                new_cubes[x] = new_cubes[x] | {y: {z: {w: active == 3}}}
                    else:
                        if x in new_cubes:
                            if y in new_cubes[x]:
                                if z in new_cubes[x][y]:
                                    new_cubes[x][y][z] = new_cubes[x][y][z] | {w: active == 3}
                                else:
                                    new_cubes[x][y] = new_cubes[x][y] | {z: {w: active == 3}}
                            else:
                                new_cubes[x] = new_cubes[x] | {y: {z: {w: active == 3}}}
                        else:
                            new_cubes = new_cubes | {x: {y: {z: {w: active == 3}}}}

    return new_cubes


def count_active_cubes_4(cubes: dict) -> int:
    counter: int = 0

    for x in cubes:
        for y in cubes[x]:
            for z in cubes[x][y]:
                for w in cubes[x][y][z]:
                    if cubes[x][y][z][w]:
                        counter += 1

    return counter


def second(initial: str) -> None:
    cubes: dict = {}
    x: int = 0
    y: int = 0

    for line in initial.splitlines():
        for char in line:
            if char == '.':
                if x in cubes:
                    cubes[x] = cubes[x] | {y: {0: {0: False}}}
                else:
                    cubes = cubes | {x: {y: {0: {0: False}}}}
            elif char == '#':
                if x in cubes:
                    cubes[x] = cubes[x] | {y: {0: {0: True}}}
                else:
                    cubes = cubes | {x: {y: {0: {0: True}}}}

            x += 1
        y += 1
        x = 0

    for i in range(6):
        cubes = apply_rules_4(cubes)

    print("Door 17.2 | Active Cubes: {0}".format(count_active_cubes_4(cubes)))
