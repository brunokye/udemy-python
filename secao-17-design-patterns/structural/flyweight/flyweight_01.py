"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""

from __future__ import annotations
from typing import List, Dict


class Client:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._address: List = []

        # Extrinsic address data
        self._address_number: str
        self._address_details: str

    def add_address(self, address: Address) -> None:
        self._address.append(address)

    def list_addresses(self) -> None:
        for address in self._address:
            address.show_address(self._address_number, self._address_details)


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            f"{self._street}, {address_number} - "
            f"{address_details}, {self._neighborhood} - {self._zip_code}"
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return "".join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print("Returning an already existing instance.")
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print("Creating a new instance.")

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street="Av Brasil", neighborhood="Centro", zip_code="00000-000"
    )
    a2 = address_factory.get_address(
        street="Av Brasil", neighborhood="Centro", zip_code="00000-000"
    )

    print(f"\n{20 * '-'}\n")

    bruno = Client("Bruno")
    bruno._address_number = "4"
    bruno._address_details = "Casa"
    bruno.add_address(a1)
    bruno.list_addresses()

    joana = Client("Joana")
    joana._address_number = "7"
    joana._address_details = "Ap 32"
    joana.add_address(a1)
    joana.list_addresses()

    print(f"\n{20 * '-'}\n")

    print(a1 == a2)
