"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
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


class WeatherStationFacade:
    def __init__(self):
        self.weather_station = WeatherStation()

        self.smartphone = Smarthphone("iPhone", self.weather_station)
        self.another_smartphone = Smarthphone("Pixel", self.weather_station)
        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.another_smartphone)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_smarthphone(self) -> None:
        self.weather_station.remove_observer(self.smartphone)

    def remove_notebook(self) -> None:
        self.weather_station.remove_observer(self.notebook)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({"temperature": 30})
    weather_station.change_state({"temperature": 31})
    weather_station.change_state({"humidity": 90})

    weather_station.remove_smarthphone()
    weather_station.remove_notebook()
    weather_station.reset_state()

    weather_station.change_state({"temperature": 20})
    weather_station.change_state({"temperature": 21})
    weather_station.change_state({"humidity": 75})
