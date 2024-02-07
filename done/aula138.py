"""
Herança simples - Relações entre classes

Associação - usa
Agregação - tem
Composição - É dono de
Herança - É um

Herança vs Composição

Classe principal (Pessoa)
  -> super class, base class, parent class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""


class Pessoa:
    cpf = "CPF da Pessoa"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print("Classe Pessoa")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome(self):
        print("Classe Cliente")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = "CPF do Aluno"


c1 = Cliente("Bruno", "Ferreira")
c1.falar_nome()
print(c1.cpf)

print(f"\n{20 * '-'}\n")

a1 = Aluno("Gabriel", "Silva")
a1.falar_nome()
print(a1.cpf)
