"""
abstractmethod para qualquer método já decorado (@property e setter)
É possível criar @property @property.setter @classmethod
@staticmethod e métodos normais como abstratos, para isso
use @abstractmethod como decorator mais interno.

Foo e Bar são palavras usadas como placeholder
para palavras que podem mudar na programação.
"""

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None

    @property
    @abstractmethod
    def name(self):
        ...

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # @abstractmethod
    # def name(self, name):
    #     ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print("Sou inútil")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # @AbstractFoo.name.setter
    # def name(self, name):
    #     self._name = name


foo = Foo("Bar")
print(foo.name)
