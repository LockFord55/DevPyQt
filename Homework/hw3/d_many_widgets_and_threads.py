"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from b_systeminfo_widget import WindowSystemInfo
from c_weatherapi_widget import WindowWeather
from PySide6 import QtWidgets


class BigWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.windowSystemInfo = WindowSystemInfo()
        self.windowWeather = WindowWeather()

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.windowSystemInfo)
        self.main_layout.addWidget(self.windowWeather)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = BigWindow()
    window.show()

    app.exec()
