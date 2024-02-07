"""
Teoria: python Special Methods, Magic Methods ou Dunder Methods
Dunder = Double Underscore = __dunder__

Antigo e útil: https://rszalski.github.io/magicmethods/
docs: https://docs.python.org/3/reference/datamodel.html#specialnames

__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
"""


# class Ponto:
#     def __init__(self, x, y, z="str"):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __str__(self) -> str:
#         return f"({self.x}, {self.y})"

#     def __repr__(self):
#         # class_name = self.__class__.__name__
#         class_name = type(self).__name__
#         return (
#           f"{class_name} (x = {self.x!r}, y = {self.y!r}, z = {self.z!r})"
#         )


# p1 = Ponto(1, 2)
# p2 = Ponto(323, 653)

# print(p1)
# print(repr(p2))
# print(f"{p2!r}")


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name} (x = {self.x!r}, y = {self.y!r})"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.x
        resultado_other = other.y + other.y

        return resultado_self > resultado_other


if __name__ == "__main__":
    p1 = Ponto(1, 2)
    p2 = Ponto(5, 6)
    p3 = p1 + p2

    print(p3)
    print(f"P1 é maior do que P2? {p1 > p2}")
    print(f"P2 é maior do que P1? {p2 > p1}")
