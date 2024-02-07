"""
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas
as referências dos objetos filhos também são
apagadas.
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("APAGANDO", self.rua, self.numero)


cliente = Cliente("Maria")

cliente.inserir_endereco("Av Brasil", 54)
cliente.inserir_endereco("Rua B", 123)

endereco_externo = Endereco("Av Teste", 323)
cliente.inserir_endereco_externo(endereco_externo)

cliente.listar_enderecos()

print(f"\n{20 * '-'}\n")
del cliente
print(f"\n{20 * '-'}\n")
