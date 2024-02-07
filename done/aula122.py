"""
Classe - Molde (geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instância.
"""


class Carro:
    def __init__(self, nome="padrão"):
        self.nome = nome

    def acelerar(self):
        print(f"{self.nome} está acelerando.")


fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)
