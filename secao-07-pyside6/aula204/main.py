import sys
import time

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget
from worker import Ui_myWidget


class Worker01(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = "0"
        self.started.emit(value)

        for i in range(1, 6):
            value = str(i)
            self.progressed.emit(str(value))
            time.sleep(1)

        self.finished.emit(value)


class Worker02(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = "0"
        self.started.emit(value)

        for i in range(50, 105, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.3)

        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button01.clicked.connect(self.hardWork01)
        self.button02.clicked.connect(self.hardWork02)

    def hardWork01(self):
        self._worker01 = Worker01()
        self._thread01 = QThread()

        worker = self._worker01
        thread = self._thread01

        worker.moveToThread(thread)

        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker01Started)
        worker.progressed.connect(self.worker01Progressed)
        worker.finished.connect(self.worker01Finished)

        thread.start()

    def worker01Started(self, value):
        self.button01.setDisabled(True)
        self.label01.setText(value)
        print(f"Worker 1 iniciado - {value}")

    def worker01Progressed(self, value):
        self.label01.setText(value)
        print(f"1 em progresso - {value}")

    def worker01Finished(self, value):
        self.label01.setText(value)
        self.button01.setDisabled(False)
        print(f"Worker 1 finalizado - {value}")

    def hardWork02(self):
        self._worker02 = Worker02()
        self._thread02 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker02
        thread = self._thread02

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        thread.started.connect(worker.executeMe)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker02Started)
        worker.progressed.connect(self.worker02Progressed)
        worker.finished.connect(self.worker02Finished)

        thread.start()

    def worker02Started(self, value):
        self.button02.setDisabled(True)
        self.label02.setText(value)
        print(f"Worker 2 iniciado - {value}")

    def worker02Progressed(self, value):
        self.label02.setText(value)
        print(f"2 em progresso - {value}")

    def worker02Finished(self, value):
        self.label02.setText(value)
        self.button02.setDisabled(False)
        print(f"Worker 2 finalizado - {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
