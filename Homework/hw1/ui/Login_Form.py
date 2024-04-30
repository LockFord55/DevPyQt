# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Login_form(object):
    def setupUi(self, Login_form):
        if not Login_form.objectName():
            Login_form.setObjectName(u"Login_form")
        Login_form.setEnabled(True)
        Login_form.resize(350, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_form.sizePolicy().hasHeightForWidth())
        Login_form.setSizePolicy(sizePolicy)
        Login_form.setMinimumSize(QSize(350, 200))
        Login_form.setMaximumSize(QSize(350, 200))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        Login_form.setFont(font)
        Login_form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Login_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Label_Login = QLabel(Login_form)
        self.Label_Login.setObjectName(u"Label_Login")
        self.Label_Login.setMinimumSize(QSize(85, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.Label_Login.setFont(font1)
        self.Label_Login.setFrameShape(QFrame.Shape.NoFrame)
        self.Label_Login.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Label_Login)

        self.lineEditLogin = QLineEdit(Login_form)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.lineEditLogin.setFont(font1)
        self.lineEditLogin.setAutoFillBackground(False)
        self.lineEditLogin.setFrame(True)

        self.horizontalLayout.addWidget(self.lineEditLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Label_Password = QLabel(Login_form)
        self.Label_Password.setObjectName(u"Label_Password")
        self.Label_Password.setMinimumSize(QSize(85, 0))
        self.Label_Password.setFont(font1)
        self.Label_Password.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.Label_Password)

        self.lineEditPassword = QLineEdit(Login_form)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setFont(font1)
        self.lineEditPassword.setAutoFillBackground(False)
        self.lineEditPassword.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.lineEditPassword.setFrame(True)
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEditPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton = QPushButton(Login_form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setFont(font1)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Login_form)

        QMetaObject.connectSlotsByName(Login_form)
    # setupUi

    def retranslateUi(self, Login_form):
        Login_form.setWindowTitle(QCoreApplication.translate("Login_form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.Label_Login.setText(QCoreApplication.translate("Login_form", u"Login:", None))
        self.lineEditLogin.setPlaceholderText(QCoreApplication.translate("Login_form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u043b\u043e\u0433\u0438\u043d", None))
        self.Label_Password.setText(QCoreApplication.translate("Login_form", u"Password:", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("Login_form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Login_form", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
    # retranslateUi

