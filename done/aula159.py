"""
O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.
Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: https://docs.python.org/3/library/dataclasses.html
"""

from dataclasses import dataclass, asdict, astuple, field

# @dataclass
# class Pessoa(init=False, repr=True, order=True):


@dataclass
class Pessoa:
    nome: str
    sobrenome: str = field(default="Sem Sobrenome")
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    # @property
    # def nome_completo(self):
    #     return f"{self.nome} {self.sobrenome}"

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = " ".join(sobrenome)


if __name__ == "__main__":
    p1 = Pessoa("Bruno", "Ferreira", 20)
    p2 = Pessoa("Bruno", "Ferreira", 20)

    print(p1)
    print(asdict(p1).keys())
    print(astuple(p1)[0])
    print(p1.nome_completo)
    print(p1 == p2)

    print(f"\n{20 * '-'}\n")

    lista = [Pessoa("A", "Z"), Pessoa("B", "Y"), Pessoa("C", "X")]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)

    print(ordenadas)
