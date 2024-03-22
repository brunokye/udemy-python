import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta: contas.Conta) -> bool:
        if conta in self.contas:
            return True
        return False

    def _checa_conta(self, conta: contas.Conta) -> bool:
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente: pessoas.Pessoa) -> bool:
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta_cliente(
        self,
        conta: contas.Conta,
        cliente: pessoas.Cliente,
    ) -> bool:
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta) -> bool:
        return (
            self._checa_agencia(conta)
            and self._checa_conta(conta)
            and self._checa_cliente(cliente)
        )

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atributos = f"({self.agencias!r}, {self.contas!r}, {self.clientes!r})"
        return f"{class_name}{atributos}"


if __name__ == "__main__":
    c1 = pessoas.Cliente("Bruno", 20)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1

    c2 = pessoas.Cliente("Maria", 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1

    banco = Banco()

    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)
