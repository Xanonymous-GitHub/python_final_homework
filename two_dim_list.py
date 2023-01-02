from pprint import pp
from secrets import choice
from typing import List, Tuple, Final, Iterable, NoReturn, Sequence, TypeVar

T = TypeVar("T")


# Pick a random value from the given sequence.
def random_choose_from(seq: Sequence[T]) -> T:
    return choice(seq)


# Generate a tuple of random numbers with the given number of rows and columns.
def gen_random_number_tuple(rows: int, cols: int) -> Tuple[int]:
    return tuple(x for x in range(1, rows * cols + 1))


# Generate a 2D list with the given number of rows and columns.
def gen_2d_list(rows: int, cols: int) -> List[List[int]]:
    return [[0] * cols for _ in range(rows)]


# Fill in the blanks to fill the given numbers into the given 2D list.
# We use tuples to represent the coordinates of the 2D list, since lists are mutable.
def fill_into_2d_list(numbers: Iterable[int], two_d: List[List[int]]) -> Tuple[Tuple[int]]:
    if len(two_d) == 0:
        return tuple()

    cols: Final[int] = len(two_d[0])
    if cols == 0:
        return tuple()

    two_d_copy: List[List[int]] = [row[:] for row in two_d]

    for i, number in enumerate(numbers):
        two_d_copy[i // cols][i % cols] = number

    return tuple(tuple(row) for row in two_d_copy)


def start() -> NoReturn:
    expected_range: Final[range] = range(3, 10)

    rows: Final[int] = random_choose_from(expected_range)
    cols: Final[int] = random_choose_from(expected_range)

    numbers: Tuple[int] = gen_random_number_tuple(rows, cols)

    empty_two_d: List[List[int]] = gen_2d_list(rows, cols)
    filled_two_d_tuple: Tuple[Tuple[int]] = fill_into_2d_list(numbers, empty_two_d)

    print(f"rows: {rows}, cols: {cols}")
    pp(filled_two_d_tuple)


if __name__ == '__main__':
    start()
