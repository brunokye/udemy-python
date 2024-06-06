"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def power(self) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def power(self) -> None:
        self._device.power = not self._device.power

    def volume_up(self) -> None:
        self._device.volume += 10

    def volume_down(self) -> None:
        self._device.volume -= 10


class RemoteControlWithMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0


class IDevice(ABC):
    @property
    @abstractmethod
    def power(self) -> bool:
        pass

    @power.setter
    @abstractmethod
    def power(self, power: bool) -> None:
        pass

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @volume.setter
    @abstractmethod
    def volume(self, volume: int) -> None:
        pass


class Tv(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        status = "ON" if self._power else "OFF"

        print(f"{self._name} is now {status}.")

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            print(f"{self._name} is OFF.")
            return

        if volume > 100 or volume < 0:
            print("Volume cannot be greater than 100 or lower than 0.")
            return

        self._volume = volume
        print(f"Volume is now {self._volume}.")


class Radio(Tv):
    pass


if __name__ == "__main__":
    tv = Tv()
    remote_control = RemoteControl(tv)

    remote_control.volume_up()
    remote_control.power()

    print(f"\n{20 * '-'}\n")

    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_up()

    print(f"\n{20 * '-'}\n")

    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()
    remote_control.volume_down()

    print(f"\n{20 * '-'}\n")

    radio = Radio()
    remote_control = RemoteControlWithMute(radio)

    remote_control.volume_up()
    remote_control.power()
    remote_control.volume_up()
    remote_control.volume_up()
    remote_control.volume_down()
    remote_control.mute()
