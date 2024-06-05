"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""

from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def up(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass


class Control(IControl):
    def up(self) -> None:
        print("Control: Moving up.")

    def down(self) -> None:
        print("Control: Moving down.")

    def left(self) -> None:
        print("Control: Moving left.")

    def right(self) -> None:
        print("Control: Moving right.")


class NewControl:
    def move_up(self) -> None:
        print("NewControl: Moving top.")

    def move_down(self) -> None:
        print("NewControl: Moving down.")

    def move_left(self) -> None:
        print("NewControl: Moving left.")

    def move_right(self) -> None:
        print("NewControl: Moving right.")


class ControlAdapter:
    """Adapter Object"""

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def up(self) -> None:
        self.new_control.move_up()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()

    def right(self) -> None:
        self.new_control.move_right()


class ControlAdapter2(Control, NewControl):
    """Adapter Class"""

    def up(self) -> None:
        self.move_up()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == "__main__":
    c0 = Control()
    c0.up()
    c0.down()
    c0.left()
    c0.right()

    print(f"\n{20 * '-'}\n")

    """Adapter Object"""
    new_control = NewControl()
    c1 = ControlAdapter(new_control)

    c1.up()
    c1.down()
    c1.left()
    c1.right()

    print(f"\n{20 * '-'}\n")

    """Adapter Class"""
    c2 = ControlAdapter2()
    c2.up()
    c2.down()
    c2.left()
    c2.right()
