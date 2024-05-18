"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Форма должна содержать:
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from a_threads import SystemInfo
from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self):
        self.setGeometry(800, 300, 250, 250)

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

        # Макет вывода загрузки CPU
        self.label_CPU = QtWidgets.QLabel('Загрузка CPU:')
        self.pushPutton_CPU = QtWidgets.QPushButton('Узнать загрузку CPU')

        layout_CPU = QtWidgets.QVBoxLayout()
        layout_CPU.addWidget(self.label_CPU)
        layout_CPU.addWidget(self.pushPutton_CPU)
        # ===============================================================

        # Макет вывода загрузки RAM
        self.label_RAM = QtWidgets.QLabel('Загрузка RAM:')
        self.pushButton_RAM = QtWidgets.QPushButton('Узнать загрузку RAM')

        layout_RAM = QtWidgets.QVBoxLayout()
        layout_RAM.addWidget(self.label_RAM)
        layout_RAM.addWidget(self.pushButton_RAM)
        # ===============================================================

        # Основной макет
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_Delay)
        layout_main.addLayout(layout_CPU)
        layout_main.addLayout(layout_RAM)

        self.setLayout(layout_main)

    def initThreads(self):
        self.thread = SystemInfo()
        self.thread.start()

    def initSignals(self):
        self.pushPutton_CPU.clicked.connect(self.get_CPU)
        self.pushButton_RAM.clicked.connect(self.get_RAM)

    def get_CPU(self, systemInfoReceived):
        self.label_CPU.setText(f'Загрузка CPU: {systemInfoReceived}')

    def get_RAM(self):
        self.label_RAM.setText(f'Загрузка RAM: {...}')

    def set_Delay(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
