from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> None:
        ...

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.detalhes(f"DEPÓSITO DE {valor}")

    def detalhes(self, msg: str = "") -> None:
        print(f"O seu saldo é: {self.saldo:.2f} ({msg})")

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f"({self.agencia!r}, {self.conta!r}, {self.saldo!r})"
        return f"{class_name}{atributos}"


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> None:
        saque = self.saldo - valor

        if saque >= 0:
            self.saldo -= valor
            self.detalhes(f"SAQUE DE {valor}")
            return

        print("Não foi possível sacar o valor desejado.")
        self.detalhes(f"SAQUE NEGADO {valor}")


class ContaCorrente(Conta):
    # fmt: off
    def __init__(
        self, agencia: int,
        conta: int,
        saldo: float = 0,
        limite: float = 0
    ) -> None:
        # fmt: on
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> None:
        saque = self.saldo - valor
        limite_maximo = -self.limite

        if saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"SAQUE DE {valor}")
            return

        print("Não foi possível sacar o valor desejado.")
        print(f"Seu limite é: {-self.limite:.2f}")
        self.detalhes(f"SAQUE NEGADO {valor}")

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = (
            f"({self.agencia!r}, {self.conta!r}, "
            f"{self.saldo!r}, {self.limite!r})"
        )

        return f"{class_name}{atributos}"


if __name__ == "__main__":
    # cp1 = ContaPoupanca(111, 222)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # cp1.sacar(1)
    # cp1.sacar(1)

    # print(f"\n{20 * '-'}\n")

    # cc1 = ContaCorrente(111, 222, 0, 1)
    # cc1.sacar(1)
    # cc1.sacar(1)
    # cc1.depositar(1)
    # cc1.sacar(1)
    ...
