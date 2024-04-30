import PySide6.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    # Main Window
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')  # Подпись окна
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    # Empty container
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter')
        btn_result.clicked.connect(self.func_result)
        btn_clear = qtw.QPushButton('Clear')
        btn_clear.clicked.connect(self.clear_calc)
        btn_9 = qtw.QPushButton('9')
        btn_9.clicked.connect(lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8')
        btn_8.clicked.connect(lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7')
        btn_7.clicked.connect(lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6')
        btn_6.clicked.connect(lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5')
        btn_5.clicked.connect(lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4')
        btn_4.clicked.connect(lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3')
        btn_3.clicked.connect(lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2')
        btn_2.clicked.connect(lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1')
        btn_1.clicked.connect(lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0')
        btn_0.clicked.connect(lambda: self.num_press('0'))
        btn_plus = qtw.QPushButton('+')
        btn_plus.clicked.connect(lambda: self.func_press('+'))
        btn_mins = qtw.QPushButton('-')
        btn_mins.clicked.connect(lambda: self.func_press('-'))
        btn_mult = qtw.QPushButton('*')
        btn_mult.clicked.connect(lambda: self.func_press('*'))
        btn_divd = qtw.QPushButton('/')
        btn_divd.clicked.connect(lambda: self.func_press('/'))

        # Adding the buttons to the layout
        container.layout().addWidget(self.result_field, 0,0,1,4)
        container.layout().addWidget(btn_result, 1,2,1,2)
        container.layout().addWidget(btn_clear, 1,0,1,2)
        container.layout().addWidget(btn_9, 2,2)
        container.layout().addWidget(btn_8, 2,1)
        container.layout().addWidget(btn_7, 2,0)
        container.layout().addWidget(btn_plus, 2,3)
        container.layout().addWidget(btn_6, 3,2)
        container.layout().addWidget(btn_5, 3,1)
        container.layout().addWidget(btn_4, 3,0)
        container.layout().addWidget(btn_mins, 3,3)
        container.layout().addWidget(btn_3, 4,2)
        container.layout().addWidget(btn_2, 4,1)
        container.layout().addWidget(btn_1, 4,0)
        container.layout().addWidget(btn_mult, 4,3)
        container.layout().addWidget(btn_0, 5,0,1,3)
        container.layout().addWidget(btn_divd, 5,3)
        # Добавляем все кнопки, привязанные к контейнеру в виджет
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec()
