import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao1 = QPushButton("Texto do botão")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("O meu slot foi executado")

    return inner


@Slot()
def outro_slot(checked):
    print(f"Está marcado: {checked}")


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())

    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra inferior")

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Qualquer Coisa")
primeira_acao = primeiro_menu.addAction("Primeira Ação")
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_acao = primeiro_menu.addAction("Segunda Ação")
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao1.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()
