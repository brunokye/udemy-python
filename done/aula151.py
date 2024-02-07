def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    return f"{class_name}: {class_dict}"


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         return f"{class_name}: {class_dict}"


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time("Brasil")
portugal = Time("Portugal")

terra = Planeta("Terra")
marte = Planeta("Marte")

print(brasil)
print(portugal)

print(f"\n{20 * '-'}\n")

print(terra)
print(marte)
