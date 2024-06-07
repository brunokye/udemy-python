"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, child: BoxStructure) -> None:
        pass

    def remove(self, child: BoxStructure) -> None:
        pass


class Box(BoxStructure):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(f"{self.name} - {self.price}")

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    # Leaf
    shirt01 = Product("Shirt", 25.90)
    shirt02 = Product("Shirt", 20.90)
    shirt03 = Product("Shirt", 15.90)

    # Composite
    shirt_box = Box("Shirts")
    shirt_box.add(shirt01)
    shirt_box.add(shirt02)
    shirt_box.add(shirt03)
    shirt_box.print_content()

    print(f"\n{20 * '-'}\n")

    # Leaf
    smartphone01 = Product("Smartphone", 1000.00)
    smartphone02 = Product("Smartphone", 2000.00)

    # Composite
    smartphone_box = Box("Smartphones")
    smartphone_box.add(smartphone01)
    smartphone_box.add(smartphone02)
    smartphone_box.print_content()

    print(f"\n{20 * '-'}\n")

    # Composite
    big_box = Box("Big Box")
    big_box.add(shirt_box)
    big_box.add(smartphone_box)
    big_box.print_content()

    print(f"\n{20 * '-'}\n")

    print(f"Total: {big_box.get_price()}")
