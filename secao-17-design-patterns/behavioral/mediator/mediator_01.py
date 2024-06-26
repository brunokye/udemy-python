"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f"{colleague.name} said: {msg}")

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_colleague: List[Colleague] = [
            c for c in self.colleagues if c.name == receiver
        ]

        if not receiver_colleague:
            return

        receiver_colleague[0].direct(
            f"{sender.name} to {receiver_colleague[0].name}: {msg}"
        )


if __name__ == "__main__":
    chat = Chatroom()

    joao = Person("Joao", chat)
    maria = Person("Maria", chat)
    elise = Person("Elise", chat)
    jose = Person("Jose", chat)

    chat.add(joao)
    chat.add(maria)
    chat.add(elise)

    joao.broadcast("Hello!")
    maria.broadcast("Hi!")
    elise.broadcast("Hey!")
    jose.broadcast("How are you?")

    print(f"\n{20 * '-'}\n")

    joao.send_direct("Maria", "Hey!")
    maria.send_direct("Joao", "Hi!")
