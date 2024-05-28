"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__} | {self.__dict__} | {params}"

    def __repr__(self):
        return self.__str__()


# class A(StringReprMixin):
#     def __init__(self, name):
#         self.x = 20
#         self.y = 10
#         self.name = name


# a = A("Bruno")
# print(a)


class MonoStateSimple(StringReprMixin):
    _state = {"x": 10, "y": 20}

    def __init__(self, first_name=None, last_name=None):
        # self.x = 0
        # self.y = 0
        self.__dict__ = self._state

        if first_name is not None:
            self.first_name = first_name

        if last_name is not None:
            self.last_name = last_name


if __name__ == "__main__":
    m1 = MonoStateSimple("Bruno")
    # print(m1)

    m2 = MonoStateSimple(last_name="Ferreira")

    m1.x = "Test"  # type: ignore
    m2.y = "?"  # type: ignore

    print(m1)
    print(m2)
