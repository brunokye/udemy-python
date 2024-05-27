"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""

from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__} "

    def __repr__(self):
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def add_first_name(self, first_name):
        pass

    @abstractmethod
    def add_last_name(self, last_name):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone_number(self, phone):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_first_name(self, first_name):
        self._result.first_name = first_name
        return self

    def add_last_name(self, last_name):
        self._result.last_name = last_name
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone_number(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name)
        self._builder.add_last_name(last_name)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, first_name, last_name, address):
        # fmt: off
        self._builder\
            .add_first_name(first_name)\
            .add_last_name(last_name)\
            .add_address(address)
        # fmt: on
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user01 = user_director.with_age("João", "Silva", 30)
    user02 = user_director.with_address("Maria", "Silva", "Rua ABC")

    print(user01)
    print(user02)
