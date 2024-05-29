"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    """Receive"""

    def __init__(self, name: str, room: str) -> None:
        self.name = name
        self.room = room
        self.color = "white"

    def on(self):
        print(f"Light {self.name} in {self.room} is now ON.")

    def off(self):
        print(f"Light {self.name} in {self.room} is now OFF.")

    def change_color(self, color: str):
        self.color = color
        print(f"Light {self.name} in {self.room} is now {color}.")


class ICommand(ABC):
    """Command Interface"""

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    """Concrete Command"""

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class ChangeLightColor(ICommand):
    """Concrete Command"""

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """Invoker"""

    def __init__(self) -> None:
        self._commands: Dict[str, ICommand] = {}
        self._history: List[Tuple[str, str]] = []

    def add_command(self, slot: str, command: ICommand) -> None:
        self._commands[slot] = command

    def execute_command(self, slot: str) -> None:
        if slot in self._commands:
            self._commands[slot].execute()
            self._history.append((slot, "execute"))

    def undo_command(self, slot: str) -> None:
        if slot in self._commands:
            self._commands[slot].undo()
            self._history.append((slot, "undo"))

    def history(self) -> None:
        if not self._history:
            print("Nothing to undo.")
            return None

        command, action = self._history.pop()

        if action == "execute":
            self._commands[command].undo()
        else:
            self._commands[command].execute()


if __name__ == "__main__":
    bedroom_light = Light("Bedroom", "Living Room")
    bathroom_light = Light("Bathroom", "Bathroom")

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)

    bedroom_light_color = ChangeLightColor(bedroom_light, "red")
    bathroom_light_color = ChangeLightColor(bathroom_light, "blue")

    remote = RemoteController()
    remote.add_command("bedroom_light_on", bedroom_light_on)
    remote.add_command("bathroom_light_on", bathroom_light_on)

    remote.add_command("bedroom_light_color", bedroom_light_color)
    remote.add_command("bathroom_light_color", bathroom_light_color)

    print("Turn on the lights:")
    remote.execute_command("bedroom_light_on")
    remote.undo_command("bedroom_light_on")
    remote.execute_command("bathroom_light_on")
    remote.undo_command("bathroom_light_on")

    print(f"\n{20 * '-'}\n")

    print("Change Color:")
    remote.execute_command("bedroom_light_color")
    remote.undo_command("bedroom_light_color")
    remote.execute_command("bathroom_light_color")
    remote.undo_command("bathroom_light_color")

    print(f"\n{20 * '-'}\n")

    remote.history()
    remote.history()
    remote.history()
    remote.history()
    remote.history()
    remote.history()
    remote.history()
    remote.history()
    remote.history()
