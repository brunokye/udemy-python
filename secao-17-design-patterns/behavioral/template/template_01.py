"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation01()
        self.base_class_method()
        self.operation02()

    def hook(self):
        pass

    def base_class_method(self):
        print("Abstract: base_class_method")

    @abstractmethod
    def operation01(self):
        pass

    @abstractmethod
    def operation02(self):
        pass


class Concrete01(Abstract):
    def operation01(self):
        print("Concrete01: operation01")

    def operation02(self):
        print("Concrete01: operation02")


class Concrete02(Abstract):
    def hook(self):
        print("Concrete02: hook")

    def operation01(self):
        print("Concrete02: operation01")

    def operation02(self):
        print("Concrete02: operation02")


if __name__ == "__main__":
    c1 = Concrete01()
    c1.template_method()

    print(f"\n{20 * '-'}\n")

    c2 = Concrete02()
    c2.template_method()
