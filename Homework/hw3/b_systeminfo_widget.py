from a_threads import SystemInfo
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self):
        self.setGeometry(800, 300, 400, 300)

        # Макет ввода задержки
        self.label_Delay = QtWidgets.QLabel('Задержка:')

        self.lineEdit_Delay = QtWidgets.QLineEdit()
        self.lineEdit_Delay.setPlaceholderText('Введите время задержки')

        self.pushButton_Delay = QtWidgets.QPushButton('Применить задержку')

        layout_Delay = QtWidgets.QVBoxLayout()
        layout_Delay.addWidget(self.label_Delay)
        layout_Delay.addWidget(self.lineEdit_Delay)
        layout_Delay.addWidget(self.pushButton_Delay)
        # ===============================================================

        # Макет вывода загрузки CPU и RAM
        # CPU
        self.label_CPU = QtWidgets.QLabel('Загрузка CPU:')
        self.plainTextEdit_CPU = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_CPU.setReadOnly(True)

        layout_CPU = QtWidgets.QVBoxLayout()
        layout_CPU.addWidget(self.label_CPU)
        layout_CPU.addWidget(self.plainTextEdit_CPU)

        # RAM
        self.label_RAM = QtWidgets.QLabel('Загрузка RAM:')
        self.plainTextEdit_RAM = QtWidgets.QPlainTextEdit()
        self.plainTextEdit_RAM.setReadOnly(True)

        layout_RAM = QtWidgets.QVBoxLayout()
        layout_RAM.addWidget(self.label_RAM)
        layout_RAM.addWidget(self.plainTextEdit_RAM)

        # CPU + RAM layout
        layout_CPU_RAM = QtWidgets.QHBoxLayout()
        layout_CPU_RAM.addLayout(layout_CPU)
        layout_CPU_RAM.addLayout(layout_RAM)
        # ===============================================================

        # Основной макет
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_Delay)
        layout_main.addLayout(layout_CPU_RAM)

        self.setLayout(layout_main)

    def initThreads(self):
        self.thread = SystemInfo()
        self.thread.start()

    def initSignals(self):
        self.thread.started.connect(self.threadStarted)
        self.thread.systemInfoReceived.connect(self.getInfo)
        self.pushButton_Delay.clicked.connect(self.changeDelay)

    def threadStarted(self):
        self.plainTextEdit_CPU.appendPlainText('Начинаю анализ...')
        self.plainTextEdit_RAM.appendPlainText('Начинаю анализ...')

    def getInfo(self, systemInfoReceived):
        self.plainTextEdit_CPU.appendPlainText(f'Загрузка CPU: {systemInfoReceived[0]} [{QtCore.QTime.currentTime().toString()}]')
        self.plainTextEdit_RAM.appendPlainText(f'Загрузка RAM: {systemInfoReceived[1]} [{QtCore.QTime.currentTime().toString()}]')

    def changeDelay(self):
        self.thread.delay = int(self.lineEdit_Delay.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
