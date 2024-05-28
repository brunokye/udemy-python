# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print("0º - call da Meta")
#         return super().__call__(*args, **kwargs)


# class Person(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print("1º - new")
#         return super().__new__(cls)

#     def __init__(self, name):
#         print("2º - init")
#         self.name = name

#     def __call__(self, x, y):
#         print("3º - call da Person")
#         print(f"call foi chamado - {self.name} {x} {y}")


# p1 = Person("Bruno")
# p1(2, 4)
# print(p1.name)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.theme = "O tema claro"
        self.font = "18px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = "O tema escuro"
    as1.font = "16px"

    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.theme)
    print(as3.font)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
