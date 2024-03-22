import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from components.main_window import MainWindow
from components.display import Display
from components.info import Info
from components.button import ButtonsGrid
from utils.variables import WINDOW_ICON_PATH
from utils.styles import setupTheme

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Adiciona o icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info("")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
