from typing import (
    List,
    Union,
    Tuple,
    Dict,
    Set,
    NewType,
    Callable,
    Sequence,
    Iterable,
)

# Primitives
number: int = 10
float: float = 10.5
boolean: bool = True
string: str = "Hello"

# Sequencial
list: List[int] = [1, 2, 3]
list_str_int: List[Union[int, str]] = ["1", 2, 3]
tuple: Tuple[int, int, int] = (1, 2, 3)

# Dictionaries and Sets
dict: Dict[str, Union[str, int]] = {"key": "value", "key2": 2}
set: Set[int] = {1, 2, 3}

# Alias
MyDict: Dict[str, Union[str, int, List[int]]]
new_dict = MyDict = {"key": "value", "key2": 2, "key3": [1, 2, 3]}

# New Type
UserId = NewType("UserId", int)
user_id = UserId(1)


# Callable
def return_function(function: Callable[[int, int], int]) -> Callable:
    return function


def say_hi():
    print("Hi!")


def new_sum(x: int, y: int) -> int:
    return x + y


# print(return_function(new_sum)(10, 20))


# Class
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self) -> None:
        print(f"{self.first_name} {self.last_name} is talking...")


# Sequence and Iterable
def iterate(sequence: Sequence[int]):
    return [x for x in sequence]


def iterate_iterable(sequence: Iterable[int]):
    return [x for x in sequence]


# print(iterate([1, 2, 3]))
# print(iterate_iterable([1, 2, 3]))
