import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from utils.variables import MEDIUM_FONT_SIZE
from utils.expressions import isNumOrDot, isValidNumber, converToNumber
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .display import Display
    from .info import Info
    from .main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px;")

        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)

        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self,
        display: "Display",
        info: "Info",
        window: "MainWindow",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]

        self.display = display
        self.info = info
        self.window = window

        self._equation = ""
        self._equationInitialValue = ""

        self._left = None
        self._right = None
        self._op = None
        self._result = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.clearPressed.connect(self._clear)
        self.display.delPressed.connect(self._backspace)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        self.display.negativePressed.connect(self._invertNumber)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        buttonText = button.text()

        if buttonText == "C":
            # button.clicked.connect(self.display.clear)

            # slot = self._makeSlot(self.display.clear)
            # self._connectButtonClicked(button, slot)

            self._connectButtonClicked(button, self._clear)

        if buttonText == "◀":
            self._connectButtonClicked(button, self.display.backspace)

        if buttonText == "N":
            self._connectButtonClicked(button, self._invertNumber)

        if buttonText in "+-/*^":
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, buttonText)
            )

        if buttonText == "=":
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = converToNumber(displayText) * -1
        self.display.setText(str(number))
        self.display.setFocus()

    @Slot()
    def _insertToDisplay(self, buttonText):
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, buttonText):
        displayText = self.display.text()

        self.display.clear()

        # Se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError("Digite algum número.")
            return

        # Se houver algo no número da esquerda, não fazemos nada.
        # Aguardaremos o número da direita.
        if self._left is None:
            self._left = converToNumber(displayText)

        self._op = buttonText
        self.equation = f"{self._left} {self._op} ?"
        self.display.setFocus()

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError("Digite algum número.")
            return

        self._right = converToNumber(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"
        self._result = "error"

        try:
            if "^" in self.equation and isinstance(self._left, int | float):
                # result = eval(self.equation.replace("^", "**"))
                self._result = math.pow(self._left, self._right)
                self._result = converToNumber(str(self._result))
            else:
                self._result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Divisão por zero.")
        except OverflowError:
            self._showError(
                "Resultado muito grande, essa conta não pode ser realizada."
            )

        self.display.clear()
        self.info.setText(f"{self.equation} = {self._result}")

        self._left = self._result
        self._right = None

        if self._result == "error":
            self._left = None

        self.display.setFocus()

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        messageBox = self.window.makeMessageBox()
        messageBox.setText(text)
        return messageBox

    def _showError(self, text):
        messageBox = self._makeDialog(text)
        messageBox.setIcon(messageBox.Icon.Critical)
        messageBox.exec()
        self.display.setFocus()

        # messageBox.setInformativeText(
        #     "Aqui é possível adicionar uma descrição"
        # )

        # messageBox.setStandardButtons(
        #     messageBox.StandardButton.Cancel | messageBox.StandardButton.Ok
        # )

        # test = messageBox.setStandardButtons(messageBox.StandardButton.No)
        # messageBox.button(test).setText("Não")

        # result = messageBox.exec()

        # if result == messageBox.StandardButton.Cancel:
        #     print("Usuário clicou em CANCEL.")
        # if result == messageBox.StandardButton.Ok:
        #     print("Usuário clicou em OK.")

    def _showInfo(self, text):
        messageBox = self._makeDialog(text)
        messageBox.setIcon(messageBox.Icon.Information)
        messageBox.exec()
        self.display.setFocus()
