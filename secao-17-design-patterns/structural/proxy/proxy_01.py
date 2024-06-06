"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    first_name: str
    last_name: str

    @abstractmethod
    def get_address(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class RealUser(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2)  # Simulating request
        self.first_name = first_name
        self.last_name = last_name

    def get_address(self) -> List[Dict]:
        sleep(2)  # Simulating request
        return [{"street": "Av. Paulista", "number": "100"}]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulating request
        return {
            "cpf": "111.111.111-11",
            "rg": "11.111.111-1",
        }


class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        # Those objects doesn't exist yet
        self._real_user: RealUser
        self._cached_address: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> RealUser:
        if not hasattr(self, "_real_user"):
            self._real_user = RealUser(self.first_name, self.last_name)

        return self._real_user

    def get_address(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, "_cached_address"):
            self._cached_address = self._real_user.get_address()

        return self._cached_address

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, "_all_user_data"):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    user01 = UserProxy("John", "Doe")

    print(user01.first_name)
    print(user01.last_name)

    print(f"\n{20 * '-'}\n")

    # 6 seconds
    print(user01.get_all_user_data())
    print(user01.get_address())

    print(f"\n{20 * '-'}\n")

    # Cached answer
    for i in range(5):
        print(user01.get_all_user_data())
        print(user01.get_address())
