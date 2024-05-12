"""
Программа должна обладать следующим функционалом:

1. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
2. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signal_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.previous_position = (0, 0)
        self.current_position = (self.window().x(), self.window().y())

        self.position_tracker()

    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.on_PushButtonLT_clicked)
        self.ui.pushButtonRT.clicked.connect(self.on_PushButtonRT_clicked)
        self.ui.pushButtonLB.clicked.connect(self.on_PushButtonLB_clicked)
        self.ui.pushButtonRB.clicked.connect(self.on_PushButtonRB_clicked)
        self.ui.pushButtonCenter.clicked.connect(self.on_PushButtonCenter_clicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.on_PushButtonMoveCoords_clicked)
        self.ui.pushButtonGetData.clicked.connect(self.on_PushButtonGetData_clicked)

    def on_PushButtonLT_clicked(self):
        self.window().move(0, 0)
        # self.position_tracker()

    def on_PushButtonRT_clicked(self):
        self.window().move(width-self.width(), 0)
        # self.position_tracker()

    def on_PushButtonLB_clicked(self):
        self.window().move(0, height-self.height()-80)
        # self.position_tracker()

    def on_PushButtonRB_clicked(self):
        self.window().move(width-self.width(), height-self.height()-80)
        # self.position_tracker()

    def on_PushButtonCenter_clicked(self):
        self.window().move(int((width-self.width())/2), int((height-self.height()-80)/2))
        # self.position_tracker()

    def on_PushButtonMoveCoords_clicked(self):
        self.window().move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())
        # self.position_tracker()

    def on_PushButtonGetData_clicked(self):
        self.ui.plainTextEdit.setPlaceholderText(f'''
    Вывожу данные, состояние на {QtCore.QTime.currentTime().toString()}...\t
    Количество экранов: {len(app.screens())} \t
    Текущее основное окно: ??? \t
    Разрешение экрана: {width}x{height} пикселей \t
    Окно находится на экране №??? \t
    Текущее разрешение окна: {self.window().width()}x{self.window().height()} пикселей \t
    Минимальные размеры окна: {self.window().minimumWidth()}x{self.window().minimumHeight()} пикселей \t
    Текущие координаты окна:   Х: {self.window().x()}   Y: {self.window().y()} \t
    Координаты центра приложения:   Х: {int((width-self.width())/2)}   Y: {int((height-self.height()-80)/2)} \t
    Текущее состояние окна: ???
''')

    def position_tracker(self) -> None:
        print(f'Смена позиции! {QtCore.QTime.currentTime().toString()}')
        self.previous_position = self.current_position
        print(f'Предыдущее положение: {self.previous_position}')
        self.current_position = (self.window().x(), self.window().y())
        print(f'Текущее положение: {self.current_position}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    screen = app.primaryScreen().geometry()
    width = screen.width()
    height = screen.height()

    window = Window()
    window.show()

    app.exec()
