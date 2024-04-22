# import PySide6
# print(PySide6.__version__)
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtWidgets
from main_window import MainWindow


app = QtWidgets.QApplication()

window = MainWindow()
window.show()

app.exec()
