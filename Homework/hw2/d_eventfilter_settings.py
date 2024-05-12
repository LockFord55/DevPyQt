"""
Программа должна обладать следующим функционалом:

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt, QSettings
from ui.d_eventfilter_settings_form import Ui_Form


class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.unite_number = 0
        self.initSignals()

    def initSignals(self):
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxChoice)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Plus:
            if self.unite_number < 100:
                self.unite_number += 1
                print(f'Новое текущее значение: {self.unite_number}')
                self.ui.dial.setValue(self.unite_number)
                self.ui.horizontalSlider.setValue(self.unite_number)
                self.ui.lcdNumber.display(self.unite_number)
        elif event.key() == Qt.Key.Key_Minus:
            if self.unite_number > 0:
                self.unite_number -= 1
                print(f'Новое текущее значение: {self.unite_number}')
                self.ui.dial.setValue(self.unite_number)
                self.ui.horizontalSlider.setValue(self.unite_number)
                self.ui.lcdNumber.display(self.unite_number)

    def comboBoxChoice(self):
        if self.ui.comboBox.currentText() == 'Двоичная':
            self.ui.lcdNumber.setBinMode()
        elif self.ui.comboBox.currentText() == 'Восьмеричная':
            self.ui.lcdNumber.setOctMode()
        elif self.ui.comboBox.currentText() == 'Десятичная':
            self.ui.lcdNumber.setDecMode()
        else:
            self.ui.lcdNumber.setHexMode()


if __name__ == "__main__":
    app = QApplication()

    window = Window()
    window.show()

    app.exec()
