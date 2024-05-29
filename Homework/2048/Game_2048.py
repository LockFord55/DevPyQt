import random
import copy
from PySide6 import QtWidgets, QtGui, QtCore


RECT_SIZE = 150
GAME_FIELD = [[(5, 5), (160, 5), (315, 5), (470, 5)],
              [(5, 160), (160, 160), (315, 160), (470, 160)],
              [(5, 315), (160, 315), (315, 315), (470, 315)],
              [(5, 470), (160, 470), (315, 470), (470, 470)]]


class RectLabel(QtWidgets.QLabel):
    colors = {
        '0': 'lightgray',
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
        'over': '3c3a32'
    }

    def __init__(self, parent=None, position=(0, 0)):
        super().__init__(parent)
        self.setGeometry(position[0], position[1], RECT_SIZE, RECT_SIZE)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def changeValue(self, value):
        self.setText(str(value) if value > 0 else ' ')
        bgcolor = self.colors.get(str(value), self.colors['over'])
        self.setStyleSheet(f'background-color:{bgcolor};border-radius:15px;font-size:64px;font:bold')


class GameWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.score = 0
        self.application = QtWidgets.QApplication.instance()

        self.continueGame = False
        self.settings = QtCore.QSettings('MyCompany', '2048')
        self.recordScore = str(self.settings.value('Record', 0))
        self.boardSize = 4
        self.gameOver = False
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        self.init_UI()
        self.start()

    def init_UI(self):
        self.setGeometry((int(1920/2)-250), (int(1080/2)-350), 500, 700)  # TODO сделать динамическое разрешение центра
        self.setWindowTitle('2048 :)')
        self.font = QtGui.QFont('Impact', 32)
        self.font2 = QtGui.QFont('TimesNewRoman', 14)

        # =============================================================================================================

        self.label_CurrentScore = QtWidgets.QLabel('Текущий счёт:')
        self.label_CurrentScore.setFont(self.font2)
        self.label_CurrentScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.plainTextEdit_CurrentScore = QtWidgets.QTextEdit('0')
        self.plainTextEdit_CurrentScore.setReadOnly(True)
        self.plainTextEdit_CurrentScore.setFont(self.font)
        self.plainTextEdit_CurrentScore.setMaximumSize(125, 75)
        self.plainTextEdit_CurrentScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_CurrentScore = QtWidgets.QVBoxLayout()
        self.layout_CurrentScore.addWidget(self.label_CurrentScore)
        self.layout_CurrentScore.addWidget(self.plainTextEdit_CurrentScore)

        self.label_RecordScore = QtWidgets.QLabel('Рекорд:')
        self.label_RecordScore.setFont(self.font2)
        self.label_RecordScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.plainTextEdit_RecordScore = QtWidgets.QTextEdit(self.recordScore)
        #self.plainTextEdit_RecordScore.setText(str(self.recordScore))
        self.plainTextEdit_RecordScore.setReadOnly(True)
        self.plainTextEdit_RecordScore.setFont(self.font)
        self.plainTextEdit_RecordScore.setMaximumSize(125, 75)
        self.plainTextEdit_RecordScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_RecordScore = QtWidgets.QVBoxLayout()
        self.layout_RecordScore.addWidget(self.label_RecordScore)
        self.layout_RecordScore.addWidget(self.plainTextEdit_RecordScore)

        self.layout_Record = QtWidgets.QHBoxLayout()
        self.layout_Record.addLayout(self.layout_CurrentScore)
        self.layout_Record.addLayout(self.layout_RecordScore)

        # =============================================================================================================

        self.groupBox_GameField = QtWidgets.QGroupBox()
        self.groupBox_GameField.setStyleSheet('background-color:black')
        self.groupBox_GameField.setMinimumSize(625, 625)
        self.groupBox_GameField.setMaximumSize(625, 625)

        self.rect1 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[0][0])
        self.rect2 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[0][1])
        self.rect3 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[0][2])
        self.rect4 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[0][3])

        self.rect5 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[1][0])
        self.rect6 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[1][1])
        self.rect7 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[1][2])
        self.rect8 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[1][3])

        self.rect9 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[2][0])
        self.rect10 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[2][1])
        self.rect11 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[2][2])
        self.rect12 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[2][3])

        self.rect13 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[3][0])
        self.rect14 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[3][1])
        self.rect15 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[3][2])
        self.rect16 = RectLabel(parent=self.groupBox_GameField, position=GAME_FIELD[3][3])

        # =============================================================================================================

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.layout_Record)
        self.main_layout.addWidget(self.groupBox_GameField)

        self.setLayout(self.main_layout)

    # =================================================================================================================

    def updateIcon(self):
        px = self.grab(self.groupBox_GameField.rect())
        self.application.setWindowIcon(QtGui.QIcon(px))

    def refreshValue(self):
        self.rect1.changeValue(self.board[0][0])
        self.rect2.changeValue(self.board[0][1])
        self.rect3.changeValue(self.board[0][2])
        self.rect4.changeValue(self.board[0][3])

        self.rect5.changeValue(self.board[1][0])
        self.rect6.changeValue(self.board[1][1])
        self.rect7.changeValue(self.board[1][2])
        self.rect8.changeValue(self.board[1][3])

        self.rect9.changeValue(self.board[2][0])
        self.rect10.changeValue(self.board[2][1])
        self.rect11.changeValue(self.board[2][2])
        self.rect12.changeValue(self.board[2][3])

        self.rect13.changeValue(self.board[3][0])
        self.rect14.changeValue(self.board[3][1])
        self.rect15.changeValue(self.board[3][2])
        self.rect16.changeValue(self.board[3][3])

    def mergeOneRowL(self, row):
        """ Эта функция смещает/сливает одну строку слева """
        # Смещаем всё влево на сколько возможно
        for j in range(self.boardSize - 1):
            for i in range(self.boardSize - 1, 0, -1):
                # Проверяем, если пустая ячейка, то перемещаемся
                if row[i - 1] == 0:
                    row[i - 1] = row[i]
                    row[i] = 0

        # Сливаем всё влево
        for i in range(self.boardSize - 1):
            # Проверяем, что текущее значение идентично соседу
            if row[i] == row[i + 1]:
                row[i] *= 2
                # if not self.checkDifferentMove():
                #     self.score += row[i]
                row[i + 1] = 0

        # Снова двигаем всё влево
        for i in range(self.boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
        return row

    def merge_left(self, currentBoard):
        """ Эта функция смещает всю доску влево """
        # Сливаем каждую строку на доске влево
        for i in range(self.boardSize):
            currentBoard[i] = self.mergeOneRowL(currentBoard[i])

        return currentBoard

    def reverse(self, row):
        """ Эта функция поворачивает вспять порядок одной строки """
        # Добавляем все элементы строки в новый список в обратном порядке
        new = []
        for i in range(self.boardSize - 1, -1, -1):
            new.append(row[i])

        return new

    def merge_right(self, currentBoard):
        """ Эта функция смещает всю доску вправо """
        # Проверяем каждую строку
        for i in range(self.boardSize):
            # Поворачиваем вспять строку, смещаем влево, затем снова поворачиваем вспять
            currentBoard[i] = self.reverse(currentBoard[i])
            currentBoard[i] = self.mergeOneRowL(currentBoard[i])
            currentBoard[i] = self.reverse(currentBoard[i])

        return currentBoard

    def transpose(self, currentBoard):
        """ Эта функция транспонирует всю доску """
        for j in range(self.boardSize):
            for i in range(j, self.boardSize):
                if not i == j:
                    temp = currentBoard[j][i]
                    currentBoard[j][i] = currentBoard[i][j]
                    currentBoard[i][j] = temp

        return currentBoard

    def merge_up(self, currentBoard):
        """ Эта функция транспонирует всю доску вверх, сливает влево, затем транспонирует обратно """
        currentBoard = self.transpose(currentBoard)
        currentBoard = self.merge_left(currentBoard)
        currentBoard = self.transpose(currentBoard)

        return currentBoard

    def merge_down(self, currentBoard):
        """ Эта функция транспонирует всю доску вниз, сливает вправо, затем транспонирует обратно """
        currentBoard = self.transpose(currentBoard)
        currentBoard = self.merge_right(currentBoard)
        currentBoard = self.transpose(currentBoard)

        return currentBoard

    def pickNewValue(self):
        """ Эта функция выбирает, появится ли на поле 2, или редкая 4 """
        if random.randint(1, 8) == 1:
            return 4
        else:
            return 2

    def addNewValue(self):
        """ Эта функция добавляет значение на доску в одну из пустых ячеек """
        rowNum = random.randint(0, self.boardSize - 1)
        colNum = random.randint(0, self.boardSize - 1)

        while not self.board[rowNum][colNum] == 0:
            rowNum = random.randint(0, self.boardSize - 1)
            colNum = random.randint(0, self.boardSize - 1)

        self.board[rowNum][colNum] = self.pickNewValue()

    def checkWin(self):
        """ Эта функция проверяет, выиграл ли игрок """
        if not self.continueGame:
            for row in self.board:
                if 2048 in row:
                    return True
            return False

    def noMoves(self):
        """ Эта функция проверяет, проиграл ли игрок """

        tempBoard1 = copy.deepcopy(self.board)
        tempBoard2 = copy.deepcopy(self.board)
        tempBoard1 = self.merge_down(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = self.merge_up(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = self.merge_left(tempBoard1)
                if tempBoard1 == tempBoard2:
                    tempBoard1 = self.merge_right(tempBoard1)
                    if tempBoard1 == tempBoard2:
                        return True
        else:
            return False

    def start(self):
        # Заполняем 2 места на доске
        numNeeded = 2
        while numNeeded > 0:
            rowNum = random.randint(0, self.boardSize - 1)
            colNum = random.randint(0, self.boardSize - 1)

            if self.board[rowNum][colNum] == 0:
                self.board[rowNum][colNum] = self.pickNewValue()
                numNeeded -= 1

        self.refreshValue()
        self.updateIcon()

    def checkDifferentMove(self):
        if self.tempBoard == self.board:
            return True

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if self.score > int(self.recordScore):
            self.settings.setValue('Record', self.score)
            event.accept()

    def countScore(self, currentBoard, previousBoard):
        sumCurrent = 0
        sumPrevious = 0

        for row in currentBoard:
            sumCurrent += sum(row)

        for row in previousBoard:
            sumPrevious += sum(row)

        self.score += (sumCurrent - sumPrevious) * 2


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key = event.key()
        if key in (QtCore.Qt.Key.Key_A, QtCore.Qt.Key.Key_Left, 1060):
            self.tempBoard = copy.deepcopy(self.board)
            self.board = self.merge_left(self.board)
            if self.checkDifferentMove():
                self.board = self.tempBoard

        elif key in (QtCore.Qt.Key.Key_D, QtCore.Qt.Key.Key_Right, 1042):
            self.tempBoard = copy.deepcopy(self.board)
            self.board = self.merge_right(self.board)
            if self.checkDifferentMove():
                self.board = self.tempBoard

        elif key in (QtCore.Qt.Key.Key_S, QtCore.Qt.Key.Key_Down, 1067):
            self.tempBoard = copy.deepcopy(self.board)
            self.board = self.merge_down(self.board)
            if self.checkDifferentMove():
                self.board = self.tempBoard

        elif key in (QtCore.Qt.Key.Key_W, QtCore.Qt.Key.Key_Up, 1062):
            self.tempBoard = copy.deepcopy(self.board)
            self.board = self.merge_up(self.board)
            if self.checkDifferentMove():
                self.board = self.tempBoard

        else:
            print('Попробуй нажать другую кнопку или сменить раскладку.')

        self.addNewValue()
        self.refreshValue()
        self.countScore(self.board, self.tempBoard)
        self.plainTextEdit_CurrentScore.setText(str(self.score))
        self.plainTextEdit_CurrentScore.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.updateIcon()
        if self.checkWin():
            reply = QtWidgets.QMessageBox.information(self,
                                                      'Победа!',
                                                      f'Вы победили со счётом {self.score}! \n'
                                                      f'Хотите продолжить игру?',
                                                      QtWidgets.QMessageBox.Yes,
                                                      QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.continueGame = True
            else:
                self.application.quit()

        if self.noMoves():
            reply = QtWidgets.QMessageBox.information(self,
                                                      'Поражение!',
                                                      f'Вы проиграли со счётом {self.score}! \n'
                                                      f'В следующий раз повезёт!',
                                                      QtWidgets.QMessageBox.Ok)
            if reply == QtWidgets.QMessageBox.Ok:
                self.application.quit()


if __name__ == '__main__':

    app = QtWidgets.QApplication()

    window = GameWindow()
    window.show()

    app.exec()
