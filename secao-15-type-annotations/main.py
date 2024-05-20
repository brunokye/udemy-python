from collections.abc import Callable
from typing import TypeVar

# types
test_string: str = "test"
test_int: int = 1
test_float: float = 1.0
test_bool: bool = True
test_list: list = [1, 2, 3]
test_dict: dict = {"a": 1, "b": 2, "c": 3}
test_tuple: tuple = (1, 2, 3)
test_set: set = {1, 2, 3}


def new_sum(x: int, y: int, z: int) -> int:
    return x + y + z


# list
list_int: list[int] = [1, 2, 3]
list_strings: list[str] = ["a", "b", "c"]
list_float: list[float] = [1.0, 2.0, 3.0]
list_list_int: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# dict
dict_int: dict[str, int] = {"a": 1, "b": 2, "c": 3}
dict_list: dict[str, list[int]] = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9],
}


# type alias
ListInt = list[int]
DictListInt = dict[str, ListInt]
dict_list_int: DictListInt = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9],
}

# Optional
string_and_int: str | int = 1
string_and_int = "A"
list_string_or_int: list[str | int] = [1, "A"]


# isinstance
def sum_new(x: int, y: float | None = None) -> float:
    if isinstance(y, float | int):
        return x + y

    return x


# Callable
SumInt = Callable[[int, int], int]


def execute(func: SumInt, x: int, y: int) -> int:
    return func(x, y)


def sum01(x: int, y: int) -> int:
    return x + y


# TypeVar
T = TypeVar("T")


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int_type = get_item([1, 2, 3], 1)
list_str_type = get_item(["a", "b", "c"], 1)


# Class
class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def say_my_name(person: Person) -> None:
    print(person.full_name)
