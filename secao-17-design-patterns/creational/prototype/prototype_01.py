"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo

Mutáveis (passados por referência)
    list
    set
    dict
    class (o usuário pode mudar isso)
    ...

Imutáveis (copiados)
    bool
    int
    float
    tuple
    str
    ...
"""

# name01 = "Bruno"
# name02 = name01

# name01 = "João"

# print(name01)
# print(name02)

# list01 = [1, 2, 3]
# list02 = list01

# list01.append(4)

# print(list01)
# print(list02)

from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__} "

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    person01 = Person("Bruno", "Silva")
    person02 = Person("João", "Silva")

    address01 = Address("Rua das Flores", "123")
    address02 = Address("Rua das Oliveiras", "456")

    person01.add_address(address01)
    person02.add_address(address02)

    print(person01)
    print(person02)

    person03 = person02.clone()
    person03.first_name = "Maria"
    print(person03)
