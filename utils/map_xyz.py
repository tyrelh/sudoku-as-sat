from functools import lru_cache

import sys


def map_ijk_to_num(i: int, j: int, k: int, n: int):
    """Maps i, j, k to a number.

    Args:
        i: x index.
        j: y index.
        k: k value of cell.
        n: The n*n board size.

    Returns:
        int: A number mapping.

    """
    return ((n * n) * (i - 1)) + n * (j - 1) + (k - 1) + 1


@lru_cache(maxsize=1)
def _gen_reverse_mapping(n: int):
    map = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                map[map_ijk_to_num(i, j, k, n)] = (i, j, k)
    return map


def map_num_to_ijk(num: int, n: int):
    """Returns a tuple of i, j, k values, given a number

    Args:
        num: The number to convert.
        n: The n*n board size.

    Returns:
        tuple: (i, j, k)
    """
    return _gen_reverse_mapping(n)[num]


if __name__ == '__main__':
    """Tests the functions in the module."""
    n = 9
    vals = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                vals.append(((i, j, k,), map_ijk_to_num(i, j, k, n),))

    for val in vals:
        original_ijk = val[0]
        mapped_value = val[1]
        mapped_ijk = map_num_to_ijk(mapped_value, n)

        if original_ijk != mapped_ijk:
            print("ERRROR", file=sys.stderr)

        print(' {}, {}, {}'.format(str(original_ijk), mapped_value, mapped_ijk))
