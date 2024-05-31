from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandleABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ["a", "b", "c"]
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter.lower() in self.letters:
            return f"HandleABC: Letter {letter} was found!"

        return self.sucessor.handle(letter)


class HandleDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ["d", "e", "f"]
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter.lower() in self.letters:
            return f"HandleDEF: Letter {letter} was found!"

        return self.sucessor.handle(letter)


class HandleUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f"HandleUnsolved: Letter {letter} was not found!"


if __name__ == "__main__":
    handle_unsolved = HandleUnsolved()
    handle_def = HandleDEF(handle_unsolved)
    handle_abc = HandleABC(handle_def)

    print(handle_abc.handle("B"))
    print(handle_abc.handle("d"))
    print(handle_abc.handle("Y"))

    print(f"\n{20 * '-'}\n")

    print(handle_def.handle("B"))
    print(handle_def.handle("d"))
    print(handle_def.handle("Y"))

    print(f"\n{20 * '-'}\n")

    print(handle_unsolved.handle("B"))
    print(handle_unsolved.handle("d"))
    print(handle_unsolved.handle("Y"))
