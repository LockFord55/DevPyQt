from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        # Общие атрибуты
        self.setFixedSize(300, 200)
        self.setWindowTitle('Параметры корабля')

        # Лейблы:
        LabelTemperature = QtWidgets.QLabel('Температура на борту')
        LabelTemperature.setMaximumWidth(75)

        self.LineEditTemperature = QtWidgets.QLineEdit()
        self.LineEditTemperature.setPlaceholderText('22 C')
        self.LineEditTemperature



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()