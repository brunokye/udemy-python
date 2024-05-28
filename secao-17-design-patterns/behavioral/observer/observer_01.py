"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """Observable"""

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    def remove_observer(self, observer: IObserver) -> None:
        pass

    def notify_observer(self) -> None:
        pass


class WeatherStation(IObservable):
    """Observable"""

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict):
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observer()

    def reset_state(self):
        self._state = {}
        self.notify_observer()

    def update(self, message: str) -> None:
        pass

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            return self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):
    """Observer"""

    @abstractmethod
    def update(self) -> None:
        pass


class Smarthphone(IObserver):
    """Observer"""

    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f"{self.name} o objeto {observable_name} acabou de ser atualizado "
            f"-> {self.observable.state}"  # type: ignore
        )


class Notebook(IObserver):
    """Observer"""

    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self):
        state = self.observable.state  # type: ignore
        print(
            "Sou o Notebook e vou fazer outra "
            f"coisa com esses dados -> {state}"
        )

    def update(self) -> None:
        self.show()


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smarthphone("iPhone", weather_station)
    another_smartphone = Smarthphone("Pixel", weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(another_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {"temperature": 30}
    weather_station.state = {"temperature": 31}
    weather_station.state = {"humidity": 90}

    weather_station.remove_observer(another_smartphone)
    weather_station.reset_state()
