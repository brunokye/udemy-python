class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


motor = Motor("1.0")
fabricante = Fabricante("Toyota")

celta = Carro("Celta")
celta.motor = motor
celta.fabricante = fabricante

print(celta.nome, celta.fabricante.nome, celta.motor.nome)
