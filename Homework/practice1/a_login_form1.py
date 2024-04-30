from PySide6 import QtWidgets
from ui.login_form import Ui_Form


DEBUG = True


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.LineEditLogin.setText('Введите логин')
        self.ui.LineEditPassword.setText('Введите пароль')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
