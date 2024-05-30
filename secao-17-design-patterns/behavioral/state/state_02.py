from __future__ import annotations
from abc import ABC, abstractmethod


class Sound:
    def __init__(self):
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        self.playing = 0
        self.mode = mode
        print(f"Mode changed: {mode.__class__.__name__}")

    def press_next(self) -> None:
        self.mode.press_next()

    def press_prev(self) -> None:
        self.mode.press_prev()

    def __str__(self) -> str:
        return f"Sound: {str(self.playing)}"


class PlayMode(ABC):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        pass

    def press_prev(self) -> None:
        pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000
        print(f"Radio mode: {self.sound.playing}")

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing >= 1000 else 0
        print(f"Radio mode: {self.sound.playing}")


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1
        print(f"Music mode: {self.sound.playing}")

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing >= 1 else 0
        print(f"Music mode: {self.sound.playing}")


if __name__ == "__main__":
    sound = Sound()

    sound.press_next()
    sound.press_prev()
    sound.press_prev()

    sound.change_mode(MusicMode(sound))

    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
